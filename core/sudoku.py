from math import sqrt, floor

def literal(row, col, val, n):
  return ((col*n)-(n-int(val))) + (n*(row-1)*n)

def toCNF(dimacs, preAssigned, nCell):
  
  # This this function implement Minimal Encoding.
  # Pre-assigned entry
  for e in preAssigned:
    x, y, z = e
    dimacs.write(f'{literal(x,y,z,nCell)} 0\n')

  # Definidness Entry
  for x in range(1, nCell+1):
    for y in range(1, nCell+1):
       for z in range(1, nCell+1):
         dimacs.write(f'{literal(x,y,z,nCell)} ')
       dimacs.write('0\n')

  # Uniqueness Row
  for y in range(1, nCell+1):
    for z in range(1, nCell+1):
      for x in range(1, nCell):
        for i in range(x+1, nCell+1):
          clause_1 = literal(x,y,z,nCell)
          clause_2 = literal(i,y,z,nCell)
          dimacs.write(f'-{clause_1} -{clause_2} 0\n')

  # Uniqueness Column
  for x in range(1, nCell+1):
    for z in range(1, nCell+1):
      for y in range(1, nCell):
        for i in range(y+1, nCell+1):
          clause_1 = literal(x,y,z,nCell)
          clause_2 = literal(x,i,z,nCell)
          dimacs.write(f'-{clause_1} -{clause_2} 0\n')

  # Uniqueness Block
  for z in range(1, nCell+1):
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
       for x in range(1, floor(sqrt(nCell))+1):
        for y in range(1, floor(sqrt(nCell))+1):
          for k in range(y+1, floor(sqrt(nCell))+1):
            clause_1 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+y,z,nCell)
            clause_2 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+k,z,nCell)
            dimacs.write(f'-{clause_1} -{clause_2} 0\n')
  for z in range(1, nCell+1):
    for i in range(floor(sqrt(nCell))):
      for j in range(floor(sqrt(nCell))):
        for x in range(1, floor(sqrt(nCell))+1):
          for y in range(1, floor(sqrt(nCell))+1):
            for k in range(x+1, floor(sqrt(nCell))+1):
              for l in range(1, floor(sqrt(nCell))+1):
                clause_1 = literal(floor(sqrt(nCell))*i+x,floor(sqrt(nCell))*j+y,z,nCell)
                clause_2 = literal(floor(sqrt(nCell))*i+k,floor(sqrt(nCell))*j+l,z,nCell)
                dimacs.write(f'-{clause_1} -{clause_2} 0\n')
