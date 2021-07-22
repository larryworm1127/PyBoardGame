import { Injectable } from '@angular/core';
import { SudokuBoard, UpdateResult } from '@modules/sudoku/logic/sudoku-board';
import { SudokuCell } from '@modules/sudoku/logic/sudoku-cell';
import { Difficulty } from '@modules/sudoku/enums/difficulty';


const tempBoard = [
  0, 1, 0, 0, 4, 0, 5, 6, 0,
  2, 3, 0, 6, 1, 5, 0, 8, 0,
  0, 0, 0, 8, 0, 0, 1, 0, 0,
  0, 5, 0, 0, 2, 0, 0, 0, 8,
  6, 0, 0, 7, 8, 1, 0, 0, 5,
  9, 0, 0, 0, 6, 0, 0, 2, 0,
  0, 0, 6, 0, 0, 8, 0, 0, 0,
  0, 8, 0, 4, 7, 3, 0, 5, 6,
  0, 4, 5, 0, 9, 0, 0, 1, 0
]


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
    this.gameBoard.boardContent = tempBoard.map((value, index) =>
      new SudokuCell(
        index,
        (value !== 0) ? value : null,
        value !== 0
      )
    )
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

  onNumpadClick(value: number): void {
    if (!this.gameStarted || this.selectedCell === -1) {
      return;
    }

    let result = this.gameBoard.makeMove(this.selectedCell, value, this.pencilEnabled);
    this.updateErrorToDuplicates(result);
  }

  erase(): void {
    if (!this.gameStarted || this.selectedCell === -1) {
      return;
    }

    // TODO: add erase move to undo as well
    let result = this.gameBoard.eraseCellValue(this.selectedCell);
    console.log(result)
    this.updateErrorToDuplicates(result);
  }

  private updateErrorToDuplicates(verifyResult: UpdateResult): void {
    if (verifyResult.isComplete) {
      return;
    }

    for (let cell of this.boardContent) {
      cell.hasError = cell.value !== null && verifyResult.duplicates.includes(cell.value) && !cell.isPencil;
    }
  }

  undo(): void {
    if (!this.gameStarted || this.gameBoard.moves.length === 0) {
      return;
    }

    this.numUndo++;
  }
}
