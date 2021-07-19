import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SudokuRightPanelComponent } from './sudoku-right-panel.component';

describe('SudokuRightPanelComponent', () => {
  let component: SudokuRightPanelComponent;
  let fixture: ComponentFixture<SudokuRightPanelComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SudokuRightPanelComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SudokuRightPanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
