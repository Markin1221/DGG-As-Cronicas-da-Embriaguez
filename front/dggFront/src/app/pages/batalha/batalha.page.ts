import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { IonButton, IonContent, IonHeader, IonTitle, IonToolbar } from '@ionic/angular/standalone';

@Component({
  selector: 'app-batalha',
  templateUrl: './batalha.page.html',
  styleUrls: ['./batalha.page.scss'],
  standalone: true,
  imports: [IonContent, IonHeader, IonTitle, IonToolbar, CommonModule, FormsModule, IonButton]
})
export class BatalhaPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }
  mostrarAtaques = false;
   toggleAtaques() {
    this.mostrarAtaques = !this.mostrarAtaques;
  }
}
