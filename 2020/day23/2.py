with open('input.txt')as f:
    data = list(map(int, list(f.read())))

nodes = {}

class Node:
    def __init__(self, num):
        self.num = num
        self.next = None

def solve():
    full_data = data + list(range(max(data) + 1, 1000001))
    
    prev_node = None
    first_node = None
    
    for val in full_data:
        new_node = Node(val)
        nodes[val] = new_node
        if prev_node:
            prev_node.next = new_node
        else:
            first_node = new_node
        prev_node = new_node
    
    prev_node.next = first_node
    
    curr_node = first_node
    max_val = 1000000

    for _ in range(10000000):
        p1 = curr_node.next
        p2 = p1.next
        p3 = p2.next
        
        curr_node.next = p3.next
        
        pickup_vals = {p1.num, p2.num, p3.num}
        
        dest_val = curr_node.num - 1
        if dest_val < 1: dest_val = max_val
        while dest_val in pickup_vals:
            dest_val -= 1
            if dest_val < 1: dest_val = max_val
        
        dest_node = nodes[dest_val]
        
        p3.next = dest_node.next
        dest_node.next = p1
        
        curr_node = curr_node.next

    node_one = nodes[1]
    val1 = node_one.next.num
    val2 = node_one.next.next.num
    
    print(val1 * val2)

solve()