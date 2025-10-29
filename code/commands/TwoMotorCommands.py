import logging
import commands2
import wpilib
from subsystems.TwoMotorSubsystem import TwoMotorSubsystemClass

logger = logging.getLogger("DualMotorControlCommand")

class DualMotor(commands2.Command):

    def __init__(self, twomotorsubsystem: TwoMotorSubsystemClass, controller: wpilib.PS5Controller) -> None:
        super().__init__()
        self.twomotorsub = twomotorsubsystem
        self.controller = controller
        self.addRequirements(self.twomotorsub)

    def initialize(self):
        logger.info("DualMotorControlCommand initialized")

    def execute(self):
        x_pressed = self.controller.getCrossButton()  # X button on PS5
        l1_pressed = self.controller.getL1Button()
        r1_pressed = self.controller.getR1Button()

        if not x_pressed:
            self.twomotorsub.stop()
            return

        # If X is pressed:
        if l1_pressed and not r1_pressed:
            self.twomotorsub.run_motor1(1.0)
            self.twomotorsub.run_motor2(0.0)
        elif r1_pressed and not l1_pressed:
            self.twomotorsub.run_motor1(0.0)
            self.twomotorsub.run_motor2(1.0)
        else:
            # If just X (or both bumpers) pressed → run both
            self.twomotorsub.run_motor1(1.0)
            self.twomotorsub.run_motor2(1.0)

    def end(self, interrupted: bool):
        self.twomotorsub.stop()
        logger.info("DualMotorControlCommand ended")

    def isFinished(self):
        # Only ends when command is cancelled (button released)
        return False
