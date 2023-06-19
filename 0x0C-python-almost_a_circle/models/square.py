#!/usr/bin/python3


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super.__init__(width, height, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Prints [Square] (<id>) <x>/<y> - <size>"""
        return "[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y,
            self.size)

    def update(self, *args, **kwargs):
        if args:
            if args >= 1:
                self.id = args[0]
            if args >= 2:
                self.size = args[1]
            if args >= 3:
                self.x = args[2]
            if args >= 4:
                self.y = args[3]

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        keys_to_include = ['id', 'size', 'x', 'y']
        return {key: value for key, value in
                super().__dict__.items()
                if key in keys_to_include}
