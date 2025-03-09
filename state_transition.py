import random

def state_transition_dict(polyomino):
    """returns a dictionary representing the state transition function for the given polyomino"""
    n = len(polyomino)
    num_states = 2 ** n
    transition_dict = {}

    for state in range(num_states):
        binary_state = format(state, f'0{n}b')
        next_state = list(binary_state)

        for i in range(n):
            neighbors = get_neighbors(polyomino, i)
            equal_count = sum(1 for neighbor in neighbors if binary_state[neighbor] == binary_state[i])
            not_equal_count = len(neighbors) - equal_count

            if not_equal_count > equal_count:
                next_state[i] = '1' if binary_state[i] == '0' else '0'

        binary_next_state = ''.join(next_state)
        transition_dict[binary_state] = binary_next_state

    return transition_dict

def get_neighbors(polyomino, index):
    """returns the indices of the neighbors of the given index in the polyomino"""
    neighbors = []
    x, y = polyomino[index]

    for i, (nx, ny) in enumerate(polyomino):
        if (nx == x and abs(ny - y) == 1) or (ny == y and abs(nx - x) == 1):
            neighbors.append(i)

    return neighbors

def state_cyclicity(transition_dict, max_iterations):
    """returns a tuple with a dictionary specifying the cyclicity of each state and the max cycle length"""
    cyclicity_dict = {}
    visited = set()
    max_cycle_length = 0

    def dfs(state, path):
        nonlocal max_cycle_length
        if state in cyclicity_dict:
            return
        if state in path:
            cycle_length = len(path) - path.index(state)
            max_cycle_length = max(max_cycle_length, cycle_length)
            for s in path[path.index(state):]:
                cyclicity_dict[s] = cycle_length
            for s in path[:path.index(state)]:
                cyclicity_dict[s] = 0
            return
        path.append(state)
        next_state = transition_dict[state]
        dfs(next_state, path)
        path.pop()

    states = list(transition_dict.keys())
    random.shuffle(states)

    iterations = 0
    for state in states:
        if state not in visited:
            dfs(state, [])
            visited.update(cyclicity_dict.keys())
            iterations += 1
            if iterations >= max_iterations:
                break

    # Ensure all states are included in the cyclicity_dict
    for state in transition_dict:
        if state not in cyclicity_dict:
            cyclicity_dict[state] = 0

    return cyclicity_dict, max_cycle_length

polyomino = [
    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5)
]
stdict = state_transition_dict(polyomino)
stcyclicity, max_cycle_length = state_cyclicity(stdict,1000)

print("State transition function:")
print(stdict)
print("\nState cyclicity:")
print(stcyclicity)
print("\nMax cycle length:")
print(max_cycle_length)