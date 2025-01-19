import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent {
  userMessage: string = ''; 
  messages: { sender: string, text: string }[] = []; 

  constructor(private http: HttpClient) {}

  // Método para enviar el mensaje del usuario
  sendMessage() {
    if (this.userMessage.trim()) {
      this.messages.push({ sender: 'user', text: this.userMessage });  // Agregar el mensaje del usuario a la conversación
      this.getBotResponse(this.userMessage);  // Obtener la respuesta del bot
      this.userMessage = '';  // Limpiar el campo de texto
    }
  }

  getBotResponse(userMessage: string) {
    this.http.post<{ response: string }>('http://127.0.0.1:8000/ChatbotAPI/', { mensaje: userMessage })
      .subscribe(
        response => {
          console.log('Respuesta del backend:', response); // Verifica la respuesta en la consola
          this.messages.push({ sender: 'bot', text: response.response }); // Agregar la respuesta del bot
        },
        error => {
          console.error('Error al obtener la respuesta del backend:', error); // Mostrar errores en la consola
          this.messages.push({ sender: 'bot', text: 'Lo siento, hubo un error. Intenta nuevamente.' });
        }
      );
  }
}
