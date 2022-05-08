# percolation
Simulation script of some percolation theory


Quick start:
- Run percolations.py with python3
- Choose "simulate"
- For board size choose "20"
- For probability choose "60"
- The simulation will run

Simulation: First, it generates a matrix of boolean values. Then, it runs an algorithm to determine if there is a continuous connection of true values from the top to the bottom. It will display an animation of that algorithm using letters to indicate continuous blocks of true values. At the end, it will give its result. The result will be displayed with Xs indicating true values that are part of the continuous block that runs to top to bottom (if there is no such block, there will be no Xs), Os indicating other true values, and ░s indicating false values.
