from LineareGleichungssysteme import gleichungssystem
matrix = [[2,1,-1,1],
          [-3,-3,2,-1],
          [-2,0,3,-6],
          [-5,-3,2,-1]]
if __name__ == "__main__":
    new_gleichungssystem = gleichungssystem.Gleichungssystem(matrix)
    new_gleichungssystem.forme_in_Zeilenstufenform()

    new_gleichungssystem.print()