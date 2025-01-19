import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TramiteService } from '../../services/tramite.service';
import { Router } from '@angular/router';

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
      fechaNacimiento: ['', Validators.required],
      paisOrigen: [''],
      motivoViaje: [''],
      tipoVisa: [''],
      numeroPasaporte: ['', Validators.maxLength(50)],
      telefonoContacto: ['', Validators.pattern('^\\+?[0-9]*$')],
      emailContacto: ['', Validators.email],
      direccionContacto: [''],
      lugarNacimiento: [''],
    });
  }

  ngOnInit(): void {}

  onSubmit(): void {
    if (this.tramiteForm.valid) {
      const tramiteData = this.tramiteForm.value;
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

  mostrarCamposAdicionales(tipoTramite: string): boolean {
    return (
      tipoTramite === 'visa' || tipoTramite === 'pasaporte' || tipoTramite === 'cedula'
    );
  }
}
