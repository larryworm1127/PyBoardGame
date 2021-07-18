import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from '@angular/router';
import { TicTacToePageComponent } from './tic-tac-toe-page.component';

const routes: Routes = [{ path: '', component: TicTacToePageComponent }]


@NgModule({
  declarations: [],
  imports: [
    RouterModule.forChild(routes),
    CommonModule
  ],
  exports: [RouterModule]
})
export class TicTacToePageRoutingModule { }
