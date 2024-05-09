#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
// Function to check if placing a queen at position (row, col) is safe
bool isSafe(const vector<int> &board, int row, int col)
{
    // Check if there is a queen in the same column
    for (int i = 0; i < row; ++i)
    {
        if (board[i] == col || abs(i - row) == abs(board[i] - col))
        {
            return false;
        }
    }
    return true;
}
// Function to solve N-Queens problem using backtracking
void solveNQueensBacktracking(vector<int> &board, int row, int n, vector<vector<int>> &solutions)
{
    if (row == n)
    {
        // If all queens are placed, add the solution to the list of solutions
        solutions.push_back(board);
        return;
    }
    for (int col = 0; col < n; ++col)
    {
        if (isSafe(board, row, col))
        {
            board[row] = col;
            solveNQueensBacktracking(board, row + 1, n, solutions);
        }
    }
}
// Function to solve N-Queens problem using branch and bound
void solveNQueensBranchAndBound(vector<int> &board, int row, int n, vector<vector<int>> &solutions)
{
    if (row == n)
    {
        // If all queens are placed, add the solution to the list of solutions
        solutions.push_back(board);
        return;
    }
    for (int col = 0; col < n; ++col)
    {
        if (isSafe(board, row, col))
        {
            board[row] = col;
            solveNQueensBranchAndBound(board, row + 1, n, solutions);
            // Reset the board after exploring this branch
            board[row] = -1;
        }
    }
}
// Function to print a solution
void printSolution(const vector<int> &solution)
{
    int n = solution.size();
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (solution[i] == j)
            {
                cout << "Q ";
            }
            else
            {
                cout << ". ";
            }
        }
        cout << endl;
    }
    cout << endl;
}
int main()
{
    int n;
    cout << "Enter the number of queens: ";
    cin >> n;
    vector<int> board(n, -1); // Initialize the board with no queens placed
    vector<vector<int>> solutions;
    cout << "Solutions using backtracking:\n";
    solveNQueensBacktracking(board, 0, n, solutions);
    for (const auto &solution : solutions)
    {
        printSolution(solution);
    }
    solutions.clear(); // Clear the solutions for the next algorithm
    cout << "Solutions using branch and bound:\n";
    solveNQueensBranchAndBound(board, 0, n, solutions);
    for (const auto &solution : solutions)
    {
        printSolution(solution);
    }
    return 0;
}