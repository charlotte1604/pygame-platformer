import pygame
import requests
from button import Button


def check_word(word):
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word).json()
    if isinstance(response, list):
        return True
    return False


def check_letters(word, hidden_word):
    green_letters = []  # correct spot
    yellow_letters = []  # just correct letter

    for index, letter in enumerate(word):
        for i2, l2 in enumerate(hidden_word):
            if letter == l2 and index == i2:
                green_letters.append([index, letter])
            elif letter == l2 and index != i2:
                yellow_letters.append([index, letter])

    return (green_letters, yellow_letters)


class Game:
    def __init__(self, window, word):
        self.window = window
        self.status = ""
        self.words = [["" for i in range(5)] for i in range(6)]
        self.current_row = 0
        self.current_letter = 0
        self.pressedkey = ""
        self.input_word = ""
        self.font = pygame.font.SysFont('arial', size=25, bold=1)
        self.check_Button = Button(600, 50, 100, 50, "check", self.check)
        self.hidden_word = word
        self.green = []
        self.yellow = []

    def handle_event(self, event):
        self.check_Button.is_clicked(event)
        if event.type == pygame.KEYDOWN:
            if event.unicode in "qwertyuiopasdfghjklzxcvbnm":
                self.pressedkey = event.unicode
                if len(self.input_word) < 5:

                    self.input_word += event.unicode
                    self.words[self.current_row][self.current_letter] = self.pressedkey
                    if self.current_letter < 4:
                        self.current_letter += 1
            elif event.key == pygame.K_BACKSPACE:
                if self.input_word:
                    if len(self.input_word) == 1:
                        self.input_word = ''
                    self.input_word = self.input_word[:-1]
                    self.words[self.current_row][self.current_letter] = ""
                    self.current_letter -= 1
                    if self.current_letter < 0:
                        self.current_letter = 0
            elif event.key == pygame.K_RETURN:
                self.check()


    def update(self):
        pass

    def check(self):
        print("blablabla")
        if self.input_word:
            if self.input_word == self.hidden_word:
                self.status = "win"
            elif self.current_row == 5:
                self.status = "lose"
            elif check_word(self.input_word):

                self.check_Button.colour = "green"
                self.green.append(check_letters(self.input_word, self.hidden_word)[0])
                self.yellow.append(check_letters(self.input_word, self.hidden_word)[1])
                self.current_row += 1
                self.input_word = ""
                self.current_letter = 0
                print(self.green, self.yellow)
            else:
                self.check_Button.colour = "red"

    def draw(self):
        self.window.fill("black")
        self.check_Button.draw(self.window)
        startx = 50
        starty = 50
        for l1 in self.words:
            for l2 in l1:
                pygame.draw.rect(self.window, "white", (startx, starty, 50, 50), 2)
                if l2:
                    letter = self.font.render(l2.title(), True, "white")
                    self.window.blit(letter, (startx + 20, starty + 20))
                startx += 70

            startx = 50
            starty += 70

        for row, word in enumerate(self.green):
            if word:

                startx = 50 + word[0][0] * 70
                starty = 50 + row * 70
                pygame.draw.rect(self.window, 'green', (startx, starty, 50, 50), 2)

        for row, word in enumerate(self.yellow):
            if word:

                startx = 50 + word[0][0] * 70
                starty = 50 + row * 70
                pygame.draw.rect(self.window, 'yellow', (startx, starty, 50, 50), 2)
