import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SudokuRoutingModule } from '@modules/sudoku/sudoku-routing.module';
import { SudokuComponent } from './pages/sudoku.page';
import { SudokuBoardComponent } from './components/sudoku-board/sudoku-board.component';
import { SudokuNumpadComponent } from './components/sudoku-numpad/sudoku-numpad.component';
import { SudokuCellComponent } from './components/sudoku-cell/sudoku-cell.component';
import { SudokuRightPanelComponent } from './components/sudoku-right-panel/sudoku-right-panel.component';
import { SudokuControlsComponent } from './components/sudoku-controls/sudoku-controls.component';


@NgModule({
  declarations: [
    SudokuComponent,
    SudokuBoardComponent,
    SudokuNumpadComponent,
    SudokuCellComponent,
    SudokuRightPanelComponent,
    SudokuControlsComponent
  ],
  imports: [
    CommonModule,
    SudokuRoutingModule
  ]
})
export class SudokuModule { }
