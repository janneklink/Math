from LineareGleichungssysteme import gleichungssystem
matrix = [[3,2,-2],[2,1,-3],[-2,-1, 1]]
if __name__ == "__main__":
    new_gleichungssystem = gleichungssystem.Gleichungssystem(matrix)
    new_gleichungssystem.print()
    print("")
    new_gleichungssystem.vertausche(1,2)
    new_gleichungssystem.print()