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

  jsonOfData = {}

  @Input()
  indexOfSelectedFolder = 1;

  videoUrl = "";

  ngOnInit() {
    this.createFiles();
  }

  createFiles() {
    const selectedFolder = this.data[this.indexOfSelectedFolder];

    if (selectedFolder && selectedFolder.contents) {
      // Déclarez le type de content explicitement
      const videoFile: string | undefined = selectedFolder.contents.find((content: string) => content.endsWith('.mp4'));

      if (videoFile) {
        this.videoUrl = "https://capydatastorage.s3.eu-north-1.amazonaws.com/" + videoFile;
        console.log(this.videoUrl)
      }
    }
  }

  goBack() {
    this.backEmitter.emit();
  }
}
