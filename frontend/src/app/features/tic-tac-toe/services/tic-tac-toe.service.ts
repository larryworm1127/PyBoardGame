import { Injectable } from '@angular/core';
import { GameStates } from '../enums/game-states';
import { GameModes } from '../enums/game-modes';
import { Players } from '../enums/players';
import { Square, TicTacToeBoard } from '../utils/tic-tac-toe-board';


@Injectable({
  providedIn: 'any'
})
export class TicTacToeService {

  private gameBoard: TicTacToeBoard;
  private currentTurn: Players = Players.PlayerX;
  private currentState: GameStates = GameStates.Stopped;
  private message: string = 'Who starts?';
  private gameType: GameModes = GameModes.Pvp;

  constructor() {
    this.gameBoard = new TicTacToeBoard();
  }

  newGame(gameType: GameModes): void {
    this.gameType = gameType;
    this.currentState = GameStates.Running;
    this.message = 'Player X turn!';
  }

  resetGame(): void {
    this.gameBoard = new TicTacToeBoard();
    this.message = 'Who starts?';
    this.currentState = GameStates.Stopped;
  }

  get gameTurn(): Players {
    return this.currentTurn;
  }

  get gameState(): GameStates {
    return this.currentState;
  }

  get displayMessage(): string {
    return this.message;
  }

  get board(): Square[] {
    return this.gameBoard.boardContent;
  }

  makeMove(square: Square): void {
    this.currentState = this.gameBoard.update(square);

    switch (this.currentState) {
      case GameStates.Draw:
        this.message = "It's a draw! Press any figure to restart.";
        break;
      case GameStates.OWin:
        this.message = "Player O wins! Press any figure to restart.";
        break;
      case GameStates.XWin:
        this.message = 'Player X wins! Press any figure to restart.';
        break;
      case GameStates.Running:
        if (this.gameTurn === Players.PlayerX) {
          this.currentTurn = Players.PlayerO;
          this.message = 'Player O turn!';
        } else {
          this.currentTurn = Players.PlayerX;
          this.message = 'Player X turn!';
        }
    }
  }
}
