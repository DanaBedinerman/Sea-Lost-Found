import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {Communication} from './Services/communication.service';
import { MapViewerComponent } from './Components/map-viewer/map-viewer.component';

import { AgmCoreModule } from '@agm/core';

@NgModule({
  declarations: [
    AppComponent,
    MapViewerComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    AgmCoreModule.forRoot({
      apiKey: 'AIzaSyC_1P6RonfgA04hdaixEsBRZV3Ey_O95cc'
    })
  ],
  providers: [Communication],
  bootstrap: [AppComponent]
})
export class AppModule { }
