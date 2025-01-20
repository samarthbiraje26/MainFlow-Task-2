import random

# Maze size (must be odd for better visual clarity)
WIDTH = 21
HEIGHT = 21

# Directions: up, down, left, right
DIRECTIONS = [(-2, 0), (2, 0), (0, -2), (0, 2)]

# Maze class for generating and solving mazes
class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maze = [[1] * width for _ in range(height)]  # Fill with walls
        self.generate_maze(1, 1)  # Start maze generation from (1, 1)

    def generate_maze(self, x, y):
        self.maze[y][x] = 0  # Carve path at (x, y)
        random.shuffle(DIRECTIONS)  # Randomize the direction order
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 1 <= nx < self.width - 1 and 1 <= ny < self.height - 1 and self.maze[ny][nx] == 1:
                if sum(self.maze[ny + dy2][nx + dx2] == 0 for dx2, dy2 in DIRECTIONS) < 2:
                    self.maze[ny][nx] = 0  # Carve a path
                    self.maze[y + dy // 2][x + dx // 2] = 0  # Carve a wall between the current cell and the new cell
                    self.generate_maze(nx, ny)  # Recursively generate the maze

    def print_maze(self):
        for row in self.maze:
            print(' '.join(str(cell) for cell in row))

    def solve(self, start, end, method="DFS"):
        if method == "DFS":
            return self.dfs(start, end)
        elif method == "BFS":
            return self.bfs(start, end)

    def dfs(self, start, end):
        stack = [start]
        visited = set()
        parent = {start: None}

        while stack:
            x, y = stack.pop()
            if (x, y) == end:
                return self.reconstruct_path(parent, end)
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (
                nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    stack.append((nx, ny))
        return None

    def bfs(self, start, end):
        queue = [start]
        visited = set()
        parent = {start: None}

        while queue:
            x, y = queue.pop(0)
            if (x, y) == end:
                return self.reconstruct_path(parent, end)
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.maze[ny][nx] == 0 and (
                nx, ny) not in visited:
                    visited.add((nx, ny))
                    parent[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
        return None

    def reconstruct_path(self, parent, end):
        path = []
        current = end
        while current:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        return path

# Main function to generate, solve, and display the maze
def main():
    maze = Maze(WIDTH, HEIGHT)

    print("Generated Maze:")
    maze.print_maze()

    start = (1, 1)
    end = (WIDTH - 2, HEIGHT - 2)

    print("\nSolving maze using DFS...")
    path = maze.solve(start, end, method="DFS")

    if path:
        print("\nPath found:")
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if (x, y) in path:
                    print('2', end=' ')  # Mark the path with '2'
                else:
                    print(maze.maze[y][x], end=' ')
            print()
    else:
        print("\nNo path found.")


if __name__ == "__main__":
    main()