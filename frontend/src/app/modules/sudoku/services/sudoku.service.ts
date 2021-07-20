import { Injectable } from '@angular/core';
import { SudokuBoard } from '@modules/sudoku/logic/sudoku-board';
import { SudokuCell } from '@modules/sudoku/logic/sudoku-cell';

@Injectable({
  providedIn: 'root'
})
export class SudokuService {

  private gameBoard: SudokuBoard;
  private selectedCell: number = 0;
  numUndo: number = 0;
  pencilEnabled: boolean = false;

  constructor() {
    this.gameBoard = new SudokuBoard();
  }

  get boardContent(): SudokuCell[] {
    return this.gameBoard.boardContent;
  }

  selectedNewCell(cell: SudokuCell) {
    if (!this.boardContent[cell.id].isFixed && !this.boardContent[cell.id].isSelected) {
      this.gameBoard.updateSelectedCell(this.selectedCell, cell.id);
      this.selectedCell = cell.id;
    }
  }
}
