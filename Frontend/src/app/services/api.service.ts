import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  sendChatMessage(message: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/ChatbotAPI/`, { message });
  }

  submitTramite(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/tramite`, data);
  }

  getTramiteStatus(tramiteId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/tramite/${tramiteId}`);
  }
}
