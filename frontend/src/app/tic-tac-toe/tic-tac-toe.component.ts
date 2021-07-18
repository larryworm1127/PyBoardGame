import { Component, OnInit } from '@angular/core';
import { GameStates, GameType, TicTacToeService } from '../tic-tac-toe.service';

@Component({
  selector: 'app-tic-tac-toe',
  templateUrl: './tic-tac-toe.component.html',
  styleUrls: ['./tic-tac-toe.component.css']
})
export class TicTacToeComponent implements OnInit {

  constructor(public boardService: TicTacToeService) { }

  ngOnInit(): void {
  }

  startGame(type: number): void {
    switch (this.boardService.gameState) {
      case GameStates.XWin:
      case GameStates.OWin:
      case GameStates.Draw:
        this.boardService.resetGame();
        break;
      case GameStates.Stopped:
        this.newGame(type);
        break;
    }
  }

  private newGame(type: number) {
    switch (type) {
      case 1:  // type 1 = computer start
        this.boardService.newGame(GameType.ComputerStart);
        break;
      case 2:  // type 2 = human start
        this.boardService.newGame(GameType.HumanStart);
        break;
      case 3:  // type 3 = pvp
        this.boardService.newGame(GameType.Pvp);
    }
  }
}
