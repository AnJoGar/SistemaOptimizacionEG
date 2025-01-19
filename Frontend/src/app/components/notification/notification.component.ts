import { Component } from '@angular/core';
import { NotificacionesService } from '../../services/Notificaciones.service';

@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrl: './notification.component.css'
})
export class NotificationComponent {
    // Array para contener las notificaciones
    notificaciones: { message: string, type: string }[] = [];

    constructor(private notificacionesService: NotificacionesService) {}

    ngOnInit(): void {}

    // Método para agregar una nueva notificación
    agregarNotificacion(message: string, type: string) {
      this.notificaciones.push({ message, type });
      // Auto eliminar la notificación después de 5 segundos
      setTimeout(() => this.eliminarNotificacion(0), 5000);
    }

    // Método para eliminar notificación
    eliminarNotificacion(index: number) {
      this.notificaciones.splice(index, 1);
    }

    enviarTramite() {
      this.notificacionesService.mostrarNotificacion('Trámite realizado con éxito!', 'success');
    }
}
