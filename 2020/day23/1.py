with open('input.txt')as f:
    data = list(map(int, list(f.read())))

class Node():
        def __init__(self, num):
            self.num = num
            self.prev = None
            self.next = None

class DLL():
    def __init__(self):
        self.head = None
        self.tail = None
        self.cur = None

    def add(self, num):
        new_node = Node(num)
        if not self.head:
            self.head = new_node
            self.cur = self.head
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last
        self.tail = new_node

    def connect(self):
        self.tail.next = self.head
        self.head.prev = self.tail

    def move(self):
        pl = self.cur.next
        pr = self.cur.next.next.next
        next_cup = pr.next
        pickup = [self.cur.next.num, self.cur.next.next.num, self.cur.next.next.next.num]

        destination = (self.cur.num - 2) % len(data) + 1
        while destination in pickup:
            destination = (destination-2) % len(data) + 1

        destination_node = self.cur.next
        while destination_node.num != destination:
            destination_node = destination_node.next
        
        self.cur.next = pr.next
        pr.next.prev = self.cur

        pr.next = destination_node.next
        destination_node.next.prev = pr

        destination_node.next = pl
        pl.prev = destination_node
        
        self.cur = next_cup

    def display(self):
        ans = []
        cur = self.cur
        while len(ans) < 9:
            ans.append(cur.num)
            cur = cur.next
        print("".join(map(str, ans)))

    def printAns(self):
        ans = []
        cur = self.cur
        while cur.num != 1:
            cur = cur.next
        start = cur.next
        while start.num != 1:
            ans.append(start.num)
            start = start.next
        print("".join(map(str, ans)))

dll = DLL()

for cup in data:
    dll.add(cup)
    
dll.connect()

for _ in range(100):
    dll.move()

dll.printAns()