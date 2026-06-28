import time

network = {
    'A': {'state': True,  'edges': ['B']},
    'B': {'state': False, 'edges': ['C', 'D']},
    'C': {'state': False, 'edges': ['E']},
    'D': {'state': False, 'edges': []},
    'E': {'state': False, 'edges': []}
}

def tick(state_machine):
    updates = {}
    for node, data in state_machine.items():
        if data['state'] is True:
            for target in data['edges']:
                if state_machine[target]['state'] is False:
                    updates[target] = True
                    
    for node, new_state in updates.items():
        state_machine[node]['state'] = new_state
        
    return len(updates) > 0

print("Initial Network State:")
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
        print(f"  Node {node}: {data['state']}")
    print("-" * 30)
    time.sleep(0.5)
    
    if not changes_occurred:
        print("Network reached terminal state. Equilibrium.")
        running = False