import { Component, OnInit, } from '@angular/core';
import { Point } from 'src/app/Models/point';
import { Communication } from 'src/app/Services/communication.service';
import { Lost } from 'src/app/Models/lost';

@Component({
  selector: 'app-map-viewer',
  templateUrl: './map-viewer.component.html',
  styleUrls: ['./map-viewer.component.css']
})
export class MapViewerComponent implements OnInit {

  public zoom = 12;

  public history: Point[];
  public currentLost: Lost = new Lost('', { latitude: 1, longitude: 1 }, 400, 1);
  public currentLosts : Point[];

  constructor(private communication: Communication) {
  }

  ngOnInit() {
    this.communication.onNewHistory().subscribe(data => {
      this.history = data;
    });

    this.communication.onNewLost().subscribe(data => {
      this.currentLost = data;
      this.currentLosts.push(new Point(this.currentLost.location.latitude, this.currentLost.location.longitude));
    });
  }
}


