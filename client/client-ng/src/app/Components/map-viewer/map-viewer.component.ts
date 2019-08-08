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

  public history: Point[] = [
    new Point(29.508811268373627, 34.959637279668414),
    new Point(29.51188374700389, 34.97408013527024),
    new Point(29.519999074265993, 34.959637279668414),
    new Point(29.519784421496425, 34.99407297788298)
  ];

  public currentLost: Lost = new Lost('',
    { latitude: 29.519784421496425, longitude: 34.99407297788298 },
    400,
    1);

  constructor(private communication: Communication) {
  }

  ngOnInit() {
    // this.communication.onNewHistory().subscribe(data => {
    //   this.history = data;
    // });

    // this.communication.onNewLost().subscribe(data => {
    //   console.log(data);
    //   this.currentLost = data;
    //   this.currentLosts.push(new Point(this.currentLost.location.latitude, this.currentLost.location.longitude));
    // });
  }
}


