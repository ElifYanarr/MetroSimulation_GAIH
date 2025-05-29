# MetroSimulation_GAIH

A simulation project that finds the **fastest** and **least-transfer** routes within a specific metro network.

## Technologies & Libraries Used

- **Python (VSCode)**  
- **Collections Module**  
  - `deque`: A double-ended queue used in the Breadth-First Search (BFS) algorithm to manage station exploration efficiently.
  - `defaultdict`: Automatically creates default values for keys, enabling easy mapping between lines and stations.
- **Heapq Module**  
  - Provides a priority queue implementation using a heap. Used in the A* algorithm to prioritize the lowest-cost paths.
- **Typing Module**  
  - Improves code readability and safety through type hints (`List`, `Dict`, `Set`, `Tuple`, `Optional`, etc.).

## Algorithm Logic

### Breadth-First Search (BFS)
- Finds the route with the **least number of transfers**.
- Uses a **queue** to explore the graph level by level from the source to the destination station.

### A* Search
- Finds the **fastest route** based on estimated travel times.
- Uses a **priority queue** and heuristic cost estimates to explore the most promising paths first.

## Example Usage & Test Results

### 1. From **AŞTİ** to **OSB**
- Least transfers:  
  `AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB`
- Fastest route *(25 min)*:  
  `AŞTİ → Kızılay → Kızılay → Ulus → Demetevler → OSB`

### 2. From **Batıkent** to **Keçiören**
- Least transfers:  
  `Batıkent → Demetevler → Gar → Keçiören`
- Fastest route *(21 min)*:  
  `Batıkent → Demetevler → Gar → Keçiören`

### 3. From **Keçiören** to **AŞTİ**
- Least transfers:  
  `Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ`
- Fastest route *(19 min)*:  
  `Keçiören → Gar → Gar → Sıhhiye → Kızılay → AŞTİ`

## Possible Improvements

- Expand the simulation to larger or real-world metro networks.
- Integrate other modes of public transport such as buses or trams.
- Add support for walking distances or paid services (e.g., taxi, Uber) for interchanges.
- Implement a **Night Mode** to simulate reduced service frequency during off-peak hours—this can help reduce energy consumption and optimize wait times.
- Add **visualizations and animations** for a more interactive user experience.

---



   
