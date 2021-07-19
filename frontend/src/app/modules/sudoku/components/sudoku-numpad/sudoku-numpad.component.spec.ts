import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SudokuNumpadComponent } from './sudoku-numpad.component';

describe('SudokuNumpadComponent', () => {
  let component: SudokuNumpadComponent;
  let fixture: ComponentFixture<SudokuNumpadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SudokuNumpadComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SudokuNumpadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
