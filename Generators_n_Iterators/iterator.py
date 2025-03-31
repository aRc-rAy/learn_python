class myIterator:
      def __init__(self,_start,_end):
            self.start=_start
            self.end=_end
      
      def __iter__(self):
            return self
      
      def __next__(self):
            if self.start<=self.end:
                  self.start+=1
                  return self.start
            else:
                  raise StopIteration
      

myItr=myIterator(1,5)


for val in myItr:
      print(f"val is : {val}")
else:
      print("Iteration is completed")