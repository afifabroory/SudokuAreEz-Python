from math import ceil

def literal(row,col,val,n):
    return str((col*n)-(n-int(val)) + (n*(row-1)*n))

def main():
  SAT = open('solution.cnf')
  sudokuSAT = SAT.read().split()
  SAT.close()
   
  ROW_COLUMN = ceil((len(sudokuSAT))**(1/3))-1 # Calculate size N of ROW/COLUMN
  
  if sudokuSAT[0] == 'SAT':
    print("\nSOLUTION")
    row = 1
    col = 0
    output = ''
    for row in range(1, ROW_COLUMN+1):
      for column in range(1, ROW_COLUMN+1):
        for value in range(1, ROW_COLUMN+1): 
          if literal(row,column,value,ROW_COLUMN) in sudokuSAT:
            output += str(value) + " "
      output += '\n'
    print(output) 
  else:
    print('No Solution found.')

if __name__ == '__main__':
  main()
