import { Component, OnInit } from '@angular/core';
import { SudokuService } from '@modules/sudoku/services/sudoku.service';
import { SudokuNum } from '@modules/sudoku/logic/sudoku-cell';

@Component({
  selector: 'app-sudoku-numpad',
  templateUrl: './sudoku-numpad.component.html',
  styleUrls: ['./sudoku-numpad.component.css']
})
export class SudokuNumpadComponent implements OnInit {

  numbers: SudokuNum[] = [1, 2, 3, 4, 5, 6, 7, 8, 9];

  constructor(public boardService: SudokuService) { }

  ngOnInit(): void {
  }

  onClick(value: SudokuNum): void {
    this.boardService.onNumpadClick(value);
  }
}
