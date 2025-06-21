import pygame


class GameOver:
    def __init__(self,display,status,word):
        self.display=display
        self.status=status
        self.word=word
        self.colour="green"if self.status else "red"
        self.font = pygame.font.SysFont('arial', size=50, bold=1)
        self.word_surface=self.font.render(self.word,True,self.colour)
        self.word_rect=self.word_surface.get_rect(center=(display.get_width()/2,400))
        self.result=self.font.render("victory"if self.status else "defeat",True,self.colour)
        self.result_rect=self.result.get_rect(center=(display.get_width()/2,200))

    def draw(self):
        self.display.fill("black")
        self.display.blit(self.word_surface,self.word_rect)
        self.display.blit(self.result,self.result_rect  )

    def update(self):
        pass
    def handle_event(self,event):
        pass