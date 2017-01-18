from DataTypes import FishPosition

class FishSensor(object):
    def __init__(self):
        pass

    def poll(self):
        return FishPosition(x=0, y=0)