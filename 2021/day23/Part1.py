import heapq
COSTS = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOM_X = {'A': 2, 'B': 4, 'C': 6, 'D': 8}
HALLWAY_STOPS = [0, 1, 3, 5, 7, 9, 10]


def get_possible_moves(state):
    hallway, rooms = state
    possible = []

    for i, pod in enumerate(hallway):
        if pod is None or pod == '.': continue

        target_idx = ord(pod) - ord('A')
        target_room = rooms[target_idx]

        if all(p == '.' or p == pod for p in target_room):
            start, end = i, ROOM_X[pod]
            step = 1 if end > start else -1
            path = range(start + step, end + step, step)

            if all(hallway[j] == '.' or hallway[j] is None for j in path):
                depth = max(d for d, p in enumerate(target_room) if p == '.')
                dist = abs(end - start) + (depth + 1)

                new_h = list(hallway)
                new_h[i] = '.'
                new_rs = [list(r) for r in rooms]
                new_rs[target_idx][depth] = pod

                new_state = (tuple(new_h), tuple(tuple(r) for r in new_rs))
                return [(new_state, dist * COSTS[pod])]

    for r_idx, room in enumerate(rooms):
        pod_type = chr(ord('A') + r_idx)

        if all(p == pod_type or p == '.' for p in room):
            continue

        depth, pod = next(((d, p) for d, p in enumerate(room) if p != '.'), (None, None))
        if pod is None: continue

        curr_x = ROOM_X[pod_type]
        for target_x in HALLWAY_STOPS:
            step = 1 if target_x > curr_x else -1
            path = range(curr_x, target_x + step, step)

            if all(hallway[j] == '.' or hallway[j] is None for j in path):
                dist = (depth + 1) + abs(target_x - curr_x)

                new_h = list(hallway)
                new_h[target_x] = pod
                new_rs = [list(r) for r in rooms]
                new_rs[r_idx][depth] = '.'

                new_state = (tuple(new_h), tuple(tuple(r) for r in new_rs))
                possible.append((new_state, dist * COSTS[pod]))

    return possible

def solve(initial_rooms):
    initial_hallway = ('.', '.', None, '.', None, '.', None, '.', None, '.', '.')
    state = (initial_hallway, initial_rooms)

    room_size = len(initial_rooms[0])
    goal_rooms = tuple(tuple(chr(ord('A') + i) for _ in range(room_size)) for i in range(4))

    pq = [(0, state)]
    visited = {state: 0}

    while pq:
        energy, curr_state = heapq.heappop(pq)

        if curr_state[1] == goal_rooms:
            return energy

        if energy > visited.get(curr_state, float('inf')):
            continue

        for next_state, move_cost in get_possible_moves(curr_state):
            new_energy = energy + move_cost
            if new_energy < visited.get(next_state, float('inf')):
                visited[next_state] = new_energy
                heapq.heappush(pq, (new_energy, next_state))
    return None

rooms = (('D', 'B'), ('D', 'A'), ('C', 'B'), ('C', 'A'))
print(solve(rooms))
