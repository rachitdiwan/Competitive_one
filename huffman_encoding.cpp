import copy


class Nodet:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, value):
        self.size += 1
        if self.head is None:
            self.head = Nodet(value)
            return
        new_node = Nodet(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        val = self.head.value
        self.head = self.head.next
        self.size -= 1
        return val

    def size(self):
        return self.size()

    def get_head(self):
        if self.head is not None:
            return self.head.value
        return None


class Node:

    def __init__(self, val, ch=None):
        self.ch = ch
        self.val = val
        self.left = None
        self.right = None
        self.visit_left = False
        self.visit_right = False

    def has_right_child(self):
        return self.right is not None

    def has_left_child(self):
        return self.left is not None

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def set_value(self, val, ch=None):
        self.ch = char
        self.val = val

    def get_char(self):
        return self.ch

    def get_value(self):
        return self.val

    def visited_left(self):
        self.visit_left = True

    def visited_right(self):
        self.visit_right = True

    def done_left(self):
        return self.visit_left

    def done_right(self):
        return self.visit_right

    def get_right_child(self):
        return self.right

    def get_left_child(self):
        return self.left

    def __repr__(self):
        return(str(self.ch)+" : "+str(self.val))


class Tree:

    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root


def frequency(string):
    freqen = []
    checker = []
    flag = False
    for i in range(len(string)):
        count = 0
        for j in range(i, len(string)):
            if string[i] not in checker and string[j] == string[i]:
                count += 1
                flag = True
        if flag:
            freqen.append([string[i], count])
            checker.append(string[i])
            flag = False
    return freqen


def freq_sort(string):
    listo = frequency(string)
    new_listo = []
    com = []
    for _ in listo:
        com.append(_[1])
    min = max(com)
    ran = len(listo)
    for i in range(ran):
        pos = 0
        for val in listo:
            if val[1] <= min:
                min = copy.copy(val[1])
                min_pos = copy.copy(pos)
            pos += 1
        if listo[min_pos] not in new_listo:
            new_listo.append(listo[min_pos])
            x = listo.pop(min_pos)
            min = max(com)
    return new_listo


def into_tree(string):
    listo = freq_sort(string)
    node_list = []
    for val in listo:
        node_list.append(Node(val[1], val[0]))
    tree = Tree()
    if len(node_list)==1:
    	tree.set_root(Node(node_list[0].get_value()))
    	tree.get_root().set_left_child(node_list[0])
    	return tree.get_root()
    tree.set_root(Node((node_list[0].get_value()+node_list[1].get_value())))
    tree.get_root().set_left_child(node_list[0])
    tree.get_root().set_right_child(node_list[1])
    i = 2
    while i != len(node_list):
        if i+1 == len(node_list) or ((tree.get_root().get_value()+node_list[i].get_value()) <= (node_list[i].get_value() + node_list[i+1].get_value())):
            new_node = Node((tree.get_root().get_value()+node_list[i].get_value()))
            new_node.set_left_child(tree.get_root())
            new_node.set_right_child(node_list[i])
            tree.set_root(new_node)
            i += 1
        else:
            new_node = Node(node_list[i].get_value() + node_list[i+1].get_value())
            new_node.set_left_child(node_list[i])
            new_node.set_right_child(node_list[i+1])
            new_node_two = Node((tree.get_root().get_value() + new_node.get_value()))
            new_node_two.set_left_child(tree.get_root())
            new_node_two.set_right_child(new_node)
            tree.set_root(new_node_two)
            i += 2
    return tree.get_root()


def code_generator(string):
    node = into_tree(string)
    stack = Stack()
    string = ""
    dicto = dict()
    stack.push(node)
    while True:
        if node.has_left_child() and not node.done_left():
            node.visited_left()
            node = node.get_left_child()
            stack.push(node)
            string += "0"
        elif node.has_right_child() and not node.done_right():
            node.visited_right()
            node = node.get_right_child()
            stack.push(node)
            string += "1"
        elif not node.has_right_child() and not node.has_left_child():
            dicto[node.get_char()] = copy.deepcopy(string)
            stack.pop()
            node = stack.get_head()
            string = string[:-1]
        else:
            stack.pop()
            node = stack.get_head()
            if node is None:
                break
            else:
                string = string[:-1]
   
    return dicto


def encoder(sentence):
    encoded = code_generator(sentence)
    ret_sent = ""
    for value in sentence:
        ret_sent += encoded[value]
        ret_sent += "-"
    return ret_sent[:-1]


def decoder(string, sentence):
    encoded = code_generator(sentence)
    decoded = dict([(value, key) for key, value in encoded.items()])
    return_Val = ""
    str_lst = string.split("-")
    for val in str_lst:
        return_Val += decoded[val]
    return return_Val


def represent(sentence):
    print("The Given Sentence is :\n"+sentence)
    print("The encoded string is :\n"+encoder(sentence))
    print("The decoded sentence is:\n"+decoder(encoder(sentence),sentence))

sentence = "AAAAAAAAAAAAAAAAAA"
sentence_two = "UDACITYNANODEGREE"
sentence_three = "THIS IS A PLEASANT DAY"
represent(sentence)
represent(sentence_two)
represent(sentence_three)

