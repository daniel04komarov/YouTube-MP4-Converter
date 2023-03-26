from typing import Text
import pygame as pg
import random
import sqlite3
import re
from tkinter import *


#button class
class button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pg.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(button):
        action = False

        #get mouse position
        pos = pg.mouse.get_pos()
        
        #check mouseover and clicked conditions
        if button.rect.collidepoint(pos) == True:
            if pg.mouse.get_pressed()[0] == 1 and button.clicked == False:
                button.clicked = True
                action = True

            if pg.mouse.get_pressed()[0] == 0:
                button.clicked = False

        #draw button
        screen.blit(button.image, (button.rect.x, button.rect.y))

        return action


#button text class
class buttontext():
    def __init__(self, text, text_colour, colour, width, height, font, screen, pos):

        self.clicked = False
        self.rect = pg.Rect(pos,(width,height))
        self.text = font.render(text, True, text_colour)
        self.text_rect = self.text.get_rect(center = self.rect.center)
        self.colour = colour
        self.text_colour = text_colour
        self.screen = screen


    def draw(self):

        action = False

        mouse_pos = pg.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
                #pg.display.update()

        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False
            #pg.display.update()

        pg.draw.rect(self.screen,self.colour, self.rect, border_radius = 50)
        self.screen.blit(self.text, self.text_rect)

        return action


#Input box class
class InputBox: #https://www.codegrepper.com/code-examples/python/how+to+make+a+text+input+box+python+pygame

    def __init__(self, x, y, w, h, font, colourinactive, colouractive, usertext=""):
        self.rect = pg.Rect(x, y, w, h)
        self.color = colourinactive
        self.colouractive = colouractive
        self.colourinactive = colourinactive
        self.text = usertext
        self.txt_surface = font.render(usertext, True, self.color)
        self.active = False
        self.font = font
        self.width = w


    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current colour of the input box.
            self.color = self.colouractive if self.active else self.colourinactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.active = False
                    self.color = self.colourinactive
                
                elif event.key == pg.K_LCTRL:
                    pg.scrap.init()
                    clip = pg.scrap.get(pg.SCRAP_TEXT)
                    clip2 = str(clip.decode())
                    for i in range (0, len(clip2)-1):
                        self.text = self.text + clip2[i]
                   
                elif event.key == pg.K_DELETE:
                    self.text = ""

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = self.font.render(self.text, True, self.color)
        text = self.text
        return (text)

 

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.width, self.txt_surface.get_width()+25)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+15, self.rect.y-2))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2, border_radius = 50)


#define font
def define_font(style, size):
    return pg.font.Font(style, size)

def draw_text(text, font, colour, screen, x, y):
    img = font.render(text, True, colour)
    screen.blit(img, (x, y))