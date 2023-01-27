class Sum:
  def __init__(self,list,target):
    self.list = list
    self.target = target
  
  def solution(self):
    self.length = len(self.list)
    
    for i in range(self.length - 1)
      for j in range(i + 1, self.lenght):
        if list[i] +list[j] == self.target
          new_list = i.j
          return list(new_list)
  return -1  
  
  
  
# Main Program 
list = [ int(val) for val in input("Enter list of values separated by space").split()]
target = int(input("Enter targer"))
ob = Sum(list,target)
print(ob.solution())
