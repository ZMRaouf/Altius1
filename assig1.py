class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"ListNode({self.data}) -> {self.next}"

def parser(inputfile):
    testcases = []

    with open(inputfile) as f:
        t = int(f.readline())
        for a in range(t):
            n = int(f.readline())
            llist1 = dummy = ListNode(0)
            for b in range(n):
                data = int(f.readline())
                llist1.next = ListNode(data)
                llist1 = llist1.next
            head1 = dummy.next

            m = int(f.readline())
            llist2 = dummy = ListNode(0)
            for c in range(m):
                data = int(f.readline())
                llist2.next = ListNode(data)
                llist2 = llist2.next
            head2 = dummy.next

            testcases.append([head1, head2])
    return testcases

def compare_lists(l1, l2):
    if l1 == None and l2 == None:
        return 1
    if l1 == None and l2 != None:
        return 0
    if l2 == None and l1 != None:
        return 0
    if l1.data != l2.data:
        return 0
    return compare_lists(l1.next, l2.next)

testcases = parser("assignment01-1.txt")
# testcases = parser("assignment01-2.txt")

for l1, l2 in testcases:
    result = compare_lists(l1, l2)
    print(result)