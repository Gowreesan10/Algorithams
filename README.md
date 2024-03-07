# Algorithams

# Ford Flukerson

## Overview
This Python script, `Ford Flukerson.py`, provides a solution to the committee assignment problem using the Ford-Fulkerson algorithm for finding maximum flow in a flow network.

## Input and Output
The script takes input from a file, which includes details of people, committees, preferences, and capacities. It then writes the results to an output file in the following format:
```
-----------------------------
Person: Committees
P1 : C1 C2
P2 : C2 C4
P3 : C1 C2 C3
-----------------------------
Committee: Person
C1 : P1 P3
C2 : P1 P2 P3
C3 : P3
C4 : P2
-----------------------------
```

## Usage
To use the script:
1. Prepare an input file with the necessary details.
2. Run the `Ford Flukerson.py` script.
3. Check the output file for the committee assignments.

# RedBlackTrees

## Overview
This script, `RedBlack Trees.py`, implements Red-Black Trees, a type of self-balancing binary search tree. It supports insertion, deletion, and various tree query operations.

## Operations Supported
The script supports the following operations:

- **Insertion**: Add a new node to the tree while maintaining Red-Black tree properties.
- **Deletion**: Remove a node from the tree while preserving Red-Black tree properties.
- **Tree Queries**:
  - **Search**: Find a specific key in the tree.
  - **Maximum**: Retrieve the node with the maximum key in the tree.
  - **Minimum**: Retrieve the node with the minimum key in the tree.

## Usage
To utilize `RedBlack Trees.py`:
1. Import the script into your Python environment.
2. Utilize the provided functions to perform tree operations.

This script provides efficient methods for managing and querying data within a Red-Black tree structure.
