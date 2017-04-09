import sys, pygame, random, time
pygame.init()
clock = pygame.time.Clock()

### INITIALIZE COLORS ###
WHITE = (255,255,255)
BLUE1 = (153,204,255)
BLUE2 = (102,178,255)
BLUE3 = (51,153,255)
BLUE4 = (0,128,255)
BLUE5 = (0,102,104)
BLUE6 = (0,0,255)
BLACK = (0,0,0)

colors = {2:BLUE6,4:BLUE5,8:BLUE4,16:BLUE3,
			32:BLUE2,64:BLUE1,128:WHITE}

def init(data):
	data.board = []
	data.message = ""
	data.font = pygame.font.Font(None,30)
	data.bigFont = pygame.font.Font(None,48)
	data.mode = "home"

def keyPressed(data,key):
	if data.mode == "home":
		if key == pygame.K_SPACE:
			data.mode = "playGame"
	if data.mode == "playGame":
		pass
		# if key == pygame.K_UP:
		# 	moveUp(data.board)
		# if key == pygame.K_DOWN:
	 #        moveDown(data.board)
	 #    if key == pygame.K_LEFT:
		# 	moveLeft(data.board)
		# if key == pygame.K_RIGHT:
		# 	moveRight(data.board)


def drawHomeMessage(data, screen):
    text = data.font.render(data.message, True, BLUE6)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                        screen.get_height() * 0.6 - text.get_height() * 2))
    text = data.bigFont.render("Welcome to Not playGame42!", True, BLUE6)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                        screen.get_height() * 0.4 - text.get_height() * 2))

def drawGameMessage(data, screen):
    text = data.font.render(data.message, True, BLUE6)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                        screen.get_height() * 0.15 - text.get_height() * 2))

def drawGameOver(data, screen):
    text = data.font.render("Game Over!", True, BLACK)
    screen.blit(text, (screen.get_width() // 2 - text.get_width() // 2,
                        screen.get_height() - text.get_height() * 2))

# def drawCircle(screen, x, y, r, color, outline):
#     pygame.draw.circle(screen, color, (x, y), r)
#     pygame.draw.circle(screen, outline, (x, y), r + 2, 5)

def redrawAll(data, screen):
	if data.mode == "home":
		data.message = "Press space to play"
		drawHomeMessage(data,screen)
	elif data.mode == "playGame":
		data.message = "Not playGame42"
		drawGameMessage(data,screen)


    # for circle in data.circles:
    #     drawCircle(screen, *circle)
    # drawMessage(data, screen)

pygame.init()
clock = pygame.time.Clock()
# create the display surface
screen = pygame.display.set_mode((600,600))

playing = True

class Struct(object): pass
data = Struct()

init(data)

while playing:
    time = clock.tick(50) # waits for the next frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        elif event.type == pygame.KEYDOWN:
            keyPressed(data, event.key)

    screen.fill(WHITE)
    redrawAll(data, screen)
    pygame.display.flip()

drawGameOver(data,screen)

pygame.quit()