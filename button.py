import pygame

class Button:
    def __init__(self,x,y,width,height,text,action,colour="red"):
        self.rect=pygame.Rect(x,y,width,height)
        self.text=text
        self.colour=colour
        self.action=action
        self.font=pygame.font.SysFont("arial",20)
        self.text_surface=self.font.render(self.text,True,"white")
        self.text_rect=self.text_surface.get_rect(center=self.rect.center)

    def draw(self,window):
        pygame.draw.rect(window,self.colour,self.rect)
        window.blit(self.text_surface,self.text_rect)

    def is_clicked(self,event):
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()