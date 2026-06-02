import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StressService {

  private apiUrl = 'http://127.0.0.1:8000/predict';

  constructor(private http: HttpClient) {}

  predictStress(data: any) {
    return this.http.post(this.apiUrl, data);
  }
}