import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TramiteService {
  private apiUrl = 'http://localhost:8000/';

  constructor(private http: HttpClient) {}

  crearTramite1(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}`, data);
  }

  obtenerEstadoTramite1(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}/${id}`);
  }

  obtenerTramites1(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  crearTramite(data: any): Observable<any> {
    let apiEndpoint = '';

    // Verificar el tipo de trámite y asignar la URL correspondiente
    switch (data.tipoTramite) {
      case 'visa':
        apiEndpoint = 'solicitar-visa/';  // Endpoint para solicitar visa
        break;
      case 'pasaporte':
        apiEndpoint = 'solicitar-pasaporte/';  // Endpoint para solicitar pasaporte
        break;
      case 'cedula':
        apiEndpoint = 'solicitar-cedula/';  // Endpoint para solicitar cédula
        break;
      default:
        throw new Error('Tipo de trámite no válido');
    }

    // Enviar solicitud POST a la URL correspondiente con los datos del trámite
    return this.http.post(`${this.apiUrl}${apiEndpoint}`, data);
  }


// Método para obtener el estado de un trámite por su ID y tipo
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



guardarTramite(tramiteData: any): void {
  let tramites = JSON.parse(localStorage.getItem('tramites') || '[]');
  tramites.push(tramiteData);
  localStorage.setItem('tramites', JSON.stringify(tramites));
}

// Obtener los trámites desde el localStorage
obtenerTramitesT(): any[] {
  return JSON.parse(localStorage.getItem('tramites') || '[]');
}

// Simular un servicio que manda la solicitud del trámite a la API
crearTramiteT(tramiteData: any) {
  // Aquí iría la llamada HTTP real a la API
  return new Observable(observer => {
    setTimeout(() => {
      observer.next({ success: true });
      observer.complete();
    }, 1000);
  });
}

}
