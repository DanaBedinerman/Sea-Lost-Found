import { Injectable } from '@angular/core';
import * as io from 'socket.io-client';
import { Lost } from '../Models/lost';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class Communication {
  private url = 'http://localhost:8080';
  private socket;

  constructor() {
    this.socket = io();
  }

  onNewHistory() {
    return Observable.create(observer => {
      this.socket.on('objcet_history', data => {
        observer.next(data.history);
      });
    });
  }

  onNewLost() {
    return Observable.create(observer => {
      this.socket.on('objcet_location',
        data => {
          observer.next(new Lost(data.id, data.location, data.raduis, data.angle));
        });
    });
  }
}
