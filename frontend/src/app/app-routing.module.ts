import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./pages/home-page/home-page.module').then((m) => m.HomePageModule)
  },
  {
    path: 'ttt',
    loadChildren: () => import('./pages/tic-tac-toe-page/tic-tac-toe-page.module').then((m) => m.TicTacToePageModule)
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
