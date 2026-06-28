import time

# --- The Initialization ---
# Multiple parallel pathways (B and C) converge on a single bottleneck node (D).
network = {
    'A': {'state': True,  'edges': ['B', 'C']},
    'B': {'state': False, 'edges': ['D']},
    'C': {'state': False, 'edges': ['D']},
    'D': {'state': False, 'edges': ['E'], 'congestion_count': 0},
    'E': {'state': False, 'edges': []}
}

def tick(state_machine):
    """
    The Congestion Engine: Tracks simultaneous arrivals at a single coordinate.
    """
    updates = {}
    
    # Reset congestion counts for the current tick
    for node in state_machine.values():
        if 'congestion_count' in node:
            node['congestion_count'] = 0

    # Evaluate propagation and calculate traffic density
    for node, data in state_machine.items():
        if data['state'] is True:
            for target in data['edges']:
                if state_machine[target]['state'] is False:
                    updates[target] = True
                    # If the target tracks congestion, increment the counter
                    if 'congestion_count' in state_machine[target]:
                        state_machine[target]['congestion_count'] += 1
                    
    # Apply updates simultaneously
    for node, new_state in updates.items():
        state_machine[node]['state'] = new_state
        
    return len(updates) > 0

# --- The Execution Loop ---
print("Initial Network State (Parallel Tracks Ready):")
for node, data in network.items():
    print(f"  Node {node}: {data['state']}")
print("-" * 30)

step = 0
running = True

while running:
    step += 1
    print(f"Clock Tick {step}:")
    
    changes_occurred = tick(network)
    
    for node, data in network.items():
        congestion_info = f" (Traffic Density: {data['congestion_count']})" if 'congestion_count' in data else ""
        print(f"  Node {node}: {data['state']}{congestion_info}")
        
    print("-" * 30)
    time.sleep(0.5)
    
    if not changes_occurred:
        print("Network reached terminal state. Traffic resolved.")
        running = False