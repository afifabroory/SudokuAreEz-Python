def main():
  dimacs = open("dimacs.cnf")
  iteration = 1

  for line in dimacs:
    if iteration != 1:
      for char in line.split():
        if int(char) > 729:
          print(f"{iteration}:{char}")
          break
    iteration += 1

if __name__ == "__main__":
  main()
