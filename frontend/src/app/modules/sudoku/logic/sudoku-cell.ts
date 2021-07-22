export class SudokuCell {

  constructor(
    public id: number,
    public value: number | null = null,
    public isFixed: boolean = false,
    public isPencil: boolean = false,
    public isSelected: boolean = false,
    public hasError: boolean = false
  ) { }

  get properValue(): number | null {
    return (this.isPencil) ? null : this.value;
  }
}
