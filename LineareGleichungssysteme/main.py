from LineareGleichungssysteme import gleichungssystem
import numpy as np

# matrix = ([1, 1, 1],[0, 1, -1],[-1, 2, 3],)

if __name__ == "__main__":
    A1 = np.matrix([[-1, 0, 0, -1, -1],
                    [0, -1, 2, 0, -3],
                    [0, -2, -2, -3, 0],
                    [1, 1, 2, 3, 0],
                    [0, -1, -2, -2, 1]])
    A2 = A1 * A1
    A3 = A1 * A2

    B1 = np.matrix([[1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, -1, 1],
                    [-1, -1, 1, 1, -1, 1],
                    [0, 0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 2, 0],
                    [0, 0, 0, 0, 0, 1]])
    diag1 = np.matrix([[1, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 0, 1]])

    print("Eigenwerte: ", np.linalg.eigvals(B1))
    print("(B1-Id6):\n", (B1 - diag1))
    print("(B1-Id6)²:\n", (B1 - diag1) * (B1 - diag1))
    print("(B1-Id6)³:\n", (B1 - diag1) * (B1 - diag1) * (B1 - diag1))
    print("A¹:\n", A1)
    print("A²:\n", A2)
    print("A³:\n", A3)

# new_gleichungssystem = gleichungssystem.Gleichungssystem(matrix)
# new_gleichungssystem.forme_in_Zeilenstufenform()
# print("Lösung des Gleichungssystem:")
# new_gleichungssystem.print()
