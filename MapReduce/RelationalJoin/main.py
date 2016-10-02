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
            print item

class IntermediateValue:
    def __init__(self, name, departmentList):
        self.name = name
        self.departmentList = departmentList
        
mapReducer = MapReduce()

def mapper(record):
    record = record[:-1].split(",")
    if record[0] == "Department":
        if record[1] in mapReducer.intermediate:
            mapReducer.intermediate[record[1]].departmentList.append(record[2])
        else:
            mapReducer.intermediate[record[1]] = IntermediateValue(None, [record[2]])
    else:
        if record[2] in mapReducer.intermediate:
            mapReducer.intermediate[record[2]].name = record[1]
        else:
            mapReducer.intermediate[record[2]] = IntermediateValue(record[1], [])
    
def reducer(key, list_of_values):
    for department in list_of_values.departmentList:
        resultTuple = (key, list_of_values.name, department)
        mapReducer.emit(resultTuple)
            
if __name__ == '__main__':
    inputData = []
    for line in sys.stdin:
        inputData.append(line)
    mapReducer.execute(inputData, mapper, reducer)

