import { Component, Output,EventEmitter } from '@angular/core';

@Component({
  selector: 'app-video-step1',
  templateUrl: './video-step1.component.html',
  styleUrls: ['./video-step1.component.scss']
})
export class VideoStep1Component {

  @Output()
  indexCardEmitter = new EventEmitter();

  tmpVideosData = [
    {
      title: "Qui est l'imposteur ?",
      urlMiniature: "https://static.hitek.fr/img/actualite/ill_m/1000626241/squeezie.jpg",
      length: "47:10",
      langue: "francais",
      animals: false,
      description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      title: "Micode et le hacking",
      urlMiniature: "https://i.ytimg.com/vi/6Jv0EzXdQbk/maxresdefault.jpg",
      length: "12:34",
      langue: "francais",
      animals: false,
      description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

    },
    {
      title: "Le lievre et le guepard",
      urlMiniature: "https://www.radiofrance.fr/s3/cruiser-production/2018/02/3b1436e7-3fdc-4899-805d-d93108bcc814/1200x680_thehunt_05_grab_.jpg",
      length: "59:15",
      langue: "english",
      animals: true,
      description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
      title: "Les poissons sont ils sympa ?",
      urlMiniature: "https://www.socialter.fr/images/article/t/docuanimalier_1639478115-1170x749.jpg",
      length: "17:37",
      langue: "francais",
      animals: true,
      description: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
  ]

  handleCardClick(i: number) {
    this.indexCardEmitter.emit(this.tmpVideosData[i]);
  }


}
