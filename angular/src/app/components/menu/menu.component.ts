import { Component, EventEmitter, Output } from '@angular/core';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.scss']
})
export class MenuComponent {

  @Output()
  menuEmitter = new EventEmitter();

  handleMenu(index: number) {
    this.menuEmitter.emit(index);
  }

}
