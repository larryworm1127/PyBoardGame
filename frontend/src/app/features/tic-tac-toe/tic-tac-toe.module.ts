import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TicTacToeBoardComponent } from './components/tic-tac-toe-board/tic-tac-toe-board.component';
import { TicTacToeSquareComponent } from './components/tic-tac-toe-square/tic-tac-toe-square.component';



@NgModule({
  declarations: [
    TicTacToeBoardComponent,
    TicTacToeSquareComponent,
  ],
  imports: [
    CommonModule
  ],
  exports: [
    TicTacToeBoardComponent,
    TicTacToeSquareComponent
  ]
})
export class TicTacToeModule { }
