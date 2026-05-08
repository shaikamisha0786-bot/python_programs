#expressions
# a,b=2,3
# c=4
# d=10.5
# e=a/b
# f=d//c
# txt="@"
# print(a*txt*b)
# print(a+b*c)
# print(c*d)
# print(a/b)
# print(f)

# a,b="2",3
# txt="@"
# print((a+txt)*b)





def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]

    def is_safe(r, c):
        for i in range(r):
            if board[i][c]:
                return False

        for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
            if board[i][j]:
                return False

        for i, j in zip(range(r - 1, -1, -1), range(c + 1, n)):
            if board[i][j]:
                return False

        return True

    def backtrack(r):
        if r == n:
            for row in board:
                print(" ".join("Q" if x else "." for x in row))
            print()
            return

        for c in range(n):
            if is_safe(r, c):
                board[r][c] = 1
                backtrack(r + 1)
                board[r][c] = 0

    backtrack(0)


solve_n_queens(8)
print("23E11A0550, Y.Bhanuteja")