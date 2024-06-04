import pygame
import player
import translate_text as tt

pygame.init()
pygame.display.set_caption("hiragana game")
screen_size = (720, 900)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True
pygame.font.init()
my_font = pygame.font.SysFont('BIZ UDGothic', 30)

player_image = pygame.image.load("kagami.png")
lebron_image = pygame.image.load("lebron.png")
ammo_image = pygame.image.load("peggle.png")

position = (screen.get_rect().centerx, 700)

player = player.Player(player_image, (611, 611), position, player_image)

typing_text = ""                   


while running:
    for event in pygame.event.get():
        #if hit the x
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                typing_text = typing_text[:-1]
            else:
                typing_text += event.unicode
                typing_text = tt.translateSentence(typing_text)
                # print("typing text:", typing_text)
                                                      
    text_surface = my_font.render(typing_text, False, (0, 0, 0))
    
    # wipe previous frame
    screen.fill("pink")

    player.rotate()

    # player
    screen.blit(player.sprite, player.rect)
    screen.blit(text_surface, (100, 100))


    # draw
    pygame.display.flip()
