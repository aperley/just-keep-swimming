#!/usr/bin/env python

import argparse
import logging
import sys

import DriveController
import FishSensor
import MotorDriver

LOG_LEVEL = logging.DEBUG
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--log", help="file to write log to (default stdout)")
    args = parser.parse_args()

    init_logging(args)

    fish_sensor = FishSensor.FishSensor()
    controller = DriveController.DriveController()
    motor_driver = MotorDriver.MotorDriver()

    logger.info("Application initialized")

    motor_driver.set_enabled(True)
    logger.info("Application running")

    while True:
        fish_position = fish_sensor.poll()
        motor_cmd = controller.process(fish_position)
        motor_driver.command(motor_cmd)

def init_logging(args):
    if args.log:
        logging.basicConfig(level=LOG_LEVEL, filename=args.log)
    else:
        logging.basicConfig(level=LOG_LEVEL, stream=sys.stdout)

    logger.debug("Logger initialized")



if __name__ == "__main__":
    main()
