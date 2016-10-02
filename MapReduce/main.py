######################################################################################################
########################################### ALGORITHM ################################################
######################################################################################################
# 1. On computing the the first few rows of the triangle , we notice a pattern that the first even
#    number is at the position 2, 3, 2, 4, 2, 3, 2, 4, 2, 3, 2, 4..... (starting from row 3). 
#    So basically the position of the first even number repeats after an interval of 4 in the above fashion.
# 2. Use this property to quickly and efficiently find the answer.
######################################################################################################
import sys
from collections import OrderedDict
class MapReduce:
    def __init__(self):
        self.intermediate = OrderedDict()
        self.result = []
   

    def emitIntermediate(self, key, value):
      self.intermediate.setdefault(key, [])       
      self.intermediate[key].append(value)

    def emit(self, value):
        self.result.append(value) 

    def execute(self, data, mapper, reducer):
        for record in data:
            mapper(record)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        self.result.sort()
        for item in self.result:
            print "{\"key\":\""+item[0]+"\",\"value\":\"" + str(item[1]) + "\"}"

mapReducer = MapReduce()

def mapper(record):
    record = record.split()
    if record[0] in mapReducer.intermediate:
        mapReducer.intermediate[record[0]].append(record[1])
    else:
        mapReducer.intermediate[record[0]] = [record[1]]

    if record[1] in mapReducer.intermediate:
        mapReducer.intermediate[record[1]].append(record[0])
    else:
        mapReducer.intermediate[record[1]] = [record[0]]

def reducer(key, list_of_values):
    mapReducer.result.append([key, len(list_of_values)])
    
if __name__ == '__main__':
  inputData = []
  for line in sys.stdin:
   inputData.append(line)
  mapReducer.execute(inputData, mapper, reducer)

