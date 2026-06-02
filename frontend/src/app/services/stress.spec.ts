import { TestBed } from '@angular/core/testing';

import { Stress } from './stress';

describe('Stress', () => {
  let service: Stress;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(Stress);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
