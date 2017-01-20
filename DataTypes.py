from collections import namedtuple

FishPosition = namedtuple('FishPosition', ['x', 'y'])

MotorCommand = namedtuple('MotorCommand', ['fl', 'fr', 'bl', 'br'])

def MC(r, l):
	return MotorCommand(fr=r, br=r, fl=l, bl=l)
