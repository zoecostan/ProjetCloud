import { Component } from '@angular/core';

@Component({
  selector: 'app-video-step-parent',
  templateUrl: './video-step-parent.component.html',
  styleUrls: ['./video-step-parent.component.scss']
})
export class VideoStepParentComponent {

  step = 1;

  currentObject =     {
    title: "",
    urlMiniature: "",
    length: "",
    langue: "",
    animals: false,
    description: ""
  };

  handleCardClick(object: any){
    this.currentObject = object;
    this.step = 2;
  }

  goBackStep1(){
    this.step = 1;
  }
}
