class Gleichungssystem:

    def __init__(self, matrix):
        self.matrix=matrix
        self.m = len(matrix)
        self.n = len(matrix[0])

    def multipliziere(self, line_i, factor):
        for element_j in range(0, self.n):
            self.matrix[line_i][element_j]*=factor


    def addiere(self,line_i, line_j, factor=1):
        for element_j in range(0, self.n):
            self.matrix[line_i][element_j] += self.matrix[line_j][element_j]*factor


    def vertausche(self, line_i, line_j):
        self.addiere(line_j,line_i)
        self.addiere(line_i,line_j,-1)
        self.addiere(line_j, line_i)
        self.multipliziere(line_i,-1)


    def forme_in_Zeilenstufenform(self):
        pass

    def print(self):
        distance = 4
        for line_i in self.matrix:
            line = ""
            for element_j in line_i:
                string_element_j = str(element_j)
                line+= str(string_element_j)
                line+= " "*(distance-len(string_element_j))
            print (line)

