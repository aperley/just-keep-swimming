import logging
from DataTypes import FishPosition, MotorCommand

logger = logging.getLogger(__name__)

class DriveController(object):
    def __init__(self):
        pass

    def process(self, fish_pos):
        logger.debug("Process %s" % str(fish_pos))
        val = fish_pos.x
        return MotorCommand(fr=val, fl=val, br=val, bl=val) 