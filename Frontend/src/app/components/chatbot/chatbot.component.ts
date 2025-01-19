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
    this.http.post<{ message: string }>('http://localhost:8000/api/chatbot', { message: userMessage })
      .subscribe(response => {
        this.messages.push({ sender: 'bot', text: response.message });  // Agregar la respuesta del bot a la conversación
      }, error => {
        this.messages.push({ sender: 'bot', text: 'Lo siento, hubo un error. Intenta nuevamente.' });
      });
  }
}
