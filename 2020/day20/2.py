import re
import numpy as np
from collections import defaultdict

def get_orientations(grid):
    """Generates all 8 rotations and flips of a 2D array."""
    for _ in range(4):
        yield grid
        yield np.fliplr(grid)
        grid = np.rot90(grid)

def get_edges(grid):
    """Returns top, bottom, left, right edges as strings."""
    return (
        "".join(grid[0, :]),    # Top
        "".join(grid[-1, :]),   # Bottom
        "".join(grid[:, 0]),    # Left
        "".join(grid[:, -1])    # Right
    )

with open('input.txt') as f:
    tiles_raw = f.read().strip().split('\n\n')

tiles = {}
tile_edges = defaultdict(list)

for tr in tiles_raw:
    lines = tr.splitlines()
    tid = int(re.findall(r'\d+', lines[0])[0])
    grid = np.array([list(l) for l in lines[1:]])
    tiles[tid] = grid
    
    t, b, l, r = get_edges(grid)
    for edge in [t, b, l, r, t[::-1], b[::-1], l[::-1], r[::-1]]:
        tile_edges[edge].append(tid)

adj = defaultdict(set)
for edge, ids in tile_edges.items():
    if len(ids) > 1:
        for i in ids:
            for j in ids:
                if i != j: adj[i].add(j)

corners = [tid for tid, neighbors in adj.items() if len(neighbors) == 2]

size = int(len(tiles)**0.5)
assembled = [[None] * size for _ in range(size)]
used = set()

start_tid = corners[0]
for orient in get_orientations(tiles[start_tid]):
    t, b, l, r = get_edges(orient)
    if len(tile_edges[t]) == 1 and len(tile_edges[l]) == 1:
        assembled[0][0] = (start_tid, orient)
        used.add(start_tid)
        break

for r in range(size):
    for c in range(size):
        if assembled[r][c] is not None: continue
        
        if c > 0:
            prev_tid, prev_grid = assembled[r][c-1]
            _, _, _, target_edge = get_edges(prev_grid)
            match_idx = 2
        else:
            prev_tid, prev_grid = assembled[r-1][c]
            _, target_edge, _, _ = get_edges(prev_grid)
            match_idx = 0
            
        potential_ids = [tid for tid in adj[prev_tid] if tid not in used]
        for tid in potential_ids:
            found = False
            for orient in get_orientations(tiles[tid]):
                curr_edges = get_edges(orient)
                if curr_edges[match_idx] == target_edge:
                    assembled[r][c] = (tid, orient)
                    used.add(tid)
                    found = True
                    break
            if found: break

image_blocks = []
for row in assembled:
    trimmed_row = [grid[1:-1, 1:-1] for tid, grid in row]
    image_blocks.append(np.hstack(trimmed_row))
full_image = np.vstack(image_blocks)

monster = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   "
]
m_h, m_w = 3, 20
m_coords = [(r, c) for r in range(m_h) for c in range(m_w) if monster[r][c] == '#']

monster_count = 0
for img_orient in get_orientations(full_image):
    h, w = img_orient.shape
    for r in range(h - m_h):
        for c in range(w - m_w):
            if all(img_orient[r + dr, c + dc] == '#' for dr, dc in m_coords):
                monster_count += 1
    if monster_count > 0:
        total_hashes = np.count_nonzero(img_orient == '#')
        print(total_hashes - (monster_count * 15))
        break