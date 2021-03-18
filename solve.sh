if [[ $# -gt 0 ]] 
then

  for arg in $@
  do

    if [[ -e "$arg" ]] 
    then
      echo 
      python3 core/sudoku2dimacs.py "$arg"
      ./core/tools/MiniSat sudoku/dimacs.cnf sudoku/solution.cnf
      python3 core/show_solution.py
    else 
      printf "\033[0;31m$arg are 'ghaib' (not exists)\033[0m\n"
      echo "Please input correct file!"
      echo "Example: ./Solve.sh <file_1> <file_2> ... <file_n>"
      exit 1
    fi

  done

  exit 0

else
  printf "\033[0;31mPlease input your sudoku problem file!\033[0m\n"
  echo "Example: ./Solve.sh <file_1> <file_2> ... <file_n>"
  exit 1
fi

