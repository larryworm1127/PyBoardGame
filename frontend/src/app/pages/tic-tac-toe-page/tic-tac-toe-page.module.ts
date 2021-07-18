import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { TicTacToePageComponent } from './tic-tac-toe-page.component';
import { TicTacToeModule } from '@features/tic-tac-toe/tic-tac-toe.module';
import { TicTacToePageRoutingModule } from './tic-tac-toe-page-routing.module';


@NgModule({
  declarations: [TicTacToePageComponent],
  imports: [
    CommonModule,
    TicTacToeModule,

    TicTacToePageRoutingModule
  ]
})
export class TicTacToePageModule {
}
