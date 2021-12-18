import pygame
import sys
from time import sleep

class GameWindow:
    #<events>
    PYGAME = pygame
    QUIT = pygame.QUIT
    KEYPRESSED = pygame.KEYDOWN
    KEYRELEASED = pygame.KEYUP
    #</events>
    def __init__(self,width,height,name):
        pygame.init()
        self.screen = pygame.display.set_mode((width,height))
        pygame.display.set_caption(name)

    def tick(self,objects=()):
        pygame.display.flip()
        self.screen.fill(self.RGB)
        try:
            if len(objects)>1:
                for i in objects:
                    i.tick()
        except TypeError:
            objects.tick()

    def set_name(self,name):
        pygame.display.set_caption(str(name))

    def set_icon(self,name):
        pygame.display.set_icon(pygame.image.load(name))
    
    def set_bg_color(self,r,g,b):
        self.RGB=(r,g,b)
        self.screen.fill((r,g,b))

    def get_events(self):
        return pygame.event.get()

    def get_key(self,type,key):
        if type.key == key:
            return True
        else:
            return False

    def exit(self):
        sys.exit()
    
    def wait(self,time):
        sleep(time)

    def wait_ms(self,time):
        sleep(time/1000)

class GameObject:
        def __init__(self,screen,file):
            self.screen = screen.screen
            self.image=pygame.image.load(file)
            self.object=self.image.get_rect()
            self.screen_rect = self.screen.get_rect()
            self.object.centerx=self.screen_rect.centerx
            self.object.centery=self.screen_rect.centery
            self.bottom=self.screen_rect.bottom
            
        def tick(self):
            self.screen.blit(self.image,self.object)

        def set_cordinate(self,X,Y):
            if self.object.centerx>0 and self.object.centerx<self.screen.get_width() and self.object.centery>0 and self.object.centery<self.screen.get_height():
                self.object.centerx=X
                self.object.centery=Y
                #self.tick()
            else:
                self.object.centerx=self.screen_rect.centerx
                self.object.centery=self.screen_rect.centery

        def move(self,X,Y):
            if self.object.centerx>1 and self.object.centerx<self.screen.get_width() and self.object.centery>1 and self.object.centery<self.screen.get_height():
                self.object.centerx+=X
                self.object.centery+=Y
                #self.tick()
            else:
                self.object.centerx=self.screen_rect.centerx
                self.object.centery=self.screen_rect.centery

        def get_cordinate(self):
            return self.object.centerx,self.object.centery

        def get_cordinate_x(self):
            return self.object.centerx
        def get_cordinate_y(self):
            return self.object.centery

        def set_immage(file):
            self.image=pygame.image.load(file)