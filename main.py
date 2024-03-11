import pygame
import time
from pprint import pprint
from random import randint

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)




class Figure:
   

    # total = 1 + 2 + 4 + 4 + 2 + 2 + 4 = 19

    def _init_(self,matrix, x, y):
        self.x = x
        self.y = y
        self.matrix=matrix
        self.orientation = randint(0, len(self.matrix) - 1)  # int
        print(self.orientation)
        # self.shape = 0
        # self.color=

    def image(self):
        # it returns the matrix of the piece

        return self.matrix[self.orientation]  # add orientation as well

    def rotate(self):
        self.orientation = (self.orientation+1) % len(self.matrix)

# total = 1 + 2 + 4 + 4 + 2 + 2 + 4 = 19


class Square(Figure):

    def _init_(self,x,y):
        # list of all the orientations
        matrix = [[[0, 1, 1, 0],
                  [0, 1, 1, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]]
        super()._init_(matrix,x,y)




class Line(Figure):
    def _init_(self,x,y):
        matrix = [[[0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0],
                 [0, 0, 0, 0]],

                [[0, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 0, 0],
                 [0, 1, 0, 0]]]

        super()._init_(matrix, x, y)

class T_shape:
    def _init_(self,x,y):
        matrix=[[[0, 1, 0, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [1, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0]]]
        super()._init_(matrix, x, y)

class L_shape(Figure):
    def _init_(self,x,y):
        matrix=[[[0, 1, 0, 0],
                [0, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [0, 1, 1, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 0]],

               [[0, 0, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0]],

               [[0, 0, 0, 0],
                [0, 0, 1, 0],
                [1, 1, 1, 0],
                [0, 0, 0, 0]],
               ]

        super()._init_(matrix, x, y)


class L_shape_mirrored(Figure):
    def _init_(self,x,y):
        matrix=[[[0, 0, 1, 0],
                         [0, 0, 1, 0],
                         [0, 1, 1, 0],
                         [0, 0, 0, 0]],

                        [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 1, 1],
                         [0, 0, 0, 0]],

                        [[0, 0, 0, 0],
                         [0, 1, 1, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]],

                        [[0, 0, 0, 0],
                         [1, 1, 1, 0],
                         [0, 0, 1, 0],
                         [0, 0, 0, 0]]]

        super()._init_(matrix, x, y)


class z_shape(Figure):
    def _init_(self,x,y):
        matrix= [[[1, 1, 0, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]],  # 12

               [[0, 1, 0, 0],
                [1, 1, 0, 0],
                [1, 0, 0, 0],
                [0, 0, 0, 0]]]  # 14


        super()._init_(matrix, x, y)


class z_shape_mirrored(Figure):
    def _init_(self,x,y):
        matrix= [[[0, 1, 1, 0],
                         [1, 1, 0, 0],
                         [0, 0, 0, 0],
                         [0, 0, 0, 0]],  # 13

                        [[1, 0, 0, 0],
                         [1, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 0]]]  # 15


        super()._init_(matrix, x, y)




class Tetris:

    def _init_(self, height, width):
        # level=2
        self.score = 0
        self.state = 'start'
        self.field = []

        # grid = []
        self.height = 0
        self.width = 0
        self.x = 100
        self.y = 60
        # zoom=20
        self.shape = None
        self.width = width
        self.height = height
        print('width', width)
        print('height', height)

        # Drawing the Grid
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)
        print(len(self.field), len(self.field[0]))

    def new_figure(self):
        shape_no = randint(1,7)  # int
        if shape_no==1:
            self.shape = Square(3, 0)
            print('new figure-sqaure')
        if shape_no==2:
            self.shape = Line(3, 0)
            print('new figure-line')
        if shape_no == 3:
            self.shape = T_shape(3, 0)
            print('new figure-t_shape')
        if shape_no==4:
            self.shape = L_shape(3, 0)
            print('new figure-L-shape')
        if shape_no==5:
            self.shape = L_shape_mirrored(3, 0)
            print('new figure-L-shape-mirrored')
        if shape_no==6:
            self.shape = z_shape(3, 0)
            print('new figure-z_shape')
        if shape_no==7:
            self.shape = z_shape_mirrored(3, 0)
            print('new figure-z_shape_mirrored')

    # def adjust(self):
    #     try:
    #         test=self.field[i + self.shape.y + 1][j + self.shape.x]
    #     except IndexError as e:
    #         print("error",i + self.shape.y + 1, j + self.shape.x)
    #         if(i+self.shape.y+1)>

            # if (j + self.shape.x) >= 10:
            #     while (j + self.shape.x) >= 10:
            #         self.go_sideways(-1)
            #
            # if (j + self.shape.x) < 0:
            #     while (j + self.shape.x) < 0:
            #         self.go_sideways(1)
            #
            # if

        # 1 - touching left, movement restricted
        # 2 - touching right, movement restricted
        # 3 - touching down, block freezes
        # 4 - touching left pieces, left movement restricted
        # 5 - touching right pieces, right movement restricted
        # 6 - touching bottom pieces, block freezes

    def touches_down(self):  # return int

        is_touching = 0  # not touching
        # we just check each cell in the 4x4 matrix
        for i in range(4):
            for j in range(4):
                if self.shape.image()[i][j] == 1:  # check if the part of the piece is in cell

                    if i + self.shape.y >= self.height - 1:
                        print('touching the baseline')
                        return 3

                    try:
                        status=self.field[i + self.shape.y + 1][j + self.shape.x]
                    except IndexError as e:
                        print("error",j + self.shape.x)
                        if (j+self.shape.x) >= 10:
                            while (j+self.shape.x) >= 10:
                                self.go_sideways(-1)

                        if (j+self.shape.x) < 0:
                            while(j+self.shape.x) < 0:
                                self.go_sideways(1)

                        status=self.field[i + self.shape.y + 1][j + self.shape.x]



                    if status != 0:
                        # if self.field[i+self.shape.y ][j+self.shape.x]!=0:
                        is_touching = 6
                        print("at the bottom")
                        return is_touching

        print('returning ', is_touching)
        return is_touching

    def touches_side(self):

        is_touching = 0

        for i in range(4):
            for j in range(4):
                if self.shape.image()[i][j] == 1:  # check if the part of the piece is in cell

                    if self.width - (j + self.shape.x) == 1:
                        is_touching = 2
                        print("touching right wall ,movement restricted")
                        return is_touching
                    elif self.field[i + self.shape.y][j + self.shape.x + 1] != 0:
                        is_touching = 5
                        print("pieces at right side")
                        return is_touching

                    if (j + self.shape.x <= 0):
                        print("touching left wall, movement restricted")
                        is_touching = 1
                        return is_touching
                    elif self.field[i + self.shape.y][j + self.shape.x - 1] != 0:
                        is_touching = 4
                        print("pieces at left side")
                        return is_touching

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if self.shape.image()[i][j] == 1:
                    self.field[i + self.shape.y][j + self.shape.x] = GREEN  # ?? review the color
        pprint(self.field)
        self.break_lines()
        self.new_figure()
        time.sleep(0.2)
        if self.touches_down():
            print("the newly created pieces touches")
            game.state = 'gameover'

    # full horizontal line cleaning

    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            # check for completeness of the line i.e. no of zeros in row
            if zeros == 0:
                lines += 1
                # after cleaning the rows move the above pieces down
                for il in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[il][j] = self.field[il - 1][j]
        # self.score+=lines**2
        self.score += lines * 100

    def free_fall(self):
        while not (self.touches_down() == 6 or self.touches_down() == 3):
            self.shape.y += 1
            print('go')
        print("can't move")
        self.freeze()

    def go_down(self):
        if self.touches_down() == 3 or self.touches_down() == 6:
            self.freeze()
        else:
            self.shape.y += 1

    def go_sideways(self, dx):
        old_x = self.shape.x
        # if touching then dont change

        if (self.touches_side() == 1 or self.touches_side() == 4) and dx < 0:
            self.shape.x = old_x  # don't allow left movement

        elif (self.touches_side() == 2 or self.touches_side() == 5) and dx > 0:
            self.shape.x = old_x  # don't allow right movement

        else:
            new_x = old_x + dx
            self.shape.x = new_x

    def rotate(self):
        old_rotation = self.shape.orientation
        try:
            self.shape.rotate()
        except:
            self.shape.orientation = old_rotation
        # print(self.field)
        # if self.touches_side() or self.touches_down():
        #     self.shape.rotation = old_rotation

pygame.init()

size = (400, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption("Tertis")

game_is_on = True

clock = pygame.time.Clock()

fps = 25
game = Tetris(20, 10)
counter = 0

# pressing_down=False

while game_is_on:

    # create new figure
    if game.shape is None:
        game.new_figure()

    counter += 1

    # reset
    if counter > 100000:
        counter = 0

    if counter % (fps // 4 // 2) == 0:  # or pressing_down:  #game.level=4
        if game.state == 'start':
            game.go_down()

    # check for all the current events
    for event in pygame.event.get():

        # QUIT
        if event.type == pygame.QUIT:
            game_is_on = False

        # check all the events with keys pressed down
        if event.type == pygame.KEYDOWN:

            # rotate
            if event.key == pygame.K_UP:
                game.rotate()

            # if event.key==pygame.K_DOWN:
            #     pressing_down=True

            if event.key == pygame.K_LEFT:
                game.go_sideways(-1)

            if event.key == pygame.K_RIGHT:
                game.go_sideways(1)

            if event.key == pygame.K_SPACE:
                game.free_fall()

            if event.key == pygame.K_ESCAPE:
                game._init_(20, 10)

        # if event.type == pygame.KEYUP:
        #     if event.key ==pygame.K_DOWN:
        #         pressing_down=False

    # draw the screen
    screen.fill(WHITE)

    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + 20 * j, game.y + 20 * i, 20, 20], 1)  # draw the gridlines
            if game.field[i][j] != 0:
                pygame.draw.rect(screen, (255, 0, 0),
                                 [game.x + 20 * j + 1, game.y + 20 * i + 1, 20 - 2, 20 - 1])  # red color

    if game.shape is not None:
        for i in range(4):
            for j in range(4):
                if game.shape.image()[i][j] != 0:
                    pygame.draw.rect(screen, GREEN, [game.x + 20 * (j + game.shape.x) + 1,
                                                     game.y + 20 * (i + game.shape.y) + 1, 20 - 2, 20 - 2])

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render("Score: " + str(game.score), True, BLACK)
    text_game_over = font.render("GAME OVER", True, (255, 125, 0))
    text_game_over1 = font.render("Press ESC", True, (255, 215, 0))

    screen.blit(text, [0, 0])
    if game.state == 'gameover':
        screen.blit(text_game_over, [20, 200])
        screen.blit(text_game_over1, [25, 265])

    pygame.display.flip()
    time.sleep(0.2)
    clock.tick(fps)

pygame.quit()
