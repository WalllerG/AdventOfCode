import collections
with open('input.txt')as f:
    scanners = [[tuple(map(int, line.split(","))) for line in s.split("\n")[1:] if line]for s in f.read().strip().split("\n\n")]
def get_rotations(point):
    x, y, z = point
    return [
        (x,y,z), (x,-z,y), (x,-y,-z), (x,z,-y),
        (-x,-y,z), (-x,z,y), (-x,y,-z), (-x,-z,-y),
        (y,z,x), (y,-x,z), (y,-z,-x), (y,x,-z),
        (-y,-z,x), (-y,x,z), (-y,z,-x), (-y,-x,-z),
        (z,x,y), (z,-y,x), (z,-x,-y), (z,y,-x),
        (-z,-x,y), (-z,y,x), (-z,x,-y), (-z,-y,-x)
    ]

scanner_rots = []
for s in scanners:
    rots = [[] for _ in range(24)]
    for p in s:
        for i, rotated_p in enumerate(get_rotations(p)):
            rots[i].append(rotated_p)
    scanner_rots.append(rots)

fixed_beacons = set(scanners[0])
aligned_indices = {0}
scanner_positions = {0: (0, 0, 0)}
queue = collections.deque([0])

while queue:
    ref_idx = queue.popleft()
    ref_beacons = [p for p in fixed_beacons] # Beacons already in global coord system

    for i in range(len(scanners)):
        if i in aligned_indices: continue
            
        found = False
        for rot_idx in range(24):
            candidate_points = scanner_rots[i][rot_idx]
            diffs = collections.defaultdict(int)
                
            for p_fixed in fixed_beacons:
                for p_cand in candidate_points:
                    dx = p_fixed[0] - p_cand[0]
                    dy = p_fixed[1] - p_cand[1]
                    dz = p_fixed[2] - p_cand[2]
                    diffs[(dx, dy, dz)] += 1
                
            for offset, count in diffs.items():
                if count >= 12:
                    scanner_positions[i] = offset
                    for p in candidate_points:
                        fixed_beacons.add((p[0]+offset[0], p[1]+offset[1], p[2]+offset[2]))
                    aligned_indices.add(i)
                    queue.append(i)
                    found = True
                    break
            if found: break
print(len(fixed_beacons))
