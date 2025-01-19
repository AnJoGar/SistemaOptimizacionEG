import { Injectable } from '@angular/core';
import { NotificationComponent } from '../components/notification/notification.component';

@Injectable({
  providedIn: 'root'
})
export class NotificacionesService {
  constructor(private notificacionesComponent: NotificationComponent) {}

  // Método para mostrar una notificación
  mostrarNotificacion(message: string, type: string) {
    this.notificacionesComponent.agregarNotificacion(message, type);
  }
}
