def delete_copy( list_x ):
    dict_x = {}
    return [ dict_x.setdefault(x, x) for x in list_x if x not in dict_x ]

class Calculator:
  #empty constructor
  def __init__(self):
    pass
  #add method - given two numbers, return the addition
  def add(self, x1, x2):
    return x1 + x2
  #multiply method - given two numbers, return the 
  #multiplication of the two
  def multiply(self, x1, x2):
    return x1 * x2
  #subtract method - given two numbers, return the value
  #of first value minus the second
  def subtract(self, x1, x2):
    return x1 - x2
  #divide method - given two numbers, return the value
  #of first value divided by the second
  def divide(self, x1, x2):
    if x2 != 0:
      return x1/x2

if __name__ == "__main__":
    my_list = [ 1,1,1,1,1 ]

    new_list = delete_copy(my_list)
    print(new_list)