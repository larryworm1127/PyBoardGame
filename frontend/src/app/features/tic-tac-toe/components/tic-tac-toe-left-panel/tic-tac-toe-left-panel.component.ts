import { Component, OnInit } from '@angular/core';
import { GameStates } from '@features/tic-tac-toe/enums/game-states';
import { GameModes } from '@features/tic-tac-toe/enums/game-modes';
import { TicTacToeService } from '@features/tic-tac-toe/services/tic-tac-toe.service';

@Component({
  selector: 'app-tic-tac-toe-left-panel',
  templateUrl: './tic-tac-toe-left-panel.component.html',
  styleUrls: ['./tic-tac-toe-left-panel.component.css']
})
export class TicTacToeLeftPanelComponent implements OnInit {

  constructor(public boardService: TicTacToeService) { }

  ngOnInit(): void {
  }

  onClick(type: GameModes): void {
    this.boardService.startGame(type);
  }
}
