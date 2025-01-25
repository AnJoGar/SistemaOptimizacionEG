import { Injectable } from '@angular/core';
import { NotificationComponent } from '../components/notification/notification.component';

import { HttpClient } from '@angular/common/http';
import { Observable, Subject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class NotificacionesService {
  private apiUrl = 'http://localhost:8000/';
  
  // Crear un Subject para emitir notificaciones
  private notificacionSubject = new Subject<{ message: string; type: string }>();

  // Observable para que los componentes se suscriban a las notificaciones
  notificaciones$ = this.notificacionSubject.asObservable();

  constructor(private http: HttpClient) {}

  // Método para mostrar una notificación
  mostrarNotificacion(message: string, type: string) {
    this.notificacionSubject.next({ message, type });  // Emitir notificación
  }

  obtenerEstadoTramite(id: number, tipoTramite: string): Observable<any> {
    let apiEndpoint = '';

    // Asignar la URL correspondiente dependiendo del tipo de trámite
    switch (tipoTramite) {
      case 'visa':
        apiEndpoint = `solicitar-visa/${id}/`;  // URL para el estado de la solicitud de visa
        break;
      case 'pasaporte':
        apiEndpoint = `solicitar-pasaporte/${id}/`;  // URL para el estado de la solicitud de pasaporte
        break;
      case 'cedula':
        apiEndpoint = `solicitar-cedula/${id}/`;  // URL para el estado de la solicitud de cédula
        break;
      default:
        throw new Error('Tipo de trámite no válido');
    }

    // Obtener el estado del trámite con un GET
    return this.http.get(`${this.apiUrl}${apiEndpoint}`);
  }

  // Método para obtener los trámites de un tipo específico
  obtenerTramites(tipoTramite: string): Observable<any[]> {
    let apiEndpoint = '';

    // Asignar la URL correspondiente dependiendo del tipo de trámite
    switch (tipoTramite) {
      case 'visa':
        apiEndpoint = 'solicitar-visa/';  // URL para obtener los trámites de visa
        break;
      case 'pasaporte':
        apiEndpoint = 'solicitar-pasaporte/';  // URL para obtener los trámites de pasaporte
        break;
      case 'cedula':
        apiEndpoint = 'solicitar-cedula/';  // URL para obtener los trámites de cédula
        break;
      default:
        throw new Error('Tipo de trámite no válido');
    }

    // Obtener los trámites de un tipo específico
    return this.http.get<any[]>(`${this.apiUrl}${apiEndpoint}`);
  }

}