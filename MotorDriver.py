# Ref: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/using-dc-motors

from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import atexit

class MotorDriver(object):
    def __init__(self):
        self.mh = Adafruit_MotorHAT(addr=0x60)
        self.fl = mh.getMotor(1)
        self.fr = mh.getMotor(2)
        self.bl = mh.getMotor(3)
        self.br = mh.getMotor(4)

        # Start with the module disabled
        self.set_enabled(False)

        # Turn off the motors if the module is killed
        atexit.register(self._turnOffMotors)

    def command(self, motor_cmd):
        if self._enabled:
            self._command_motor(self.fl, motor_cmd.fl)
            self._command_motor(self.fr, motor_cmd.fr)
            self._command_motor(self.bl, motor_cmd.bl)
            self._command_motor(self.br, motor_cmd.br)

    def set_enabled(self, enabled):
        self._enabled = enabled
        if not self._enabled:
            self._turnOffMotors()

    def is_enabled(self):
        return self._enabled


    def _command_motor(self, motor, velocity):
        assert -1.0 <= velocity <= 1.0
        pwm_val = int(abs(velocity) * 255)
        if velocity >= 0:
            direction = Adafruit_MotorHAT.FORWARD
        else:
            direction = Adafruit_MotorHAT.BACKWARD

        motor.setSpeed(pwm_val)
        motor.run(direction)

    def _turnOffMotors(self):
        for motor in (self.fl, self.fr, self.bl, self.br):
            motor.run(Adafruit_MotorHAT.RELEASE)