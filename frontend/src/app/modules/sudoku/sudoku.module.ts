import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SudokuRoutingModule } from '@modules/sudoku/sudoku-routing.module';
import { SudokuComponent } from './pages/sudoku.page';


@NgModule({
  declarations: [
    SudokuComponent
  ],
  imports: [
    CommonModule,
    SudokuRoutingModule
  ]
})
export class SudokuModule { }
