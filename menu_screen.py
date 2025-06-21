import pygame

from button import Button
class MenuScreen:
    def __init__(self,window):
        self.window=window
        self.status=""
        self.exit_button=Button(200,400,100,50,"exit",self.exit)
        self.start_button=Button(200,300,100,50,"start",self.start)
    def handle_event(self,event):
        self.exit_button.is_clicked(event)
        self.start_button.is_clicked(event)
    def update(self):
        pass
    def draw(self):
        self.window.fill("green")
        self.exit_button.draw(self.window)
        self.start_button.draw(self.window)
    def exit(self):
        self.status="exit"
        print("Clicked")

    def start(self):
        self.status="game"