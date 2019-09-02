# BottleRocketSimulator
Simulates the path of a bottle rocket initial physical parameters of the bottle at start.

## Prerequisites

- Python 3
- Matplotlib
- Numpy

## Usage

- Clone the repository, run `main.py`. A plot will be generated as `result.png` displaying trajectory and length.
- Given parameters (such as *p<sub>atm</sub>*, *p<sub>over</sub>*, *m<sub>bottle</sub>*, *m<sub>water</sub>*, *V<sub>bottle</sub>*, *V<sub>water</sub>*) can easily be changed in `bottle_rocket_simulator.py`.

## Method

1. The initial velocity (ΔV) is approximated using starting parameters.
2. Trajectory is approximated with iterated steps given drag and gravity parameters.

## Result

![](result.png)

## TODOs

- [ ] Make better approximation of initial velocity.