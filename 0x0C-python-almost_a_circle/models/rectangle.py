#!/usr/bin/python3
"""
module with rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.validate_dim(width, "width")
        self.validate_dim(height, "height")
        self.validate_pos(x, 'x')
        self.validate_pos(y, 'y')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    def validate_dim(self, dim_value, dim_name=""):
        """method to validate dimensions (width and height)
        """
        if (isinstance(dim_value, int) is False) or\
                (isinstance(dim_value, bool) is True):
            raise TypeError("{} must be an integer".format(dim_name))
        elif dim_value <= 0:
            raise ValueError("{} must be > 0".format(dim_name))
        else:
            return True

    def validate_pos(self, pos_value, pos_axis=''):
        """method to validate position (x and y)
        """
        if (isinstance(pos_value, int) is False) or\
                (isinstance(pos_value, bool) is True):
            raise TypeError("{} must be an integer".format(pos_axis))
        elif pos_value < 0:
            raise ValueError("{} must be >= 0".format(pos_axis))
        else:
            return True
        return False

    @property
    def width(self):
        """getter for width
        """
        return self.__width

    @property
    def height(self):
        """getter for height
        """
        return self.__height

    @property
    def x(self):
        """getter for x
        """
        return self.__x

    @property
    def y(self):
        """getter for y
        """
        return self.__y

    @width.setter
    def width(self, value):
        """setter for width
        """
        self.validate_dim(value, "width")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for height
        """
        self.validate_dim(value, "height")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter for x
        """
        self.validate_pos(value, 'x')
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y
        """
        self.validate_pos(value, 'y')
        self.__y = value

    def area(self):
        """method to return area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """method to display rectangleon the screen
        """
        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(' ', end='')
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """method to print object on screen
        """
        form = "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}"
        name = __class__.__name__
        s_x = self.__x
        s_y = self.__y
        s_w = self.__width
        s_h = self.__height
        return form.format(name, self.id, s_x, s_y, s_w, s_h)

    def update(self, *args, **kwargs):
        """method to update an instance using args or kwargs
        """
        try:
            self.id = args[0]
            self.validate_dim(args[1], "width")
            self.width = args[1]
            self.validate_dim(args[2], "height")
            self.height = args[2]
            self.validate_pos(args[3], "x")
            self.x = args[3]
            self.validate_pos(args[4], "y")
            self.y = args[4]
        except IndexError:
            pass
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.validate_dim(value)
                    self.__width = value
                elif key == "height":
                    self.validate_dim(value)
                    self.__height = value
                elif key == "x":
                    self.validate_pos(value)
                    self.__x = value
                elif key == "y":
                    self.validate_pos(value)
                    self.__y = value

    def to_dictionary(self):
        """method to get the dictionary representation of an instance
        """
        dic_rep = {}
        dic_rep["id"] = self.id
        dic_rep["width"] = self.width
        dic_rep["height"] = self.height
        dic_rep["x"] = self.x
        dic_rep["y"] = self.y
        return dic_rep
