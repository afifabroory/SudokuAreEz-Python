import sys
from math import sqrt, floor

def calculateClause(nCell):
    return nCell*nCell + (nCell*nCell * (nCell * (nCell - 1)/2)) * 3

def literal(row, col, val, n):
  return ((col*n)-(n-int(val))) + (n*(row-1)*n)

def toCNF(dimacs, preAssigned, nCell):
  
  # This this function implement Minimal Encoding.
  # Pre-assigned entry
  for e in preAssigned:
    x, y, z = e
    dimacs.write(f"{literal(x,y,z,nCell)} 0\n")

  # Definidness Entry
  for x in range(1, nCell+1):
    for y in range(1, nCell+1):
       for z in range(1, nCell+1):
         dimacs.write(f"{literal(x,y,z,nCell)} ")
       dimacs.write("0\n")

  # Uniqueness Row
  for y in range(1, nCell+1):
    for z in range(1, nCell+1):
      for x in range(1, nCell):
        for i in range(x+1, nCell+1):
          clause_1 = literal(x,y,z,nCell)
          clause_2 = literal(i,y,z,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")

  # Uniqueness Column
  for x in range(1, nCell+1):
    for z in range(1, nCell+1):
      for y in range(1, nCell):
        for i in range(y+1, nCell+1):
          clause_1 = literal(x,y,z,nCell)
          clause_2 = literal(x,i,z,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")

  # Uniqueness Block
  for z in range(1, nCell+1):
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
       for x in range(1, floor(sqrt(nCell))+1):
        for y in range(1, floor(sqrt(nCell))+1):
          for k in range(y+1, floor(sqrt(nCell))+1):
            clause_1 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+y,z,nCell)
            clause_2 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+k,z,nCell)
            dimacs.write(f"-{clause_1} -{clause_2} 0\n")
  for z in range(1, nCell+1):
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
        for x in range(1, floor(sqrt(nCell))+1):
          for y in range(1, floor(sqrt(nCell))+1):
            for k in range(x+1, floor(sqrt(nCell))+1):
              for l in range(1, floor(sqrt(nCell))+1):
                clause_1 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+y,z,nCell)
                clause_2 = literal(floor(sqrt(nCell))*i+k,floor(sqrt(nCell))*j+l,z,nCell)
                dimacs.write(f"-{clause_1} -{clause_2} 0\n")

def main(sudokuProblem, emptyEntry='x'):
  sudoku = open(sudokuProblem)
  dimacs = open("dimacs.cnf", "w+")
  
  nRow = 1
  nCell = 0
  preAssigned = []
  for line in sudoku:
    tmp = line.split()

    nCol = 1
    for cell in tmp:
      if cell != emptyEntry:
        preAssigned.append((nRow, nCol, cell))

      nCol += 1

    nCell += 1
    nRow += 1

  # DIMACS Header format
  # p cnf <total literal> <total clauses>
  dimacs.write(f"p cnf {nCell**3} {calculateClause(nCell)+len(preAssigned)}\n")
  toCNF(dimacs, preAssigned, nCell)
  dimacs.close()

if __name__ == "__main__":

  if len(sys.argv) > 1:
    for sudokuProblem in sys.argv[1:]:
      main(sudokuProblem)
  
  else:
    print("Please input your Sudoku problem file!\n" \
          "sudoku2dimacs.py <file 1> <file 2> ... <file n>")
