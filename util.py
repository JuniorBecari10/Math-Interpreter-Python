def print_error(pos: int, msg: str):
  if pos != None:
    print(" " * 2, end="")
    print(" " * pos, end="")
    
    print("^")
  
  print(msg)