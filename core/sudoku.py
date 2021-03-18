from math import sqrt, floor

def literal(row, col, val, n):
  return ((col*n)-(n-int(val))) + (n*(row-1)*n)

def toCNF(dimacs, preAssigned, nCell):
  
  # This function implement Minimal Encoding.
  # Pre-assigned Entry/Cell
  for e in preAssigned:
    x, y, z = e
    dimacs.write(f'{literal(x,y,z,nCell)} 0\n')

  # Definedness Entry/Cell
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

  # Implement Extended Encoding
  # Uniqueness Entry
  for x in range(1, nCell+1):
    for y in range(1,nCell+1):
      for z in range(1,nCell):
        for i in range(z+1,nCell+1):
          clause_1 = literal(x,y,z,nCell)
          clause_2 = literal(x,y,i,nCell)
          dimacs.write(f"-{clause_1} -{clause_2} 0\n")
  
  # Definedness Row
  for x in range(1,nCell+1):
    for v in range(1, nCell+1):
      for y in range(1,nCell+1):
        dimacs.write(f"{literal(x,y,v,nCell)} ")
      dimacs.write("0\n")
         
  # Definedness Column
  for y in range(1,nCell+1):
    for v in range(1,nCell+1):
      for x in range(1,nCell+1):
        dimacs.write(f'{literal(x,y,v,nCell)} ')
      dimacs.write("0\n")
         
  # Definedness Block
  for i in range(floor(sqrt(nCell))):
    for j in range(floor(sqrt(nCell))):
      for v in range(1,nCell+1):
        for x in range(1,floor(sqrt(nCell))+1):
          for y in range(1,floor(sqrt(nCell))+1):
            clause = literal(i*floor(sqrt(nCell))+x,j*floor(sqrt(nCell))+y,v,nCell)
            dimacs.write(f'{clause} ')
        dimacs.write('0\n')
            
