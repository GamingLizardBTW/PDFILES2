import logging
logger = logging.getLogger("secondmotorsubsystemlogger")

import commands2
from wpilib import PS5Controller
from constants import OP  
from subsystems.SecondMotorSubsystem import SecondMotorSubsystemClass


class TriggerSpin(commands2.Command):

    def __init__(self, secondmotorsubsystem: SecondMotorSubsystemClass, controller: PS5Controller) -> None:
        super().__init__()
        self.secondmotorsub = secondmotorsubsystem
        self.controller = controller
        self.addRequirements(self.secondmotorsub)

    def initialize(self):
        logger.info("TriggerSpin Command Initialized")

    def execute(self):
        # Read PS5 triggers
        right = self.controller.getR2Axis()  # 0.0 → 1.0
        left = self.controller.getL2Axis()   # 0.0 → 1.0
        speed = right - left                  # convert to -1.0 → +1.0
        self.secondmotorsub.run(speed)

    def end(self, interrupted: bool):
        self.secondmotorsub.stop()
        logger.info("TriggerSpin Command Ended")

    def isFinished(self):
        # Never finishes on its own
        return False
