# Ford-Fulkerson Algorithm with Augmenting Path Variants

This Python script implements the Ford-Fulkerson algorithm for finding the maximum flow in a flow network. The script provides variations of augmenting path algorithms and conducts simulations on different graphs.

## Table of Contents
- [Introduction](#introduction)
- [Usage](#usage)
- [Algorithms](#algorithms)
- [Simulation](#simulation)
- [Graph Representation](#graph-representation)
- [Simulations](#simulations)
- [File Loading](#file-loading)
- [Example Simulations](#example-simulations)

## Introduction

The Ford-Fulkerson algorithm is a widely used algorithm for solving the maximum flow problem in a flow network. The script includes several augmenting path algorithms, such as Shortest Augmenting Path, Depth-First Search-like, Max Capacity, and Random Augmenting Path.

## Usage

To use the script, you can modify the `simulation_values` list to define the parameters for the simulations. Then, run the script to perform the simulations and display the results.

## Algorithms

The following augmenting path algorithms are implemented:

1. **Shortest Augmenting Path (SAP):** Finds the shortest augmenting path using Dijkstra's algorithm.
2. **Depth-First Search-like (DFS):** Utilizes a depth-first search approach to find augmenting paths.
3. **Max Capacity:** Selects paths with maximum capacity at each step.
4. **Random Augmenting Path:** Randomly selects augmenting paths.

## Simulation

The script conducts simulations for each augmenting path algorithm on different randomly generated graphs. The simulations display various metrics, including the number of paths, mean length (ML), mean proportional length (MPL), total edges, and the resulting maximum flow.

## Graph Representation

The flow network is represented as an adjacency matrix. The `Graph.py` file contains a function `generate_source_sink_graph` to generate a random graph with source and sink nodes.

## Simulations

Simulations are performed on graphs with different sizes (`n`), edge probabilities (`r`), and upper capacities. The results are displayed in a tabular format using the `tabulate` library.

## File Loading

The script includes a function `load_graph_from_file` to load a graph from a file. The file format is assumed to have the following structure:


## Example Simulations

The script includes an example set of simulations defined in the `simulation_values` list. The graph parameters are specified, and graphs are generated using the `generate_source_sink_graph` function. Simulations are then run on these graphs, and the results are displayed.

Feel free to customize the script based on your specific requirements and use cases.

## How to run

- pip install tabulate
- python Augumenting-Path.py
