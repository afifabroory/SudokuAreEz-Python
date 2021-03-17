import sys
from math import sqrt, floor

def calculateClause(nCell):
    # Cell
    CellD = nCell*nCell
    CellSum = 0
    for i in range(1, nCell):
      CellSum += nCell - i
    CellU = nCell*nCell*CellSum
    print(f"CellU = {CellU}")

    # Row
    RowD = nCell*nCell
    RowSum = 0
    for i in range(1, nCell):
      RowSum += nCell - i
    RowU = nCell*nCell * RowSum
    print(f"RowU = {RowU}")

    # Column
    ColD = nCell*nCell
    ColSum = 0
    for i in range(1, nCell):
      ColSum += nCell - i
    ColU = nCell*nCell * ColSum
    print(f"ColU = {ColU}")

    # Block
    BlockD = sqrt(nCell)*sqrt(nCell)*nCell
    BlockSum = 0
    for i in range(1, nCell+1):
      BlockSum += nCell - i
    BlockU = int(sqrt(nCell)*sqrt(nCell))*nCell * BlockSum
    print(f"BlockU = {BlockU}")

    return int(CellD + CellU + RowD + RowU + ColD + ColU + BlockD + BlockU)

def literal(row, col, val, n):
  return int(row*n**2 - n**2 + col*n + int(val) - n)

def toCNF(dimacs, preAssigned, nCell):
  
  # Pre-assigned entry
  for e in preAssigned: # Conjunction
    r, c, v = e
    dimacs.write(f"{literal(r,c,v,nCell)} 0\n")

  # Definidness Entry
  for r in range(1, nCell+1): # Conjunction
    for c in range(1, nCell+1):
       for v in range(1, nCell+1): # Disjunction
         dimacs.write(f"{literal(r,c,v,nCell)} ")
       dimacs.write("0\n")

  # Uniqueness Entry
  for r in range(1, nCell+1): # Conjunction
    for c in range(1, nCell+1):
      for vi in range(1, nCell):
        for vj in range(vi+1, nCell+1):
          clause_1 = literal(r,c,vi,nCell)
          clause_2 = literal(r,c,vj,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")

  # Definidness Row
  for c in range(1, nCell+1): # Conjunction
    for v in range(1, nCell+1):
      for r in range(1, nCell+1): # Disjunction
        dimacs.write(f"{literal(r,c,v,nCell)} ")
      dimacs.write("0\n")

  # Uniqueness Row
  for c in range(1, nCell+1): # Conjunction
    for v in range(1, nCell+1):
      for ri in range(1, nCell):
        for rj in range(ri+1, nCell+1):
          clause_1 = literal(ri,c,v,nCell)
          clause_2 = literal(rj,c,v,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")

  # Definidness Column
  for r in range(1, nCell+1): # Conjunction
    for v in range(1, nCell+1):
      for c in range(1, nCell+1): # Disjunction
        dimacs.write(f"{literal(r,c,v,nCell)} ")
      dimacs.write("0\n")
 
  # Uniqueness Column
  for r in range(1, nCell+1): # Conjunction
    for v in range(1, nCell+1):
      for ci in range(1, nCell):
        for cj in range(ci+1, nCell+1):
          clause_1 = literal(r,ci,v,nCell)
          clause_2 = literal(r,cj,v,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")

  # Definidness Block
  for v in range(1, nCell+1): # Disjunction
    for i in range(floor(sqrt(nCell))): # Conjunction
      for j in range(floor(sqrt(nCell))):
        for r in range(1, floor(sqrt(nCell))+1):
          for c in range(1, floor(sqrt(nCell))+1):
            dimacs.write(f"{literal(floor(sqrt(nCell)*i+r),floor(sqrt(nCell))*j+c,v,nCell)} ")
  dimacs.write("0\n")
    #dimacs.write("0\n") # THIS IS WIERD!
 
  # Uniqueness Block
  for v in range(1, nCell+1): # Conjunction
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
       for r in range(1, floor(sqrt(nCell))+1):
        for ci in range(1, floor(sqrt(nCell))+1):
          for cj in range(ci+1, floor(sqrt(nCell))+1):
            clause_1 = literal(floor(sqrt(nCell))*i+r,floor(sqrt(nCell))*j+ci,v,nCell)
            clause_2 = literal(floor(sqrt(nCell))*i+r,floor(sqrt(nCell))*j+cj,v,nCell)
            dimacs.write(f"-{clause_1} -{clause_2} 0\n")
  for v in range(1, nCell+1): # Conjunction
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
        for ri in range(1, floor(sqrt(nCell))+1):
          for c in range(1, floor(sqrt(nCell))+1):
            for rj in range(ci+1, floor(sqrt(nCell))+1):
              for k in range(1, floor(sqrt(nCell))+1):
                clause_1 = literal(floor(sqrt(nCell))*i+ri,floor(sqrt(nCell))*j+c,v,nCell)
                clause_2 = literal(floor(sqrt(nCell))*i+rj,floor(sqrt(nCell))*j+k,v,nCell)
                dimacs.write(f"-{clause_1} -{clause_2} 0\n")


def main(sudokuProblem, emptyEntry='x'):
  sudoku = open(sudokuProblem)
  dimacs = open("dimacs.cnf", "w+")
  
  nRow = 1
  nCell = 0
  preAssigned = []
  for line in sudoku:
    tmp = line.split()
    print(tmp) # DEBUG: splitted char in input file

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
