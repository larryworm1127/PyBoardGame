import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-tic-tac-toe-page',
  templateUrl: './tic-tac-toe-page.component.html',
  styleUrls: ['./tic-tac-toe-page.component.css']
})
export class TicTacToePageComponent implements OnInit {

  gameName: string = "Tic Tac Toe";

  constructor() { }

  ngOnInit(): void {
  }

}
