def isSafe(board,row,col):
    for i in range (row):
        if(board[i] == col or abs(i-row) == abs(board[i] - col)):
            return False
    return True

def Backtracking(board,row,n,solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    for col in range(n):
        if isSafe(board,row,col):
            board[row] = col
            Backtracking(board,row + 1,n,solutions)

def BranchNBound(board,row,n,solutions):
    if row == n:
        solutions.append(board[:])
        return
    
    for col in range(n):
        if isSafe(board,row,col):
            board[row] = col
            BranchNBound(board,row + 1,n,solutions)
            board[row] = -1

def PrintSolution(solution):
    n = len(solution)
    for i in range(n):
        for j in range(n):
            if solution[i] == j:
                print("Q ",end="")
            else:
                print(". ",end="")
        print()
    print()


if __name__ == "__main__":
    n = int(input("Enter the number of queens: "))
    board = [-1] * n
    solutions = []
    print("Solutions using backtracking:")
    Backtracking(board, 0, n, solutions)
    for solution in solutions:
        PrintSolution(solution)
    
    solutions.clear()
    print("Solutions using branch and bound:")
    BranchNBound(board, 0, n, solutions)
    for solution in solutions:
        PrintSolution(solution)