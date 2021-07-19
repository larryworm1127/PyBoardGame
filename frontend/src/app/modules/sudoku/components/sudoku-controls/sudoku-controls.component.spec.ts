import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SudokuControlsComponent } from './sudoku-controls.component';

describe('SudokuControlsComponent', () => {
  let component: SudokuControlsComponent;
  let fixture: ComponentFixture<SudokuControlsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SudokuControlsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SudokuControlsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
