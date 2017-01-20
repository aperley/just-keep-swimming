import logging
from DataTypes import FishPosition, MotorCommand, MC

logger = logging.getLogger(__name__)

TURN_S = 1
STRAIGHT_S = 1
STEER_IS = 1
STEER_OS = .3

SPIN_RIGHT = MotorCommand(fr=-1, fl=1, br=-1, bl=1)
SPIN_LEFT = MotorCommand(fr=1, fl=-1, br=1, bl=-1)
FRONT_STRAIGHT = MotorCommand(fr=STRAIGHT_S, fl=STRAIGHT_S, br=STRAIGHT_S, bl=STRAIGHT_S)
BACK_STRAIGHT = MotorCommand(fr=-STRAIGHT_S, fl=-STRAIGHT_S, br=-STRAIGHT_S, bl=-STRAIGHT_S)
FRONT_LEFT = MC(r=STEER_OS, l=STEER_IS)
FRONT_RIGHT = MC(r=STEER_IS, l=STEER_OS)
BACK_LEFT = MC(r=-STEER_OS, l=-STEER_IS)
BACK_RIGHT = MC(r=-STEER_IS, l=-STEER_OS)
STOP = MC(r=0, l=0)


class DriveController(object):
    X_MIN = -1
    Y_MIN = -1
    X_RANGE = 2
    Y_RANGE = 2
    ZONE_START = .3

    def __init__(self):
        pass

    def process(self, fish_pos):
        #logger.debug("Process %s" % str(fish_pos))
        val = fish_pos.x
        command = STOP
        if fish_pos.x >= -1 and fish_pos.x <= -self.ZONE_START:
            if fish_pos.y >= -1 and fish_pos.y < -self.ZONE_START:
		logger.debug("Zone: 'Backward Left'")
                command = BACK_LEFT
            elif fish_pos.y >= -self.ZONE_START and fish_pos.y <= self.ZONE_START:
		logger.debug("Zone: 'Backward Straight'")
                command=BACK_STRAIGHT
            elif fish_pos.y > self.ZONE_START and fish_pos.y <= 1:
		logger.debug("Zone: 'Backward Right'")
                command=BACK_RIGHT
        elif fish_pos.x <= 1 and fish_pos.x >= self.ZONE_START:
            if fish_pos.y >= -1 and fish_pos.y < -self.ZONE_START:
		logger.debug("Zone: 'Forward Left'")
                command=FRONT_LEFT
            elif fish_pos.y >= -self.ZONE_START and fish_pos.y <= self.ZONE_START:
		logger.debug("Zone: 'Forward Straight'")
                command=FRONT_STRAIGHT
            elif fish_pos.y > self.ZONE_START and fish_pos.y <= 1:
		logger.debug("Zone: 'Forward Right'")
                command=FRONT_RIGHT
        return command
	
