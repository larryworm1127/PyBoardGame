import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TicTacToeBoardComponent } from './tic-tac-toe-board.component';

describe('TicTacToeComponent', () => {
  let component: TicTacToeBoardComponent;
  let fixture: ComponentFixture<TicTacToeBoardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TicTacToeBoardComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TicTacToeBoardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
