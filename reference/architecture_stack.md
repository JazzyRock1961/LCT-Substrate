# Architecture Stack

This file defines the structural hierarchy of the LCT state machine layers.

## The Execution Order
```text
[ Layer 0: LCT Substrate ]  -> Primitive State Logic (if-then / AND / OR)
           ↓
[ Layer 1: Mathematics ]    -> Interface (Coordinate Maps, Grid Constraints)
           ↓
[ Layer 2: Physics ]        -> Instantiated Behavior (Propagation, Congestion)