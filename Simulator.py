import pygame
from pygame.locals import *
import DataTypes

class Simulator(object):
    def __init__(self):
        pygame.init()
        self.width, self.height = 400, 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Simulator')

        self.background = pygame.Surface(self.screen.get_size())
        self.background.convert()
        self.background.fill((255, 255, 255))

        self.clock = pygame.time.Clock()

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        self.sensor = FishSensorSimulator(self)
        self.driver = MotorDriverSimulator(self)

    def redraw(self):
        self.clock.tick(60)

        self.screen.blit(self.background, (0, 0))

        self.driver.redraw(self.screen)
        self.sensor.redraw(self.screen)

        pygame.display.flip()


class FishSensorSimulator(object):
    def __init__(self, sim):
        self.sim = sim
        self.pos_x, self.pos_y = 0.0, 0.0
        self.cx, self.cy = sim.width/2, sim.height/2
        self.rect_width, self.rect_height = 5, 5
        self.display_scale = 1
        self.tank_width, self.tank_height = 50, 25
        pygame.key.set_repeat(100, 10)

    def poll(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT and self.pos_x != -self.tank_width/2:
                    self.pos_x -= 1
                if event.key == K_RIGHT and self.pos_x != self.tank_width/2:
                    self.pos_x += 1

        self.sim.redraw()
        return DataTypes.FishPosition(x=self.pos_x / (self.tank_width/2),
                                      y=self.pos_y / (self.tank_height/2))

    def redraw(self, surf):
        tank_rect = pygame.Rect(self.cx - self.tank_width/2 * self.display_scale,
                                self.cy - self.tank_height/2 * self.display_scale,
                                self.tank_width * self.display_scale,
                                self.tank_height * self.display_scale)

        fish_rect = pygame.Rect(int(self.pos_x * self.display_scale + self.cx),
                                int(self.pos_y * self.display_scale + self.cy),
                                self.rect_width, self.rect_height)
        pygame.draw.rect(surf, (0, 0, 0), tank_rect, 2)
        pygame.draw.rect(surf, (0, 0, 255), fish_rect)


class MotorDriverSimulator(object):
    def __init__(self, sim):
        self.sim = sim
        self.pos_x, self.pos_y = 0, 0
        self.rect_width, self.rect_height = 10, 10
        self.display_scale = 1
        self.cx, self.cy = sim.width/2, sim.height/2

    def command(self, motor_cmd):
        self.pos_x += motor_cmd.fl
        self.sim.redraw()

    def redraw(self, surf):
        rect = pygame.Rect(int(self.pos_x * self.display_scale + self.cx),
                           int(self.pos_y * self.display_scale + self.cy),
                           self.rect_width, self.rect_height)
        pygame.draw.rect(surf, (255, 0, 0), rect)




