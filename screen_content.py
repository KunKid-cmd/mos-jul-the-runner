from turtle import Screen, Turtle
from content import Player, Map, Timer


class Screen_display:
    """
    create turtle screen
    """
    def __init__(self, name, width, height, background, title):
        self.name = name
        self.width = width
        self.height = height
        self.background = background
        self.title = title
        self.turtle_sc = Screen()
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.list_set = []
        self.turtle_sc.tracer(0)  # screen delay

    @property
    def width(self):
        """get or set value of the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        check if width is int or float and width is greater than zero or not
        """
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if width <= 0:
            raise ValueError("width must be greater than zero")
        self.__width = width

    @property
    def height(self):
        """get or set value of the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        check height is int or float and height is greater than zero or not
        """
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if height <= 0:
            raise ValueError("height must be greater than zero")
        self.__height = height

    @property
    def background(self):
        """get or set background"""
        return self.__background

    @background.setter
    def background(self, background):
        """ check background is str or not """
        if not isinstance(background, str):
            raise TypeError("background must be a string")
        self.__background = background

    @property
    def title(self):
        """get or set background"""
        return self.__title

    @title.setter
    def title(self, name_title):
        """ check background is str or not """
        if not isinstance(name_title, str):
            raise TypeError("background must be a string")
        self.__title = name_title

    @property
    def name(self):
        """get or set name"""
        return self.__name

    @name.setter
    def name(self, new):
        """ check name is str or not """
        if not isinstance(new, str):
            raise TypeError("name must be a string")
        self.__name = new

    def add_set(self, new):
        """
        append turtle to self list_set
        """
        self.list_set.append(new)

    def clear_set(self):
        """clear list_set"""
        self.list_set = []

    def add_shape(self, new):
        """ add new model for turtle """
        self.turtle_sc.register_shape(new)

    def create_screen(self):
        """ create program screen """
        self.add_shape('ch_right.gif')
        play = Player('ch_right.gif', 'white', -400, -230)
        play.set()
        play.control()
        self.turtle.speed(0)
        self.turtle_sc.bgpic(self.background)
        self.turtle_sc.bgcolor("black")
        self.turtle_sc.setup(self.height, self.width)
        self.turtle_sc.title(self.title)
        score = Timer(play.get_stage, self.name)

        self.add_set(Map('yellow', 400, 250, 5, 5))
        self.add_set(Map('brown', 0, -280, 1000, 4))
        self.add_set(Map('brown', 0, 60, 10, 1))
        self.add_set(Map('brown', 280, 0, 9, 1))
        self.add_set(Map('brown', -350, 120, 12, 1))
        self.add_set(Map('brown', -300, 200, 8, 1))
        self.add_set(Map('brown', 30, 200, 9, 1))
        self.add_set(Map('brown', 400, 200, 12, 1))
        self.add_set(Map('brown', -300, -200, 5, 5))
        self.add_set(Map('brown', -200, -150, 5, 9))
        self.add_set(Map('brown', 0, -20, 1, 7))
        self.add_set(Map('brown', 330, -100, 1, 10))

        # lava
        self.add_set(Map('blue', 0, -280, 8, 4))
        self.add_set(Map('blue', 230, -280, 8, 4))
        self.add_set(Map('blue', 280, 5, 6, 1))
        self.add_set(Map('blue', 0, 65, 6, 1))
        self.add_set(Map('blue', -300, 205, 6, 1))
        self.add_set(Map('blue', 30, 205, 6, 1))

        # spike
        self.add_set(Map('blue', 350, -100, 1, 1))
        self.add_set(Map('blue', 430, -150, 1, 1))
        self.add_set(Map('blue', 430, -50, 1, 1))
        self.add_set(Map('blue', 430, 50, 1, 1))
        self.add_set(Map('blue', -300, 140, 1, 1))
        self.add_set(Map('blue', -370, 180, 1, 1))

        for slt in self.list_set:
            slt.area()

        while play.on:
            self.turtle_sc.update()
            play.movement()
            play.map1()

            if play.get_stage == 2:
                score.ups()
                self.turtle_sc.clear()
                self.clear_set()

                self.add_shape('ch_right.gif')
                play = Player('ch_right.gif', 'white', 400, -230)
                play.set()
                play.control()
                self.turtle.speed(0)
                self.turtle_sc.bgpic('background1.png')
                self.turtle_sc.bgcolor("black")

                self.add_set(Map('black', 350, -280, 10, 4))
                self.add_set(Map('black', -380, -280, 10, 4))
                self.add_set(Map('black', -380, -280, 3, 4))
                self.add_set(Map('black', -80, -280, 3, 4))
                self.add_set(Map('black', 260, -180, 1, 7))
                self.add_set(Map('black', 260, 80, 1, 7))
                self.add_set(Map('red', 350, 130, 1, 5))
                self.add_set(Map('red', 350, -80, 1, 5))
                self.add_set(Map('black', 100, -50, 1, 15))
                self.add_set(Map('black', -50, 100, 1, 20))
                self.add_set(Map('black', 230, -100, 4, 1))
                self.add_set(Map('black', 230, 150, 4, 1))
                self.add_set(Map('red', 400, -100, 4, 1))
                self.add_set(Map('red', 400, 130, 4, 1))

                # wall slab left
                self.add_set(Map('red', -400, -40, 10, 1))
                # left
                self.add_set(Map('black', -300, -120, 4, 1))
                self.add_set(Map('black', -200, -50, 4, 1))
                self.add_set(Map('black', -200, 150, 1, 4))
                self.add_set(Map('black', -100, 180, 4, 1))
                # lwall
                self.add_set(Map('black', -300, 50, 1, 10))
                # box FINAL
                self.add_set(Map('yellow', -380, 20, 3, 3))
                # lava wall
                self.add_set(Map('red', -130, 90, 1, 4))

                for slt in self.list_set:
                    slt.area()

                while play.on:
                    play.map2()
                    self.turtle_sc.update()
                    play.movement()

        score.write()
        self.turtle_sc.bye()
