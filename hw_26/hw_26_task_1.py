class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def delete(self, data):
        prev_node = None
        this_node = self.root
        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False

    def search(self, data):
        this_node = self.root
        while this_node:
            if this_node.data == data:
                return True
            this_node = this_node.next_node
        return False

    def elements(self):
        this_node = self.root
        output = ""
        while this_node:
            output += str(this_node.data) + "->"
            this_node = this_node.next_node
        return output.rstrip("->")

    def selection_sort(self):
        if not self.root:
            return
        this_node = self.root
        while this_node:
            min_node = this_node
            next_node = this_node.next_node
            while next_node:
                if next_node.data < min_node.data:
                    min_node = next_node
                next_node = next_node.next_node
            this_node.data, min_node.data = min_node.data, this_node.data
            this_node = this_node.next_node


new_list = LinkedList()
new_list.add(1)
new_list.add(2)
new_list.add(3)
new_list.add(4)
print(new_list.elements())
new_list.delete(2)
print(new_list.elements())
print(new_list.search(8))
new_list.selection_sort()
print(new_list.elements())
