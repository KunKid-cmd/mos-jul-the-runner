import time
from turtle import Turtle, Screen
from score import Score


class Map:
    """
    create map by turtle change size
    """
    def __init__(self, color, x=0, y=0, wid=0, high=0):
        """
        get all ingredient to make create map by change size of turtle
        """
        self.turtle = Turtle()
        self.x = x
        self.y = y
        self.turtle.penup()
        self.high = high
        self.wid = wid
        self.color = color

    @property
    def color(self):
        """ get or set color """
        return self.__color

    @color.setter
    def color(self, new_color):
        """check if color is str or not"""
        if not isinstance(new_color, str):
            raise TypeError("color must be a string")
        self.__color = new_color

    @property
    def x(self):
        """ get or set x """
        return self.__x

    @x.setter
    def x(self, new):
        """check if x is int or float or not"""
        if not isinstance(new, (int, float)):
            raise TypeError("The x attribute must be a number")
        self.__x = new

    @property
    def high(self):
        """ get or set high """
        return self.__high

    @high.setter
    def high(self, new):
        """check if high is int or float or not"""
        if not isinstance(new, (int, float)):
            raise TypeError("The high attribute must be a number")
        self.__high = new

    @property
    def wid(self):
        """ get or set wid """
        return self.__wid

    @wid.setter
    def wid(self, new):
        """check if wid is int or float or not"""
        if not isinstance(new, (int, float)):
            raise TypeError("The wid attribute must be a number")
        self.__wid = new

    @property
    def __y(self):
        """ get or set y """
        return self.__y

    @__y.setter
    def __y(self, new):
        """check if y is int or float or not"""
        if not isinstance(new, (int, float)):
            raise TypeError("The y attribute must be a number")
        self.__y = new

    def area(self):
        """
        create turtle to make map
        """
        self.turtle.color(self.color)
        self.turtle.speed(0)
        self.turtle.shape('square')
        self.turtle.penup()
        self.turtle.goto(self.x, self.y)
        self.turtle.shapesize(stretch_len=self.wid, stretch_wid=self.high)


class Timer:
    """set time start"""
    def __init__(self, floor, player_name):
        """start count time to collect in score.py and write in json after"""
        self.start_time = time.time()
        self.floor = floor
        self.player_name = player_name

    @property
    def floor(self):
        """ get or set floor"""
        return self.__floor

    @floor.setter
    def floor(self, new):
        """check if floor is int or not"""
        if not isinstance(new, int):
            raise TypeError("The floor attribute must be int")
        self.__floor = new

    @property
    def player_name(self):
        """ get or set player_name"""
        return self.__player_name

    @player_name.setter
    def player_name(self, new):
        """check if player_name is string or not"""
        if not isinstance(new, str):
            raise TypeError("player_name must be a string")
        self.__player_name = new

    def ups(self):
        """
        increase floor by 1
        """
        self.floor += 1

    def write(self):
        """
        get final time and write file in user_data as json file
        by (name, floor and time)
        """
        stop = time.time()  # stop time
        score = stop - self.start_time
        data = Score('user_data')
        data.insert(self.player_name, self.floor, score)


