/* tslint:disable:no-unused-variable */

import { TestBed, async, inject } from '@angular/core/testing';
import { TramiteService } from './tramite.service';

describe('Service: Tramite', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TramiteService]
    });
  });

  it('should ...', inject([TramiteService], (service: TramiteService) => {
    expect(service).toBeTruthy();
  }));
});
