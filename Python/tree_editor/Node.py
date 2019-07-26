#!/usr/bin/env python3

#todo:
#   update system
#       urls
#       attributes: subscribers, subscriptions


class Node:

    def __init__(self, value = ''):
        if not isinstance(value, str):
            raise TypeError
        self.value = value
        self.children = []
        self.parent = None
        self.index = None


    def save(self, filename = 'tree.txt', print_root = True):
        my_file = open(filename, 'w')
        my_file.write(self.__str__(print_root))
        my_file.close()


    @staticmethod
    def new_from_file(filename = 'tree.txt', hidden_root_default_value = 'ROOT'):

        hidden_root_detected = False

        # detect file settings: tab_size and minimal_indentation
        with open(filename, 'r') as my_file:

            line_no = 1
            line = my_file.readline()
            if not line:
                raise EOFError('empty file')
            indentation_1 = len(line) - len(line.lstrip(' '))
            indentation_2 = indentation_1
            while line and indentation_2 == indentation_1:
                line_no += 1
                line = my_file.readline()
                indentation_2 = len(line) - len(line.lstrip(' '))
            if not line:
                if indentation_1 > 0:
                    tab_size = indentation_1
                else:
                    # bogus value
                    tab_size = 1
            if indentation_2 != indentation_1:
                if indentation_2 < indentation_1:
                    raise IndentationError('', (filename, line_no, indentation_2, line))
                tab_size = indentation_2 - indentation_1
            minimal_indentation = indentation_1 // tab_size

        # parse the file: create the tree
        with open(filename, 'r') as my_file:

            line_no = 1
            line = my_file.readline()
            value = line.lstrip(' ')
            root = Node(value.rstrip('\n'))
            minimal_indentation = (len(line) - len(value)) // tab_size
            previous_indentation = minimal_indentation
            previous_node = root

            parents_stack = []
            line_no += 1
            line = my_file.readline()
            while line:
                value = line.lstrip(' ')
                new_node = Node(value.rstrip('\n'))
                new_indentation = (len(line) - len(value)) // tab_size
                if new_indentation > previous_indentation:
                    if new_indentation != previous_indentation + 1:
                        raise IndentationError('', (filename, line_no, (previous_indentation + 1) * tab_size, line))
                    parents_stack.append(previous_node)
                else:
                    if (not hidden_root_detected) and new_indentation == minimal_indentation:
                        # print('DEBUG: hidden_root_detected')
                        hidden_root_detected = True
                        new_root = Node(hidden_root_default_value)
                        parents_stack.insert(0, new_root)
                        new_root.adopt_child(root)
                        root = new_root
                    if new_indentation < previous_indentation:
                        if new_indentation < minimal_indentation:
                            raise IndentationError('', (filename, line_no, new_indentation * tab_size, line))
                        number_of_parents_to_remove = previous_indentation - new_indentation
                        parents_stack = parents_stack[:-number_of_parents_to_remove]
                parents_stack[-1].adopt_child(new_node)
                previous_indentation = new_indentation
                previous_node = new_node
                line_no += 1
                line = my_file.readline()

        return root


    def adopt_child_with_value(self, value = '', index = None):
        self.adopt_child(Node(value), index)


    #testme
    def adopt_child(self, new_child, index = None):

        # validate index
        if index is not None:
            # handle a strange index
            if index < 0:   # count from the end, like Python lists
                # determine the real index to save it in the child
                index += len(self.children)
            if index < 0 or index > len(self.children):
                raise IndexError(self.value, index, len(self.children))
        else: # by default, add at the end
            index = len(self.children)

        new_child.remove_parent()
        self.children.insert(index, new_child)
        new_child.parent = self
        new_child.index = index

                #testme
                #todo
                #todo: arg index
                def set_parent(self, new_parent = None):
                    if new_parent is not self.parent:
                        self.remove_parent()
                        if new_parent is not None:
                            new_parent.adopt_child(self)
                    else:
                        print('DEBUG: child already has this parent')


    # testme
    # todo
    # wrapper for adopt_child
    def set_parent(self, new_parent = None):
        if new_parent is None:
            self.remove_parent()
        else:
            new_parent.adopt_child(self)


    #testme
    def remove_parent(self):
        parent = self.parent
        if parent is not None:
            parent.children.pop(self.index)
            self.parent = None
            self.index = None
        # else:
            # print('DEBUG: no parent already')
        return parent


    #testme
    def remove_child_at_index(self, index):
        child = self.children.pop(index)
        child.parent = None
        child.index = None
        return child


    def change_child_index(self, current_index, new_index):
        self.children.insert(new_index, self.remove_child_at_index(current_index))


    def __str__(self, print_root = True, tab_size = 4, min_amount_of_tabs = 0):
        tab = tab_size * ' '
        tabs = min_amount_of_tabs * tab
        return self.__str__helper(tabs, tab, print_root)


    def __str__helper(self, tabs, tab, print_root = True):
        result = ''
        if print_root:
            # node value
            result += tabs + self.value + '\n'
            tabs += tab
        # node children
        result += ''.join([s.__str__helper(tabs, tab) for s in self.children])
        return result


    def __repr__(self):
        # (ambiguous output)
        # return self.value
        return self.__str__()


    def __eq__(self, other):
        # (does not test equality of parents)
        return self.value == other.value and self.children == other.children
    

if __name__ == '__main__':
    # p = Node.new_from_file()

    n = Node('test')
    n.adopt_child_with_value('hello')
    n.adopt_child_with_value('hey')
    n.adopt_child_with_value('you')
    n.children[0].adopt_child_with_value('hi')
    n.children[0].children[0].adopt_child_with_value('welcome')
    n.children[0].children[0].adopt_child_with_value('cheers')
    n.children[1].adopt_child_with_value('good evening')

    # print(n == p)
    # p.value = n.value
    # print(n == p)

    print(n)
    print('-------')
    print(n.__str__(print_root = False))

    n.save()
    # n.save(print_root = False)
