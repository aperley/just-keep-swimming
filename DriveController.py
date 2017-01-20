import logging
from DataTypes import FishPosition, MotorCommand

logger = logging.getLogger(__name__)

class DriveController(object):
    MIN_DELTA_X = 0.01
    MIN_SPEED = 0.01
    DECCEL = 1.05
    Y_THRESHOLD = .5
    TURN_COEFF = .7

    def __init__(self):
        self.prev_pos = FishPosition(x=0, y=0)
        self.vel_x = 0.0
        self.turn = 0.0

    def process(self, fish_pos):
        delta_x = fish_pos.x - self.prev_pos.x
        if abs(delta_x) >= self.MIN_DELTA_X:
            self.vel_x = self.compute_speed(delta_x)
        elif abs(self.vel_x) > self.MIN_SPEED:
            self.vel_x /= self.DECCEL
        else:
            self.vel_x = 0.0


        logger.debug("Process: delta_x=%.2f, vel_x=%.2f" % (delta_x, self.vel_x))

        self.prev_pos = fish_pos
        if abs(fish_pos.y) < self.Y_THRESHOLD:
            return MotorCommand(fl=self.vel_x, fr=self.vel_x, bl=self.vel_x, br=self.vel_x)
        elif fish_pos.y < 0:
            slow_wheel = self.vel_x / (1 + abs(fish_pos.y) * self.TURN_COEFF)
            return MotorCommand(fl=slow_wheel, fr=self.vel_x, bl=slow_wheel, br=self.vel_x)
        else:
            slow_wheel = self.vel_x / (1 + abs(fish_pos.y) * self.TURN_COEFF)
            return MotorCommand(fl=self.vel_x, fr=slow_wheel, bl=self.vel_x, br=slow_wheel)



    def compute_speed(self, delta_x):
        speed = delta_x * 10
        if speed > 1.0:
            speed = 1.0
        elif speed < -1.0:
            speed = -1.0
        return speed
