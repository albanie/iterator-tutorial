from math import factorial

class PascalIterator:
    def __init__(self, row):
        self.row = row
        self.column = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.column > self.row:
            raise StopIteration
        else:
            pascal_num = self.pascal_number(self.row, self.column)
            self.column += 1
            return pascal_num

    def pascal_number(self, row, column):
        numerator = factorial(row) 
        denominator = factorial(row - column) * factorial(column)
        pascal_num = int(numerator / denominator)
        return pascal_num