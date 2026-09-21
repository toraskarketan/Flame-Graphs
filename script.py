import heapq
import math
import time
import argparse

# Hardcoded scale configuration to prevent quick exits
GRID_SIZE = 1000
ITERATIONS = 5

def euclidean_heuristic(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])

def get_neighbors(node):
    x, y = node
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            # Place procedural obstacles across the grid without blocking the goal
            if (nx * 3 + ny * 7) % 13 == 0 and (nx, ny) != (GRID_SIZE - 1, GRID_SIZE - 1):
                continue
            neighbors.append((nx, ny))
    return neighbors

def dijkstra_search(start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}
    nodes_expanded = 0

    while open_set:
        current_cost, current = heapq.heappop(open_set)
        nodes_expanded += 1

        if current == goal:
            return g_score[goal], nodes_expanded

        if current_cost > g_score.get(current, float('inf')):
            continue

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                heapq.heappush(open_set, (tentative_g, neighbor))

    return float('inf'), nodes_expanded

def astar_search(start, goal):
    open_set = []
    heapq.heappush(open_set, (euclidean_heuristic(start, goal), 0, start))
    g_score = {start: 0}
    nodes_expanded = 0

    while open_set:
        _, current_g, current = heapq.heappop(open_set)
        nodes_expanded += 1

        if current == goal:
            return g_score[goal], nodes_expanded

        if current_g > g_score.get(current, float('inf')):
            continue

        for neighbor in get_neighbors(current):
            tentative_g = g_score[current] + 1
            if tentative_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = tentative_g
                f_score = tentative_g + euclidean_heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    return float('inf'), nodes_expanded

def main():
    parser = argparse.ArgumentParser(description="Profile Dijkstra vs A* Search")
    parser.add_argument("--algo", choices=["dijkstra", "astar"], required=True)
    args = parser.parse_args()

    start_node = (0, 0)
    goal_node = (GRID_SIZE - 1, GRID_SIZE - 1)

    print(f"--- Running {args.algo.upper()} ---")
    print(f"Grid: {GRID_SIZE}x{GRID_SIZE} | Iterations: {ITERATIONS}")

    t_start = time.perf_counter()
    total_single_time = 0.0
    final_nodes = 0
    final_cost = 0

    for i in range(ITERATIONS):
        print(f"Executing Iteration {i + 1}/{ITERATIONS}...")
        t0 = time.perf_counter()
        
        if args.algo == "dijkstra":
            cost, nodes = dijkstra_search(start_node, goal_node)
        else:
            cost, nodes = astar_search(start_node, goal_node)
            
        t1 = time.perf_counter()
        
        total_single_time += (t1 - t0) * 1000
        final_nodes = nodes
        final_cost = cost

    t_end = time.perf_counter()
    total_run_duration = t_end - t_start

    print("\n--- RESULTS ---")
    print(f"Total Command Runtime: {total_run_duration:.2f} seconds")
    print(f"Avg Time per Run:     {total_single_time / ITERATIONS:.2f} ms")
    print(f"Nodes Expanded:       {final_nodes}")
    print(f"Path Cost:            {final_cost}")
    print("----------------\n")

if __name__ == "__main__":
    main()