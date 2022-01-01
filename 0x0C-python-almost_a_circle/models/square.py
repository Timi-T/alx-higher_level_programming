#!/usr/bin/python3
"""
module for square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class square which is a subclass of rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.validate_dim(size, "width")
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[{}] ({:d}) {:d}/{:d} - {:d}".format(self.__class__.__name__,
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.validate_dim(value, "width")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        try:
            self.id = args[0]
            self.validate_dim(args[1], "width")
            self.width = args[1]
            self.height = args[1]
            self.validate_pos(args[2], "x")
            self.x = args[2]
            self.validate_pos(args[3], "y")
            self.y = args[3]
        except IndexError:
            pass
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.validate_dim(value, "width")
                    self.height = value
                    self.width = value
                elif key == "x":
                    self.validate_pos(value, "x")
                    self.x = value
                elif key == "y":
                    self.validate_pos(value, "y")
                    self.y = value

    def to_dictionary(self):
        dic_rep = {}
        dic_rep["id"] = self.id
        dic_rep["size"] = self.width
        dic_rep["x"] = self.x
        dic_rep["y"] = self.y
        return dic_rep
