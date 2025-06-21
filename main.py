import pygame
import json
import random
from menu_screen import MenuScreen
from game_screen import Game
from game_over import GameOver


with open('words.json') as file:
    all_words = json.load(file)

def main():
    pygame.init()
    width=800
    height=600
    fps=60

    window=pygame.display.set_mode((width,height))
    pygame.display.set_caption("wordle")
    clock=pygame.time.Clock()

    current_mode=MenuScreen(window)
    run=True
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            current_mode.handle_event(event)
        current_mode.update()
        current_mode.draw()
        if current_mode.status=="exit":
            run=False
        elif current_mode.status=="game":
            word=random.choice(all_words['words'])
            current_mode=Game(window,word)
        elif current_mode.status=="win":
            current_mode=GameOver(window,True,word)
        elif current_mode.status=="lose":
            current_mode=GameOver(window,False,word)
        pygame.display.flip()
    pygame.quit()

if __name__=="__main__":
    main()