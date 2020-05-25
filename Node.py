class Node:

    def __init__(self, name, parentName = None, f = None, g = 0, h = 0):
        self.name = name
        self.parentName = parentName
        self.f = f if f else g+h
        self.g = g
        self.h = h