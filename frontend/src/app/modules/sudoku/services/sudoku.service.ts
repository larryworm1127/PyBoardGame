import { Injectable } from '@angular/core';
import { SudokuBoard } from '@modules/sudoku/logic/sudoku-board';
import { SudokuCell, SudokuNum } from '@modules/sudoku/logic/sudoku-cell';
import { Difficulty } from '@modules/sudoku/enums/difficulty';

@Injectable({
  providedIn: 'root'
})
export class SudokuService {

  private gameBoard: SudokuBoard;
  private selectedCell: number = -1;
  numUndo: number = 0;
  pencilEnabled: boolean = false;
  difficulty: Difficulty = Difficulty.Easy;
  gameStarted: boolean = false;

  constructor() {
    this.gameBoard = new SudokuBoard();
  }

  get boardContent(): SudokuCell[] {
    return this.gameBoard.boardContent;
  }

  newGame(): void {
    this.gameStarted = true;
  }

  selectedNewCell(cell: SudokuCell): void {
    // Do nothing if game hasn't started
    if (!this.gameStarted) {
      return;
    }

    // Can't select fixed or already selected cell
    if (!this.boardContent[cell.id].isFixed && !this.boardContent[cell.id].isSelected) {
      if (this.selectedCell === -1) {
        this.gameBoard.updateSelectedCell(cell.id);
      } else {
        this.gameBoard.updateSelectedCell(cell.id, this.selectedCell);
      }
      this.selectedCell = cell.id;
    }
  }

  onNumpadClick(value: SudokuNum): void {
    if (!this.gameStarted || this.selectedCell === -1) {
      return;
    }

    let result = this.gameBoard.makeMove(this.selectedCell, value, this.pencilEnabled);
  }

  erase(): void {
    if (!this.gameStarted || this.selectedCell === -1) {
      return;
    }

    // TODO: add erase move to undo as well
    let result = this.gameBoard.eraseCellValue(this.selectedCell);
  }

  undo(): void {
    if (!this.gameStarted || this.gameBoard.moves.length === 0) {
      return;
    }

    this.numUndo++;
  }
}
