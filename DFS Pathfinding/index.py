def solve_maze(maze, x, y):
    if x < 0 or x >= 5 or y < 0 or y >= 5 or maze[y][x] == '#' or maze[y][x] == '+':
        return False

    if maze[y][x] == 'E':
        return True

    maze[y][x] = '+'

   
    if solve_maze(maze, x, y - 1) or solve_maze(maze, x, y + 1) or solve_maze(maze, x - 1, y) or solve_maze(maze, x + 1, y):
        return True

    maze[y][x] = '.'  # Mark as visited, but not part of the solution path
    return False


maze = [
    ['S', '.', '#', '.', '.'],
    ['.', '#', '.', '#', '#'],
    ['.', '.', '.', '.', '.'],
    ['#', '#', '.', '#', '#'],
    ['.', '.', '.', '.', 'E']
]

for y in range(5):  # Find the start position
    for x in range(5):
        if maze[y][x] == 'S':
            start_x, start_y = x, y

if solve_maze(maze, start_x, start_y):
    print("Solution found:")
    for row in maze:
        print(''.join(row))
else:
    print("No solution found.")