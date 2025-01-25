import { Component, OnInit } from '@angular/core';
import { NotificacionesService } from '../../services/Notificaciones.service';
import { TramiteService } from '../../services/tramite.service';
@Component({
  selector: 'app-notification',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.css']
})
export class NotificationComponent implements OnInit {
  // Array para contener las notificaciones
  notificaciones: { message: string, type: string }[] = [];
  
  // Array para contener los trámites
  tramites: any[] = [];
  tramites2: any[] = [];
  constructor(private notificacionesService: NotificacionesService,private tramiteService: TramiteService) {}

  ngOnInit(): void {
    // Suscribirse al observable para recibir las notificaciones
    this.notificacionesService.notificaciones$.subscribe((notificacion) => {
      this.agregarNotificacion(notificacion.message, notificacion.type);
    });

    // Llamar al método para obtener los trámites, por ejemplo, 'visa'
    this.obtenerTramites('visa');
    this.obtenerTramites('cedula');
      // Obtener los trámites desde el servicio
      this.obtenerTramites('pasaporte');
      
  }

  // Método para agregar una nueva notificación
  agregarNotificacion(message: string, type: string) {
    this.notificaciones.push({ message, type });
    // Auto eliminar la notificación después de 5 segundos
    setTimeout(() => this.eliminarNotificacion(0), 50000);
  }

  // Método para eliminar notificación
  eliminarNotificacion(index: number) {
    this.notificaciones.splice(index, 1);
  }

  // Método para obtener los trámites y mostrarlos
  obtenerTramites(tipoTramite: string) {
    this.tramiteService.obtenerTramites(tipoTramite).subscribe({
      next: (data) => {
        this.tramites.push(...data);
        this.notificacionesService.mostrarNotificacion(
          `Trámites obtenidos con éxito para ${tipoTramite}: ${JSON.stringify(data)}`,
          'success'
        );
      },
      error: (err) => {
        this.notificacionesService.mostrarNotificacion(
          `Error al obtener los trámites de ${tipoTramite}: ${err.message}`,
          'error'
        );
      }
    });
  }

  // Método para enviar una notificación al servicio
  enviarTramite() {
    this.notificacionesService.mostrarNotificacion('Trámite realizado con éxito!', 'success');
  }
}
