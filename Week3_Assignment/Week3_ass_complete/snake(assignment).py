import pygame, sys, time, random

#initial game variables

# Window size
frame_size_x = 720
frame_size_y = 480

#Parameters for Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
change_to = direction

#Parameters for food
food_pos = [0,0]
food_spawn = False

SIZE = 40
BACKGROUND_COLOR = (110, 110, 5)

score = 0


# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
surface = pygame.display.set_mode((frame_size_x, frame_size_y))



# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()




def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.move_left()

            elif event.key == pygame.K_RIGHT:
                snake.move_right()

            elif event.key == pygame.K_UP:
                snake.move_up()

            elif event.key == pygame.K_DOWN:
                snake.move_down()

        elif event.type == pygame.QUIT:
            sys.exit()



#def update_snake():
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction
    







    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions 
    # since we have not made snake and food as a specific sprite or surface.
    





    # End the game if the snake collides with the wall or with itself. 
    






#def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    




def show_score(pos, color, font, size):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    font = pygame.font.SysFont(font,size)
    score_display = font.render(f"Score: {score}",True,color)
    surface.blit(score_display,pos)


#show_score((850,10), (200,200,200), 'arial', 30)



#def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """







def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    surface.fill(BACKGROUND_COLOR)
    font = pygame.font.SysFont('arial', 30)
    line1 = font.render(f"Game is over! Your score is {score}", True, (255, 255, 255))
    surface.blit(line1, (200, 300))

    pygame.display.flip()

    time.sleep(3)
    sys.exit(0)


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/apple.jpg").convert()
        self.x = 120
        self.y = 120

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE



class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("resources/block.jpg").convert()
        self.direction = 'down'

        self.length = 2
        self.x = [80,40]
        self.y = [40,40]

    def move_left(self):
        if self.direction != 'right':
            self.direction = 'left'

    def move_right(self):
        if self.direction != 'left':
            self.direction = 'right'

    def move_up(self):
        if self.direction != 'down':
            self.direction = 'up'

    def move_down(self):
        if self.direction != 'up':
            self.direction = 'down'

    def walk(self):
        # update body
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        # update head
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'down':
            self.y[0] += SIZE

        self.draw()

    def draw(self):
        self.parent_screen.fill(BACKGROUND_COLOR)

        for i in range(self.length):
            self.parent_screen.blit(self.image, (self.x[i], self.y[i]))
        pygame.display.flip()

    def increase_length(self):
        self.length += 1
        self.x.append(0)
        self.y.append(0)


def is_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + SIZE:
        if y1 >= y2 and y1 < y2 + SIZE:
            return True
    return False


def collisionWithWall(x1, y1):
    screen_rect = surface.get_rect()
    xr = screen_rect.right
    xl = screen_rect.left
    yu = screen_rect.top
    yd = screen_rect.bottom

    if x1 >= xr:
        return True
    if x1 <= xl:
        return True
    if y1 <= yu:
        return True
    if y1 >= yd:
        return True

    return False


pygame.init()
pygame.display.set_caption("Codebasics Snake And Apple Game")
surface = pygame.display.set_mode((1000, 800))
snake = Snake(surface)
snake.draw()
apple = Apple(surface)
apple.draw()



# Main loop
while True:
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    snake.walk()
    apple.draw()
    score = snake.length-1
    show_score((850,10), (200,200,200), 'arial', 30)
    pygame.display.flip()
    if is_collision(snake.x[0], snake.y[0], apple.x, apple.y):
        snake.increase_length()
        apple.move()
    for i in range(2, snake.length):
        if is_collision(snake.x[0], snake.y[0], snake.x[i], snake.y[i]):
            game_over()
    if collisionWithWall(snake.x[0], snake.y[0]):
        game_over()
    

    # To set the speed of the screen
    fps_controller.tick(5)
