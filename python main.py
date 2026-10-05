from collections import deque
grid_size = 5
obstacles = []
start = (0, 0)
point_a = (2, 2)
point_b = (4, 4)

print(point_a)
print(point_b)
def find_path(start, goal, obstacles):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:

            return path


        r, c = current
        neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

        for nxt in neighbors:
            nr, nc = nxt

            if 0 <= nr < 5 and 0 <= nc < 5 and nxt not in obstacles and nxt not in visited:
                visited.add(nxt)
                new_path = list(path)
                new_path.append(nxt)
                queue.append(new_path)


    return None




