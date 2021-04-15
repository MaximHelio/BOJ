n = 5

class Node:
    def __init__(self, num):
        self.data = None
        self.num = num
        self.left = None
        self.right = None

tree = Node(0)
def find(node, num):
    if node is None: return None
    if node.num == num: return node
    find_sub = find(node.left, num)
    if find_sub is None: find_sub = find(node.right, num)
    return find_sub

for i in range(n):
    input_str = input()
    splited_input = input_str.split()
    if len(splited_input) == 4: # 연산자
        num = int(splited_input[0])
        data = splited_input[1]
        left_child_num = int(splited_input[2])
        right_child_num = int(splited_input[3])
        my_node = find(tree, num)
        if my_node is None: my_node = Node(num)
        if tree.left is None: tree.left = my_node
        my_node.data = data
        my_node.left = Node(left_child_num)
        my_node.right = Node(right_child_num)
    else: # 숫자
        num = int(splited_input[0])
        data = int(splited_input[1])
        my_node = find(tree, num)
        my_node.data = data
print(tree)
