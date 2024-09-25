# DMOJ problem - coci19c5p1
# https://dmoj.ca/problem/coci19c5p1


def bfs(grid, visited, start_x, start_y):
    queue = [(start_x, start_y)]  # Используем обычный список
    visited[start_x][start_y] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        x, y = queue.pop(0)  # Удаляем первый элемент
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < len(grid) and 0 <= ny < len(grid[0])
                    and grid[nx][ny] == '*' and not visited[nx][ny]):
                visited[nx][ny] = True
                queue.append((nx, ny))  # Добавляем в конец


n, m = map(int, input().split())
grid_list = [list(input()) for _ in range(n)]

visited_list = [[False] * m for _ in range(n)]
rectangles = 0

for i in range(n):
    for j in range(m):
        if grid_list[i][j] == '*' and not visited_list[i][j]:
            bfs(grid_list, visited_list, i, j)
            rectangles += 1

# Вывод результата
print(rectangles)