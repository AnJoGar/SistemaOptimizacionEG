import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TramiteService {
  private apiUrl = 'http://localhost:8000/api/tramites';

  constructor(private http: HttpClient) {}

  crearTramite(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/create/`, data);
  }

  obtenerEstadoTramite(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/${id}/status/`);
  }

  obtenerTramites(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }
}
