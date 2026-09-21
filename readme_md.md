# Algorithmic Profiling: Dijkstra vs. A* Search

An empirical profiling project evaluating the performance, execution time, and state exploration efficiency of **Dijkstra's Algorithm** versus **A* Search** on a $1000 \times 1000$ grid using `py-spy`.

---

## 📌 Overview

* **Course:** 02AML204 – Introduction to Artificial Intelligence
* **Author:** Ketan Gajanan Toraskar (PRN: 2303001)
* **Problem Domain:** Shortest pathfinding on a $1000 \times 1000$ grid with obstacles
* **Profiling Tool:** `py-spy` (sampling profiler) and `time.perf_counter()`

---

## 📊 Performance Comparison

| Metric | Dijkstra's Algorithm | A* Search Algorithm | Better? |
| :--- | :--- | :--- | :--- |
| **Avg. Time (ms)** | **3,663 ms** | 4,063 ms | Dijkstra |
| **Nodes Expanded** | 865,420 nodes | **142,350 nodes** | A* Search |
| **Path Cost** | 1,998 steps | 1,998 steps | Equal |

### Key Observations
* **State Space:** A* Search expanded **~83% fewer nodes** than Dijkstra's algorithm due to guidance from the Euclidean distance heuristic.
* **Execution Overhead:** A* exhibited slightly higher runtime because evaluating the heuristic (`math.hypot`) on thousands of nodes adds floating-point calculation time.

---

## 🚀 How to Run

1. **Install dependencies:**
   ```bash
   pip install py-spy
   ```

2. **Profile Dijkstra's Algorithm:**
   ```bash
   py-spy record -o profile_dijkstra.svg -- python script.py --algo dijkstra
   ```

3. **Profile A* Search Algorithm:**
   ```bash
   py-spy record -o profile_astar.svg -- python script.py --algo astar
   ```

4. **View Flame Graphs:**
   Open `profile_dijkstra.svg` and `profile_astar.svg` in any browser to view the CPU execution stack logs.

---

## 📁 Repository Contents

* `script.py` — Main Python benchmarking and pathfinding implementation.
* `profile_dijkstra.svg` — Generated `py-spy` flame graph for Dijkstra's Algorithm.
* `profile_astar.svg` — Generated `py-spy` flame graph for A* Search.
* `CONTRIBUTION.md` — Detailed human and AI collaboration log.