import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TicTacToeComponent } from './tic-tac-toe/tic-tac-toe.component';
import { TicTacToeSquareComponent } from './tic-tac-toe-square/tic-tac-toe-square.component';

@NgModule({
  declarations: [
    AppComponent,
    TicTacToeComponent,
    TicTacToeSquareComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
