import logging
from DataTypes import FishPosition, MotorCommand

logger = logging.getLogger(__name__)

class DriveController(object):
    X_MIN = -1
    Y_MIN = -1
    X_RANGE = 2
    Y_RANGE = 2

    def __init__(self):
        pass

    def process(self, fish_pos):
        logger.debug("Process %s" % str(fish_pos))
        val = fish_pos.x
        if fish_pos.x >= -1 and fish_pos.x <= -.5:
            if fish_pos.y >= -1 and fish_pos.y < -.5:
                return MotorCommand(fr=-.5, fl=-1, br=-.5, bl=-1)
            elif fish_pos.y >= -.5 and fish_pos.y <= .5:
                return MotorCommand(fr=-1, fl=-1, br=-1, bl=-1)
            elif fish_pos.y > .5 and fish_pos.y <= 1:
                return MotorCommand(fr=-1, fl=-.5, br=-1, bl=-.5)
        elif fish_pos.x <= 1 and fish_pos.x >= .5:
            if fish_pos.y >= -1 and fish_pos.y < -.5:
                return MotorCommand(fr=1, fl=.5, br=1, bl=.5)
            elif fish_pos.y >= -.5 and fish_pos.y <= .5:
                return MotorCommand(fr=1, fl=1, br=1, bl=1)
            elif fish_pos.y > .5 and fish_pos.y <= 1:
                return MotorCommand(fr=.5, fl=1, br=.5, bl=1)
        else:
            return MotorCommand(fr=0, fl=0, br=0, bl=0)
        return MotorCommand(fr=val, fl=val, br=val, bl=val) 