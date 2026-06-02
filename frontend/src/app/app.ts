import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { StressService } from './services/stress';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './app.html',
  styleUrl: './app.css'
})
export class App {

  formData = {
    age: 23,
    gender: 'male',
    occupation: 'student',
    daily_screen_time_hours: 10,
    phone_usage_before_sleep_minutes: 0,
    sleep_duration_hours: 8,
    sleep_quality_score: 9,
    caffeine_intake_cups: 2,
    physical_activity_minutes: 15,
    notifications_received_per_day: 10,
    mental_fatigue_score: 7
  };

  result: any = null;
  errorMessage: string = '';
  loading: boolean = false;

  constructor(private stressService: StressService) {}

  onSubmit() {
    this.result = null;
    this.errorMessage = '';
    this.loading = true;

    console.log('Form data:', this.formData);

    this.stressService.predictStress(this.formData).subscribe({
      next: (response: any) => {
        console.log('Backend response:', response);

        this.result = {
          stress_score: response.stress_score,
          stress_category: response.stress_category,
          message: response.message
        };

        this.loading = false;
      },
      error: (error) => {
        console.log('Backend error:', error);

        this.errorMessage = error.error?.detail || 'Backend error occurred';
        this.loading = false;
      },
      complete: () => {
        console.log('Request completed');
        this.loading = false;
      }
    });
  }
}