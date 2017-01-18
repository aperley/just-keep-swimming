from collections import namedtuple

FishPosition = namedtuple('FishPosition', ['x', 'y'])

MotorCommand = namedtuple('MotorCommand', ['fl', 'fr', 'bl', 'br'])