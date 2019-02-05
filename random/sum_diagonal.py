"""
Given a square matrix of size , calculate the absolute difference between the
sums of its diagonals.

Input Format

The first line contains a single integer, . The next  lines denote the matrix's
rows, with each line containing space-separated integers describing the
columns.

Output Format

Print the absolute difference between the two sums of the matrix's diagonals as
a single integer.
"""
import random


def generate_matrix(n):
    matrix = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = random.randint(-100, 100)
    print(matrix)
    return matrix


def sum_diagonals(matrix):
    for row in matrix:
        top = m.pop(0)
        bot = 
    top = m.pop(0)
    bot = m.pop()
    sum = top[0] + top[-1] + bot[0] + bot[-1]


def main():
    n = int(input('Matrix dimension: '))
    matrix = generate_matrix(n)
    solution = sum_diagonals(matrix)


if __name__ == '__main__':
    main()
