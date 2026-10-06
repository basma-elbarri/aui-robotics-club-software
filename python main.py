from collections import deque
import random

class ArenaPathPlanner:

    def __init__(self, size=5):
        self.size = size
        self.start = (0, 0)  # (0,0)
        self.point_a = (round((size-1)/2), round((size-1)/2))
        self.point_b = (size-1, size-1)

    def find_path(self, start, goal, obstacles):

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
                # Check grid boundaries, obstacles, and visited states
                if 0 <= nr < self.size and 0 <= nc < self.size and nxt not in obstacles and nxt not in visited:
                    visited.add(nxt)
                    new_path = list(path)
                    new_path.append(nxt)
                    queue.append(new_path)

        return None

    def print_grid(self, obstacles, path=[]):

        print("-" * 17)
        for r in range(self.size):
            row_str = "|"
            for c in range(self.size):
                pos = (r, c)
                if pos == self.start:
                    char = "S "
                elif pos == self.point_a:
                    char = "A "
                elif pos == self.point_b:
                    char = "B "
                elif pos in obstacles:
                    char = "X "
                elif pos in path:
                    char = ". "
                else:
                    char = "  "
                row_str += char + "|"
            print(row_str)
        print("-" * 17)

    def run_mission(self, obstacles):

        print("--- Start to Point A  ---")
        leg1 = self.find_path(self.start, self.point_a, obstacles)

        if not leg1:
            print("Goal Unreachable: Cannot reach Point A! Path is blocked.")
            self.print_grid(obstacles)
            return False

        print(f"Path to Point A: {leg1}")

        print("\n--- Point A to Point B  ---")
        # Note: Point A is treated as start for the second leg
        leg2 = self.find_path(self.point_a, self.point_b, obstacles)

        if not leg2:
            print("Goal Unreachable: Cannot reach Point B from Point A! Path is blocked.")
            self.print_grid(obstacles)
            return False

        print(f"Path to Point B: {leg2}")


        full_path = leg1 + leg2[1:]
        print("\nFull Mission Path Visualization (S=Start, A=Point A, B=Point B, .=Path, X=Obstacle):")
        self.print_grid(obstacles, full_path)
        return True



if __name__ == "__main__":



        while True:
            print("\n========================================")
            print(" AUI Robotics - Track A (by Basma El Barri)")
            print("==========================================")
            size_input = input("Enter grid size >= 3 (press Enter for the default 5x5 grid): ").strip()
            grid_size = int(size_input) if size_input.isdigit() and int(size_input) >= 3 else 5

            planner = ArenaPathPlanner(size=grid_size)

            print("1. Run Successful Layout")
            print("2. Run Blocked Layout")
            print("3. Run Randomized Layout")
            print("4. Exit")

            choice = input("\nSelect an option (1-4): ").strip()

            if choice == "1":
                print("\n=== TEST: SUCCESSFUL LAYOUT ===")
                normal_obstacles = [(1, 2), (2, 1), (3, 2)]
                planner.run_mission(normal_obstacles)

            elif choice == "2":
                ax, ay = planner.point_a
                print("\n=== TEST: BLOCKED LAYOUT ===")
                blocked_obstacles = [(ax -1, ay), (ax + 1, ay), (ax, ay - 1 ), (ax, ay + 1)]
                planner.run_mission(blocked_obstacles)

            elif choice == "3":
                print("\n=== TEST: RANDOMIZED LAYOUT ===")
                all_cells = [(r, c) for r in range(planner.size) for c in range(planner.size)]
                reserved = {planner.start, planner.point_a, planner.point_b}
                available_cells = [cell for cell in all_cells if cell not in reserved]


                num_obstacles = random.randint(3, 8)
                random_obstacles = random.sample(available_cells, num_obstacles)

                print(f"Generated Obstacles: {random_obstacles}")
                planner.run_mission(random_obstacles)

            elif choice == "4":
                print("\nExiting simulator.")
                break
            else:
                print("\nInvalid input. Please enter a number between 1 and 4.")