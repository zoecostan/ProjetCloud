import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-video-step2',
  templateUrl: './video-step2.component.html',
  styleUrls: ['./video-step2.component.scss']
})
export class VideoStep2Component {

  @Output()
  backEmitter = new EventEmitter();

  @Input()
  data: any[] = [];

  @Input()
  indexOfSelectedFolder = 1;

  goBack() {
    this.backEmitter.emit()
  }

}
