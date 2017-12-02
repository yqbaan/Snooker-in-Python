import pygame
from game import Game
from score import Score
from settings import *
def main():
    pygame.init()
    the_game = Game()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    running = True

    while running:
        the_game.white_ball_grab()
        for event in pygame.event.get():
            print(pygame.event.get())
            if event.type == pygame.QUIT:
                running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                running = False
        the_game.painter.game_surface.fill(BACKGROUND_COLOR)
        the_game.painter.game_surface.blit(the_game.table, TABLE_POS)
        the_game.painter.game_surface.blit(the_game.score.score_board, SCORE)
        the_game.game_handler()
        the_game.balls_handler()
        screen.blit(the_game.painter.game_surface, (0, 0))
        pygame.display.flip()
        the_game.clock.tick(100)
    pygame.quit()

if __name__ == '__main__':
    main()
    print("Game closed")