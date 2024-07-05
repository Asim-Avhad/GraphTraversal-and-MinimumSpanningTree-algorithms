import heapq

class PuzzleNode:
    def __init__(self, state, goal, parent=None, move=0, depth=0):
        self.state = state
        self.goal = goal
        self.parent = parent
        self.move = move
        self.depth = depth

    def __lt__(self, other):
        return (self.depth + self.heuristic()) < (other.depth + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __str__(self):
        return str(self.state)

    def heuristic(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != self.goal[i][j]:
                    count += 1
        return count
    
    def get_neighbors(self):
        neighbors = []
        i, j = self.find_blank()
        for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < 3 and 0 <= y < 3:
                neighbor_state = [row[:] for row in self.state]
                neighbor_state[i][j], neighbor_state[x][y] = neighbor_state[x][y], neighbor_state[i][j]
                neighbors.append(PuzzleNode(neighbor_state, self.goal, parent=self, move=neighbor_state[x][y], depth=self.depth+1))
        return neighbors

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node = node.parent
    return path[::-1]

def astar(start_state, goal_state):
    start_node = PuzzleNode(start_state, goal_state)
    frontier = []
    heapq.heappush(frontier, start_node)
    frontier_set = {tuple(map(tuple, start_node.state)): start_node}
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)
        if node.state == goal_state:
            return reconstruct_path(node)
        explored.add(node)
        for neighbor in node.get_neighbors():
            neighbor_state_tuple = tuple(map(tuple, neighbor.state))
            if neighbor_state_tuple not in explored:
                if neighbor_state_tuple not in frontier_set or neighbor < frontier_set[neighbor_state_tuple]:
                    heapq.heappush(frontier, neighbor)
                    frontier_set[neighbor_state_tuple] = neighbor
    return None

def print_solution(path):
    for i, node in enumerate(path):
        print(f"Step {i}:")
        for row in node.state:
            print(row)
        print()

def get_user_input():
    print("Enter the start state of the puzzle (use 0 for the blank tile):")
    start_state = []
    for i in range(3):
        row = input(f"Enter row {i+1} separated by spaces: ").strip().split()
        start_state.append([int(x) for x in row])
    print("Enter the goal state of the puzzle (use 0 for the blank tile):")
    goal_state = []
    for i in range(3):
        row = input(f"Enter row {i+1} separated by spaces: ").strip().split()
        goal_state.append([int(x) for x in row])
    return start_state, goal_state

if __name__ == "__main__":
    start_state, goal_state = get_user_input()
    path = astar(start_state, goal_state)
    if path:
        print("Solution found!")
        print_solution(path)
    else:
        print("No solution found.")