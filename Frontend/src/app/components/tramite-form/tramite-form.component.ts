import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TramiteService } from '../../services/tramite.service';
import { Router } from '@angular/router';

import { MatSnackBar } from '@angular/material/snack-bar';
@Component({
  selector: 'app-formulario-tramite',
  templateUrl: './tramite-form.component.html',
  styleUrls: ['./tramite-form.component.css']
})
export class FormularioTramiteComponent implements OnInit {
  tramiteForm: FormGroup;

  constructor(
    private fb: FormBuilder,
    private tramiteService: TramiteService,
    private router: Router
  ) {
    this.tramiteForm = this.fb.group({
      tipoTramite: ['', Validators.required],
      nombre: ['', [Validators.required, Validators.maxLength(100)]],
      fecha_nacimiento: ['', Validators.required],
      paisOrigen: [''],
      motivoViaje: [''],
      tipoVisa: [''],
      numeroPasaporte: ['', Validators.maxLength(50)],
      telefono_contacto: ['', Validators.pattern('^\\+?[0-9]*$')],
      email_contacto: ['', Validators.email],
      direccion: [''],
      lugar_nacimiento: ['']
      
    });
  }

  mensajeExito: boolean = false;

  ngOnInit(): void {}

   // Método que se ejecuta cuando se envía el formulario
   onSubmit(): void {

   
    if (this.tramiteForm.valid) {

      const tipoTramite1 = this.tramiteForm.value.tipoTramite;
      console.log('Tipo de trámite seleccionado:', tipoTramite1);  // Depuración
  
      // Verificar que el tipo de trámite esté dentro de los valores válidos
      if (!['visa', 'pasaporte', 'cedula'].includes(tipoTramite1)) {
        console.error('Error: Tipo de trámite no válido');
        return;  // Detener la ejecución si el tipo de trámite es inválido
      }
      // Crear un objeto vacío que se enviará al servidor
      const tipoTramite= this.tramiteForm.value.tipoTramite;
      let tramiteData: any = {
        tipoTramite: this.tramiteForm.value.tipoTramite,
        nombre: this.tramiteForm.value.nombre,
        fecha_nacimiento: this.tramiteForm.value.fecha_nacimiento,
        telefono_contacto: this.tramiteForm.value.telefono_contacto,
        email_contacto: this.tramiteForm.value.email_contacto,
        estado: 'Pendiente', // Valor por defecto
      };
  
     
  
      // Dependiendo del tipo de trámite, agregar campos adicionales
      if (tipoTramite === 'visa') {
        tramiteData.pais_origen = this.tramiteForm.value.paisOrigen;
        tramiteData.motivo_viaje = this.tramiteForm.value.motivoViaje;
        tramiteData.tipo_visa = this.tramiteForm.value.tipoVisa;
        tramiteData.numero_pasaporte = this.tramiteForm.value.numeroPasaporte;
      } else if (tipoTramite === 'pasaporte') {
        tramiteData.nacionalidad = this.tramiteForm.value.paisOrigen; // Asumí que 'paisOrigen' corresponde a 'nacionalidad'
        tramiteData.fecha_emision = this.tramiteForm.value.fecha_nacimiento; // Cambiar a la fecha adecuada si es diferente
        tramiteData.direccion = this.tramiteForm.value.direccion;
      } else if (tipoTramite === 'cedula') {
        tramiteData.direccion = this.tramiteForm.value.direccion;
        tramiteData.lugar_nacimiento = this.tramiteForm.value.lugar_nacimiento;
      }
  
      console.log('Datos enviados al servidor:', tramiteData);  // Depuración
   // Guardar el trámite en el servicio
   this.tramiteService.guardarTramite(tramiteData);

   // Enviar los datos al servicio
   this.tramiteService.crearTramiteT(tramiteData).subscribe(
     response => {
       console.log('Trámite creado exitosamente:', response);
       this.router.navigate(['/tramite-confirmacion']);
       this.mensajeExito = true;
       setTimeout(() => {
        this.mensajeExito = false;
        this.tramiteForm.reset();  // Limpiar el formulario
      }, 3000);
     },
     error => {
       console.error('Error al crear el trámite:', error);
     }
   );
      // Enviar los datos al servicio
      this.tramiteService.crearTramite(tramiteData).subscribe(
        response => {
          console.log('Trámite creado exitosamente:', response);
          this.router.navigate(['/tramite-confirmacion']);
        },
        error => {
          console.error('Error al crear el trámite:', error);
        }
      );
    }
  }
  

  // Método para mostrar los campos adicionales basados en el tipo de trámite
  mostrarCamposAdicionales(tipoTramite: string): boolean {
    return (
      tipoTramite === 'visa' || tipoTramite === 'pasaporte' || tipoTramite === 'cedula'
    );
  }

  // Método para obtener la URL base que se utilizará en la creación del trámite
  obtenerApiUrl(): string {
    const tipoTramite = this.tramiteForm.value.tipoTramite;
    switch (tipoTramite) {
      case 'visa':
        return 'solicitar-visa/';
      case 'pasaporte':
        return 'solicitar-pasaporte/';
      case 'cedula':
        return 'solicitar-cedula/';
      default:
        throw new Error('Tipo de trámite no válido');
    }
  }
}
