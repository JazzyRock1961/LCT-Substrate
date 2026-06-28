import time
import random

# --- The Initialization ---
# Node A has an OR path allocation to choose between path B or path C.
# It simulates a single discrete state transaction choosing a runtime path.
network = {
    'A': {'state': True,  'options': ['B', 'C']},
    'B': {'state': False, 'edges': ['D']},
    'C': {'state': False, 'edges': ['D']},
    'D': {'state': False, 'edges': []}
}

def tick(state_machine):
    """
    The Transaction Engine: Evaluates conditional OR choices.
    """
    updates = {}
    path_chosen = None
    
    for node, data in state_machine.items():
        if data['state'] is True:
            # Check for an OR choice constraint
            if 'options' in data and data['options']:
                # Filter out options that are already True to prevent reprocessing
                available_paths = [opt for opt in data['options'] if not state_machine[opt]['state']]
                if available_paths:
                    path_chosen = random.choice(available_paths)
                    updates[path_chosen] = True
            # Standard edge propagation (if-then / AND)
            elif 'edges' in data:
                for target in data['edges']:
                    if state_machine[target]['state'] is False:
                        updates[target] = True
                        
    for node, new_state in updates.items():
        state_machine[node]['state'] = new_state
        
    return updates, path_chosen

# --- The Execution Loop ---
print("Initial Network State (OR Path Pending):")
for node, data in network.items():
    print(f"  Node {node}: {data['state']}")
print("-" * 30)

step = 0
running = True

while running:
    step += 1
    print(f"Clock Tick {step}:")
    
    updates, chosen = tick(network)
    
    if chosen:
        print(f"  [OR Choice Executed]: Selected Path -> Node {chosen}")
        
    for node, data in network.items():
        print(f"  Node {node}: {data['state']}")
        
    print("-" * 30)
    time.sleep(0.5)
    
    if not updates:
        print("Network reached terminal state. Transaction finalized.")
        running = False