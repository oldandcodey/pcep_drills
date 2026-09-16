# Practicing a 3x3 Matrix as might be on the exam
# Bob Pelletier
#
board = [
    ['x','o','x'],
    ['o','x','x'],
    ['x','o','o']
]

# My Orignal Work
for i in range(3):
    if i == 0:
        print(" ", board[i][i])
    if i == 1:
        print("  ", board[i][i])
    if i == 2:
        print("   ",board[i][i])

# Grok Recommended
for i in range(3):
    print(" " * (i + 1), board[i][i])
