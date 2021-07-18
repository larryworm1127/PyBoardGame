import { Injectable } from '@angular/core';


export enum GameStates {
  XWin,
  OWin,
  Draw,
  Running,
  Stopped
}

export enum Players {
  PlayerX,
  PlayerO
}

export enum GameType {
  ComputerStart,
  HumanStart,
  Pvp
}

type Square = {
  id: number;
  state: Players | null;
};


@Injectable({
  providedIn: 'any'
})
export class TicTacToeService {

  private gameBoard: TicTacToeBoard;
  private currentTurn: Players = Players.PlayerX;
  private currentState: GameStates = GameStates.Stopped;
  private message: string = 'Who starts?';
  private gameType: GameType = GameType.Pvp;

  constructor() {
    this.gameBoard = new TicTacToeBoard();
  }

  newGame(gameType: GameType): void {
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


class TicTacToeBoard {

  private board: Square[] = [];
  private boardDim: number = 9;

  constructor() {
    this.board = this.createBoard();
  }

  get boardContent() {
    return this.board;
  }

  createBoard(): Square[] {
    let board = [];
    for (let i = 0; i < this.boardDim; i++) {
      board.push({ id: i, state: null });
    }
    return board;
  }

  getEmptySquares(): Square[] {
    return this.board.filter(square => square.state === null);
  }

  update(square: Square): GameStates {
    this.board[square.id].state = square.state;
    return this.checkWin();
  }

  checkWin(): GameStates {
    // Initialize lines with diagonals
    let lines = [
      [this.board[0], this.board[4], this.board[8]],
      [this.board[2], this.board[4], this.board[6]],
    ];

    // Add rows and columns
    for (let i = 0; i < 3; i++) {
      // row
      lines.push([
        this.board[i * 3],
        this.board[i * 3 + 1],
        this.board[i * 3 + 2],
      ])

      // column
      lines.push([
        this.board[i],
        this.board[i + 3],
        this.board[i + 6],
      ])
    }

    // Check all lines
    for (let line of lines) {
      if (line.every((val, i, arr) => val.state === arr[0].state && val.state !== null)) {
        return (line[0].state === Players.PlayerX) ? GameStates.XWin : GameStates.OWin;
      }
    }

    // No winner, check for draw
    if (this.getEmptySquares().length == 0) {
      return GameStates.Draw;
    }
    return GameStates.Running;
  }
}
