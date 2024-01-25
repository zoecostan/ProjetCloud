import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MenuComponent } from './components/menu/menu.component';
import { VideoStepParentComponent } from './pages/video-step-parent/video-step-parent.component';
import { VideoStep1Component } from './pages/video-step-parent/components/video-step1/video-step1.component';

@NgModule({
  declarations: [
    AppComponent,
    MenuComponent,
    VideoStepParentComponent,
    VideoStep1Component,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
