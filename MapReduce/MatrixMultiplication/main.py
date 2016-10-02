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
        self.result[value[0]][value[1]] = value[2] 

    def execute(self, matrix1, matrix2, mapper, reducer):
        n = len(matrix1)
        m = len(matrix2[0])
        for i in xrange(0,n):
            self.result.append([0]*m)
        
        mapper(matrix1, matrix2)

        for key in self.intermediate:
            reducer(key, self.intermediate[key])

        for i in xrange(0,n):
            row = ""
            for j in xrange(0,m):
                 row += str(self.result[i][j]) + " "
            print row

mapReducer = None

def mapper(matrix1, matrix2):
    for i in xrange(0, len(matrix1)):
        for j in xrange(0, len(matrix2[0])):
            for k in xrange(0, len(matrix1[i])):
                mapReducer.emitIntermediate(str(i)+ "," +str(j), matrix1[i][k] * matrix2[k][j])

def reducer(key, list_of_values):
    value = [ int(x) for x in key.split(",") ]
    value.append(sum(list_of_values))
    mapReducer.emit(value)
    
if __name__ == '__main__':
    testcases = int(sys.stdin.readline().strip())
    for t in xrange(0,testcases):
        mapReducer = MapReduce()
        matrix1 = []
        matrix2 = []

        # For matrix 1
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        for i in range(0, row):
            read_row = sys.stdin.readline().strip()
            matrix1.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix1[i].append(int(row_elems[j]))
        
        # For matrix 2
        dimensions = sys.stdin.readline().strip().split(" ")
        row = int(dimensions[0])
        column = int(dimensions[1])
        for i in range(0, row):
            read_row = sys.stdin.readline().strip()
            matrix2.append([])
            row_elems = read_row.strip().split()
            for j in range(0, len(row_elems)):
                matrix2[i].append(int(row_elems[j]))
        
        mapReducer.execute(matrix1, matrix2 , mapper, reducer)

