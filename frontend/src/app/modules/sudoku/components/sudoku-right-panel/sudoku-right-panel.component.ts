import { Component, OnInit } from '@angular/core';
import { SudokuService } from '@modules/sudoku/services/sudoku.service';

@Component({
  selector: 'app-sudoku-right-panel',
  templateUrl: './sudoku-right-panel.component.html',
  styleUrls: ['./sudoku-right-panel.component.css']
})
export class SudokuRightPanelComponent implements OnInit {

  constructor(public boardService: SudokuService) { }

  ngOnInit(): void {
  }

}
