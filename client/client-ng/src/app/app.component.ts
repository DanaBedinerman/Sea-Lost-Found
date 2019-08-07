import { Component } from '@angular/core';
import { Communication } from './Services/communication.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'client-ng';

  constructor(communication: Communication) {}
}
