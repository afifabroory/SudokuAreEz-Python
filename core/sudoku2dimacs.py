import sys
import sudoku
from pathlib import Path

def calculateClause(nCell):
    return nCell*nCell + (nCell*nCell * (nCell * (nCell - 1)/2)) * 3

def main(sudokuProblem):
  
  sudokuFile = open(Path(sudokuProblem))
  dimacs = open(Path('sudoku/dimacs.cnf'), 'w+')
  
  nRow = 1
  nCell = 0
  preAssigned = []
  for line in sudokuFile:
    tmp = line.split()

    nCol = 1
    for cell in tmp:
      if cell != 'x':
        preAssigned.append((nRow, nCol, cell))
      nCol += 1
    nCell += 1
    nRow += 1
  
  sudokuFile.close()
  
  # DIMACS Header format
  # p cnf <total literal> <total clauses>
  dimacs.write(f'p cnf {nCell**3} {calculateClause(nCell)+len(preAssigned)}\n')
  sudoku.toCNF(dimacs, preAssigned, nCell)
  dimacs.close()

if __name__ == '__main__':

  if len(sys.argv) > 1:
    for sudokuProblem in sys.argv[1:]:
      main(sudokuProblem)
  
  else:
    print('Please input your Sudoku problem file!\nsudoku2dimacs.py <file 1> <file 2> ... <file n>\nI Recommend you to run solve.sh')
