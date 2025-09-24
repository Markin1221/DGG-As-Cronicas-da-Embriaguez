import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class BattleService {
  private API_URL = 'http://127.0.0.1:8000/api';

  constructor(private http: HttpClient) { }

  atacar(personagemId: number, inimigoId: number, ataqueId: number): Observable<any> {
    return this.http.post(`${this.API_URL}/ataque`, {
      personagem_id: personagemId,
      inimigo_id: inimigoId,
      ataque_id: ataqueId
    });
    }
}
