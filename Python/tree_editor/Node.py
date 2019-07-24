#!/usr/bin/env python3

class Node:

    def __init__(self, value = ""):
        assert(isinstance(value, str))
        self.value = value
        self.children = []


    @staticmethod
    def new_from_file(filename = 'tree.txt', tab_size = 4, hidden_root_default_value = 'ROOT'):

        hidden_root_detected = False

        with open(filename, 'r') as my_file:

            line = my_file.readline()
            assert(line)
            value = line.lstrip(' ')
            root = Node(value.rstrip('\n'))
            minimal_indentation = (len(line) - len(value)) // tab_size
            previous_indentation = minimal_indentation
            previous_node = root

            parents_stack = []
            line = my_file.readline()
            while line:

                value = line.lstrip(' ')
                new_node = Node(value.rstrip('\n'))
                new_indentation = (len(line) - len(value)) // tab_size

                if new_indentation > previous_indentation:
                    assert(new_indentation == previous_indentation + 1)
                    parents_stack.append(previous_node)
                else:
                    if (not hidden_root_detected) and new_indentation == minimal_indentation:
                        # print('DEBUG: hidden_root_detected')
                        hidden_root_detected = True
                        new_root = Node(hidden_root_default_value)
                        parents_stack.insert(0, new_root)
                        new_root.add_node(root)
                        root = new_root
                    if new_indentation < previous_indentation:
                        assert(new_indentation >= minimal_indentation)
                        number_of_parents_to_remove = previous_indentation - new_indentation
                        parents_stack = parents_stack[:-number_of_parents_to_remove]

                parents_stack[-1].add_node(new_node)
                previous_indentation = new_indentation
                previous_node = new_node
                line = my_file.readline()
        
        return root


    def add_node_from_value(self, value = "", position = None):
        self.add_node(Node(value), position)


    def add_node(self, node, position = None):
        # (does not check for duplicate node references)

        if position is None: # by default, append at the end
            position = len(self.children)

        self.children.insert(position, node)


    def pop_node_at_index(self, index):
        return self.children.pop(index)


    def change_child_index(self, current_index, new_index):
        self.children.insert(new_index, self.pop_node_at_index(current_index))


    def save(self, filename = 'tree.txt', print_first_value = True):
        my_file = open(filename, 'w')
        my_file.write(self.__str__(print_first_value))
        my_file.close()


    def __str__(self, print_first_value = True, min_indentation = 0, tab_size = 4):
        tab = tab_size * " "
        tabs = min_indentation * tab
        return self.__str__helper(print_first_value, tabs, tab)


    def __str__helper(self, print_first_value = True, tabs = '', tab = ''):
        result = ''
        if print_first_value:
            # node value
            result += tabs + self.value + "\n"
            tabs += tab
        # node children
        result += ''.join([s.__str__helper(True, tabs, tab) for s in self.children])
        return result


    def __repr__(self):
        # (ambiguous output)
        # return self.value
        return self.__str__()

    def __eq__(self, other):
        return self.value == other.value and self.children == other.children


if __name__ == '__main__':
    p = Node.new_from_file()
    n = Node('test')
    n.add_node_from_value('hello')
    n.add_node_from_value('hey')
    n.add_node_from_value('you')
    n.children[0].add_node_from_value('hi')
    n.children[0].children[0].add_node_from_value('welcome')
    n.children[0].children[0].add_node_from_value('cheers')
    n.children[1].add_node_from_value('good evening')
    print(n == p)
    p.value = n.value
    print(n == p)

    # print(n)
    # print()
    # print(n.__str__(print_first_value = False))

    # n.save()
    # n.save(print_first_value = False)
