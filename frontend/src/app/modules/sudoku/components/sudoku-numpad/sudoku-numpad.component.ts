import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-sudoku-numpad',
  templateUrl: './sudoku-numpad.component.html',
  styleUrls: ['./sudoku-numpad.component.css']
})
export class SudokuNumpadComponent implements OnInit {

  numbers: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

  constructor() { }

  ngOnInit(): void {
  }

}
