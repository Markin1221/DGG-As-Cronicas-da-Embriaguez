import { Component } from '@angular/core';
import { IonHeader, IonToolbar, IonTitle, IonContent, IonButton } from '@ionic/angular/standalone';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
  imports: [IonHeader, IonToolbar, IonTitle, IonContent, IonButton],
})
export class HomePage {
  constructor(private router: Router) {}

  startGame() {
    console.log("Novo jogo iniciado!");
    // exemplo: navegar para a tela do jogo
    this.router.navigate(['/game']);
  }

  openSaves() {
    console.log("Abrindo saves...");
    this.router.navigate(['/saves']);
  }

  showsettings() {
    console.log("Abrindo configurações...");
    this.router.navigate(['/settings']);
  }

  exitGame() {
    console.log("Saindo do jogo...");
    // no navegador não dá pra fechar janela direto, mas pode redirecionar
    this.router.navigate(['/exit']);
  }
}
