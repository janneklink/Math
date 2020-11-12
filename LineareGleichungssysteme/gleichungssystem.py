class Gleichungssystem:

    def __init__(self, matrix):
        self.matrix=matrix
        self.lines = len(matrix)
        self.spalten = len(matrix[0])

    def multipliziere(self, line_i, factor):
        for spalte in range(0, self.spalten):
            self.matrix[line_i][spalte]*=factor


    def addiere(self,line_i, line_j, factor=1):
        for spalte in range(0, self.spalten):
            self.matrix[line_i][spalte] += self.matrix[line_j][spalte]*factor


    def vertausche(self, line_i, line_j):
        self.addiere(line_j,line_i)
        self.addiere(line_i,line_j,-1)
        self.addiere(line_j, line_i)
        self.multipliziere(line_i,-1)


    def forme_in_Zeilenstufenform(self):
        self.sortiere_nach_pivoten()
        for spalte_j in range (0, self.spalten):
            self.setze_spalte_null(spalte_j,spalte_j)


    def setze_spalte_null(self,pivot_line, pivot_spalte):
        pivot = self.matrix[pivot_line][pivot_spalte]
        self.multipliziere_alle(pivot_line+1,pivot)
        for line_i in range(pivot_line+1,self.lines):
            erstes_element_line_i = self.matrix[line_i][pivot_spalte]
            self.addiere(line_i,pivot_line,-erstes_element_line_i/pivot)

    def sortiere_nach_pivoten(self):
        pass

    def print(self):
        distance = 4
        for line_i in self.matrix:
            line = ""
            for element_j_i in line_i:
                string_element_j = str(int(element_j_i))
                line+= str(string_element_j)
                line+= " "*(distance-len(string_element_j))
            print (line)

    def multipliziere_alle(self, first_line, factor):
        for line_i in range(first_line,self.lines):
            self.multipliziere(line_i, factor)



