import { Component, OnInit } from '@angular/core';
import { TicTacToeService } from '../../services/tic-tac-toe.service';
import { GameStates } from '../../enums/game-states';
import { GameModes } from '../../enums/game-modes';

@Component({
  selector: 'app-tic-tac-toe-board',
  templateUrl: './tic-tac-toe-board.component.html',
  styleUrls: ['./tic-tac-toe-board.component.css']
})
export class TicTacToeBoardComponent implements OnInit {

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
        this.boardService.newGame(GameModes.ComputerStart);
        break;
      case 2:  // type 2 = human start
        this.boardService.newGame(GameModes.HumanStart);
        break;
      case 3:  // type 3 = pvp
        this.boardService.newGame(GameModes.Pvp);
    }
  }
}