class Player:
    """create player and movement"""
    def __init__(self, shape, color, location_x=0, location_y=0):
        """
        create player character and movement
        """
        self.turtle = Turtle()
        self.screen = Screen()
        self.shape = shape
        self.turtle.speed(0)
        self.location_x = location_x
        self.location_y = location_y
        self.turtle.penup()
        self.color = color
        self.status = 'ready'
        self.position_x = 0
        self.position_y = 0
        self.gravity = -0.125
        self.speed = 5
        self.screen.register_shape('ch_left.gif')
        self.screen.register_shape('ch_right.gif')
        self.stage = 1
        self.on = True

    @property
    def location_x(self):
        """ get or set location in x_axis"""
        return self.__location_x

    @location_x.setter
    def location_x(self, new):
        """check if x is int ,float or not """
        if not isinstance(new, (int, float)):
            raise TypeError("The x attribute must be a number")
        self.__location_x = new

    @property
    def location_y(self):
        """ get or set location in y_axis"""
        return self.__location_y

    @location_y.setter
    def location_y(self, new):
        """check if y is int ,float or not"""
        if not isinstance(new, (int, float)):
            raise TypeError("The y attribute must be a number")
        self.__location_y = new

    @property
    def shape(self):
        """ get or set shape """
        return self.__shape

    @shape.setter
    def shape(self, shape):
        """check if shape is string or not"""
        if not isinstance(shape, str):
            raise TypeError("shape must be a string")
        self.__shape = shape

    @property
    def color(self):
        """ get or set color """
        return self.__color

    @color.setter
    def color(self, new_color):
        """check if color is string or not"""
        if not isinstance(new_color, str):
            raise TypeError("color must be a string")
        self.__color = new_color

    @property
    def get_stage(self):
        """return player stage"""
        return self.stage

    def jump(self):
        """
        check that player status is ready and set position in y-axis +5
        """
        if self.status == "ready":
            self.position_y = 5
            Player.state = "jumping"

    def left(self):
        """
        set player skin to left side and set position in x-axis to go left
        """
        self.turtle.shape('ch_left.gif')
        self.position_x = -1.2

    def right(self):
        """
        set player skin to right side and set position in x-axis to go right
        """
        self.turtle.shape('ch_right.gif')
        self.position_x = 1.2

    def stop(self):
        """
        set player movement position in x-axis to 0
        """
        self.position_x = 0

    def quit(self):
        """
        return false to the loop in screen_content
        """
        self.on = False

    def control(self):
        """
        set movement key and used function
        """
        self.screen.listen()
        self.screen.onkeypress(self.jump, 'w')
        self.screen.onkeypress(self.right, 'd')
        self.screen.onkeypress(self.left, 'a')
        self.screen.onkeypress(self.stop, 's')
        self.screen.onkey(self.quit, "q")

    def set(self):
        """set turtle location color and shape"""
        self.turtle.goto(self.location_x, self.location_y)
        self.turtle.color(self.color)
        self.turtle.shape(self.shape)

    def movement(self):
        """
        add player position + gravity and make all movement work
        """
        self.position_y += self.gravity
        self.screen.tracer(0)

        # (jump) add player position in y-axis and set the position
        y = self.turtle.ycor()
        y += self.position_y
        self.turtle.sety(y)
        self.status = "jumping"

        # (left and right) add player position in x-axis and set the position
        x = self.turtle.xcor()
        x += self.position_x
        self.turtle.setx(x)
        self.status = "jumping"

        # (stop) player position in x-axis = 0 and set the position
        x = self.turtle.xcor()
        x += self.position_x
        self.turtle.setx(x)
        self.status = "jumping"

    def map1(self):
        """set map and obstruct location for stage 1"""
        if self.turtle.ycor() < -230:
            self.turtle.sety(-230)
            self.status = 'ready'

        if self.turtle.xcor() < -440:
            self.turtle.setx(-440)
            self.status = 'ready'

        if self.turtle.xcor() > 430:
            self.turtle.setx(430)
            self.status = 'ready'

        # slab1
        if 60 > self.turtle.ycor() > 40 and 70 > self.turtle.xcor() > -100:
            self.turtle.sety(40)

        if 80 > self.turtle.ycor() > 70 and 100 > self.turtle.xcor() > -100:
            self.turtle.sety(80)
            self.status = 'ready'

        # slab2
        if 0 > self.turtle.ycor() > -20 and 370 > self.turtle.xcor() > 190:
            self.turtle.sety(-20)

        if 20 > self.turtle.ycor() > 5 and 370 > self.turtle.xcor() > 190:
            self.turtle.sety(20)
            self.status = 'ready'

        # slab3
        if 120 > self.turtle.ycor() > 100 and -230 > self.turtle.xcor() > -470:
            self.turtle.sety(100)

        if 140 > self.turtle.ycor() > 125 and -230 > self.turtle.xcor() > -470:
            self.turtle.sety(140)
            self.status = 'ready'

        # slab4
        if 200 > self.turtle.ycor() > 180 and -220 > self.turtle.xcor() > -380:
            self.turtle.sety(178)

        if 220 > self.turtle.ycor() > 205 and -220 > self.turtle.xcor() > -380:
            self.turtle.sety(220)
            self.status = 'ready'

        # slab5
        if 200 > self.turtle.ycor() > 180 and 120 > self.turtle.xcor() > -60:
            self.turtle.sety(178)

        if 220 > self.turtle.ycor() > 205 and 120 > self.turtle.xcor() > -60:
            self.turtle.sety(220)
            self.status = 'ready'

        # slab6
        if 200 > self.turtle.ycor() > 180 and 520 > self.turtle.xcor() > 280:
            self.turtle.sety(178)

        if 220 > self.turtle.ycor() > 205 and 520 > self.turtle.xcor() > 280:
            self.turtle.sety(220)
            self.status = 'ready'

        # wall1
        if 40 >= self.turtle.ycor() >= -80 and 20 > self.turtle.xcor() > - 20:
            self.turtle.setx(-20)
            self.status = 'ready'

        # box1
        if self.turtle.ycor() < -160 and -250 > self.turtle.xcor() > -360:
            self.turtle.setx(-360)
            self.status = 'ready'

        if self.turtle.ycor() < -140 and -250 > self.turtle.xcor() > -360:
            self.turtle.sety(-140)
            self.status = 'ready'

        # box2
        if self.turtle.ycor() < -70 and -150 > self.turtle.xcor() > -260:
            self.turtle.setx(-260)
            self.status = 'ready'

        if self.turtle.ycor() < -50 and -150 > self.turtle.xcor() > -260:
            self.turtle.sety(-50)
            self.status = 'ready'

        if self.turtle.ycor() < -70 and -140 > self.turtle.xcor() > -260:
            self.turtle.setx(-140)
            self.status = 'ready'

        # wall2
        if 0 >= self.turtle.ycor() >= -200 and 350 > self.turtle.xcor() > 320:
            self.turtle.setx(350)
            self.status = 'ready'

        if 0 >= self.turtle.ycor() >= -200 and 330 > self.turtle.xcor() > 310:
            self.turtle.setx(310)
            self.status = 'ready'

        # lava 1
        if self.turtle.ycor() < -229 and 85 > self.turtle.xcor() > -80:
            self.quit()

        # lava 2
        if self.turtle.ycor() < -229 and 315 > self.turtle.xcor() > 150:
            self.quit()

        # lava 3
        if 25 > self.turtle.ycor() > 5 and 345 > self.turtle.xcor() > 220:
            self.quit()

        # lava 4
        if 90 > self.turtle.ycor() > 70 and 0 + 65 > self.turtle.xcor() \
                > 0 - 60:
            self.quit()

        # lava 5
        if 225 > self.turtle.ycor() > 205 and -300 + 65 > self.turtle.xcor() \
                > -300 - 60:
            self.quit()

        # lava 6
        if 225 > self.turtle.ycor() > 205 and 30 + 65 > self.turtle.xcor() \
                > 30 - 60:
            self.quit()

        # spike 1
        if -100 + 20 > self.turtle.ycor() > -100 - 20 and 350 + 20 > \
                self.turtle.xcor() > 350 - 20:
            self.quit()

        # spike 2
        if -150 + 20 > self.turtle.ycor() > -150 - 20 and 430 + 20 > \
                self.turtle.xcor() > 430 - 20:
            self.quit()

        # spike 3
        if -50 + 20 > self.turtle.ycor() > -50 - 20 and 430 + 20 > \
                self.turtle.xcor() > 430 - 20:
            self.quit()

        # spike 4
        if 50 + 20 > self.turtle.ycor() > 50 - 20 and 430 + 20 > \
                self.turtle.xcor() > 430 - 20:
            self.quit()

        # spike 5
        if 140 + 20 > self.turtle.ycor() > 140 - 20 and -300 + 20 > \
                self.turtle.xcor() > -300 - 20:
            self.quit()

        # spike 6
        if 180 + 20 > self.turtle.ycor() > 180 - 20 and -370 + 20 > \
                self.turtle.xcor() > -370 - 20:
            self.quit()

        # end map1
        if 300 > self.turtle.ycor() > 210 and 550 > self.turtle.xcor() > 350:
            self.stage += 1

    def map2(self):
        """set map and obstruct location for stage 2"""

        if self.turtle.xcor() < -440:
            self.turtle.setx(-440)
            self.status = 'ready'

        if self.turtle.xcor() > 430:
            self.turtle.setx(430)
            self.status = 'ready'

        # ground mid
        if self.turtle.ycor() < -230 and -80 + 30 > self.turtle.xcor() \
                > -80 - 30:
            self.turtle.sety(-230)
            self.status = 'ready'

        # fall
        if self.turtle.ycor() < -250:
            self.quit()

        # ground right
        if self.turtle.ycor() < -230 and 350 + 100 > self.turtle.xcor() \
                > 350 - 100:
            self.turtle.sety(-230)
            self.status = 'ready'

        # ground left
        if self.turtle.ycor() < -230 and -380 + 100 > self.turtle.xcor() \
                > -380 - 100:
            self.turtle.sety(-230)
            self.status = 'ready'

        # wall
        if 100 >= self.turtle.ycor() >= -200 and 100 + 20 > self.turtle.xcor()\
                > 100 - 0:
            self.turtle.setx(100 + 20)
            # self.status = 'ready'

        if 100 >= self.turtle.ycor() >= -200 and 100 + 0 > self.turtle.xcor() \
                > 100 - 20:
            self.turtle.setx(100 - 20)
            self.status = 'ready'

        # mid_wall2
        if 500 >= self.turtle.ycor() >= -90 and -50 + 20 > self.turtle.xcor() \
                > -50 - 0:
            self.turtle.setx(-50 + 20)
            self.status = 'ready'

        if 500 >= self.turtle.ycor() >= -90 and -50 + 0 > self.turtle.xcor() \
                > -50 - 20:
            self.turtle.setx(-50 - 20)
            self.status = 'ready'

        # wall 1
        if -180 + 70 >= self.turtle.ycor() >= -180 - 80 and 260 + 20 > \
                self.turtle.xcor() > 260 - 20:
            self.turtle.setx(260 + 20)
            self.status = 'ready'

        # wall 2
        if 150 >= self.turtle.ycor() >= 10 and 260 + 20 > self.turtle.xcor() \
                > 260 - 20:
            self.turtle.setx(260 + 20)
            self.status = 'ready'

        # slab 1
        if -80 > self.turtle.ycor() > -100 and 230 + 40 > self.turtle.xcor() \
                > 230 - 40:
            self.turtle.sety(-80)
            self.status = 'ready'

        # slab 2
        if 170 > self.turtle.ycor() > 150 and 230 + 40 > self.turtle.xcor() \
                > 230 - 40:
            self.turtle.sety(170)
            self.status = 'ready'

        # sl_lava1
        if -80 > self.turtle.ycor() > -120 and 400 + 40 > self.turtle.xcor() \
                > 400 - 40:
            self.quit()

        # sl_lava2
        if -80 > self.turtle.ycor() > -120 and 400 + 40 > self.turtle.xcor() \
                > 400 - 40:
            self.quit()

        # lava1 wall
        if -20 >= self.turtle.ycor() >= -150 and 350 + 20 > self.turtle.xcor()\
                > 350 - 20:
            self.quit()

        # lava2 wall
        if 190 >= self.turtle.ycor() >= 70 and 350 + 20 > self.turtle.xcor() \
                > 350 - 20:
            self.quit()

        # left 1
        if -100 > self.turtle.ycor() > -120 and -300 + 40 > self.turtle.xcor()\
                > -300 - 40:
            self.turtle.sety(-100)
            self.status = 'ready'

        if -120 > self.turtle.ycor() > -140 and -300 + 40 > self.turtle.xcor()\
                > -300 - 40:
            self.turtle.sety(-140)
            self.status = 'ready'

        #     left 2
        if -30 > self.turtle.ycor() > -50 and -200 + 40 > self.turtle.xcor() \
                > -200 - 40:
            self.turtle.sety(-30)
            self.status = 'ready'
        #
        if -50 > self.turtle.ycor() > -70 and -200 + 40 > self.turtle.xcor() \
                > -200 - 40:
            self.turtle.sety(-70)
            self.status = 'ready'

        # left 3 (wall)

        if 190 >= self.turtle.ycor() >= 100 and -200 + 20 > self.turtle.xcor()\
                > -200 - 10:
            self.turtle.setx(-200 + 20)
            self.status = 'ready'

        if 200 >= self.turtle.ycor() >= 100 and -200 + 0 > self.turtle.xcor()\
                > -200 - 20:
            self.turtle.setx(-200 - 20)
            self.status = 'ready'

        #     left 4
        if 200 > self.turtle.ycor() > 180 and -100 + 40 > self.turtle.xcor() \
                > -100 - 40:
            self.turtle.sety(200)
            self.status = 'ready'
        #
        if 179 > self.turtle.ycor() > 160 and -100 + 40 > self.turtle.xcor() \
                > -100 - 40:
            self.turtle.sety(160)
            self.status = 'ready'

        #     wall left
        if 150 >= self.turtle.ycor() >= -50 and -300 + 20 > self.turtle.xcor()\
                > -300 - 10:
            self.turtle.setx(-300 + 20)
            # self.status = 'ready'

        if 150 >= self.turtle.ycor() >= -50 and -300 + 0 > self.turtle.xcor()\
                > -300 - 20:
            self.turtle.setx(-300 - 20)
            self.status = 'ready'

        # wall slab left
        if -20 > self.turtle.ycor() > -60 and -400 + 100 > self.turtle.xcor()\
                > -400 - 100:
            self.quit()

        # final box
        if 50 > self.turtle.ycor() > -10 and -380 + 50 > self.turtle.xcor() \
                > -380 - 50:
            self.quit()
            print(
                '===========================================================')
            print('!!you reach the final WoW!!')
            print(
                '===========================================================')
            time.sleep(3)

        # wall slab left
        if 90 + 40 >= self.turtle.ycor() >= 90 - 40 and -130 + 20 > \
                self.turtle.xcor() > -130 - 20:
            self.quit()
