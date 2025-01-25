import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { ChatbotComponent } from './components/chatbot/chatbot.component';
import { FormularioTramiteComponent } from './components/tramite-form/tramite-form.component';
import { NotificationComponent } from './components/notification/notification.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'chatbot', component: ChatbotComponent },
  { path: 'registra-consulta', component: FormularioTramiteComponent },
  { path: 'notificaciones', component: NotificationComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }