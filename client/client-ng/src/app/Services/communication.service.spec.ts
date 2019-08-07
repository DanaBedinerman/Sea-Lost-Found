import { TestBed } from '@angular/core/testing';

import { Communication } from './communication.service';

describe('Communication', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: Communication = TestBed.get(Communication);
    expect(service).toBeTruthy();
  });
});
