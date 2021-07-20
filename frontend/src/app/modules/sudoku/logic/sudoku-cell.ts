export type SudokuNum = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9;

export class SudokuCell {

  constructor(
    public id: number,
    public isPencil: boolean = false,
    public value: SudokuNum | null = null,
    public isFixed: boolean = false,
    public isSelected: boolean = false,
    public hasError: boolean = false
  ) { }

  get properValue(): SudokuNum | null {
    return (this.isPencil) ? null : this.value;
  }
}
