import commands2
import logging
from subsystems.TwoMotorSubsystem import TwoMotorSubsystemClass

logger = logging.getLogger("TwoMotorCommands")

class RunBothMotors(commands2.Command):
    def __init__(self, twomotorsubsystem: TwoMotorSubsystemClass, speed: float = 1.0):
        super().__init__()
        self.twomotorsub = twomotorsubsystem
        self.speed = speed
        self.addRequirements(self.twomotorsub)

    def execute(self):
        self.subsystem.run_both(self.speed)

    def end(self, interrupted: bool):
        self.subsystem.stop()

    def isFinished(self):
        return False

class RunMotor1Only(commands2.Command):
    def __init__(self, twomotorsubsystem: TwoMotorSubsystemClass, speed: float = 1.0):
        super().__init__()
        self.twomotorsub = twomotorsubsystem
        self.speed = speed
        self.addRequirements(self.twomotorsub)

    def execute(self):
        self.subsystem.run_motor1_only(self.speed)

    def end(self, interrupted: bool):
        self.subsystem.stop()

    def isFinished(self):
        return False

# Run only motor2 while held
class RunMotor2Only(commands2.Command):
    def __init__(self, twomotorsubsystem: TwoMotorSubsystemClass, speed: float = 1.0):
        super().__init__()
        self.twomotorsub = twomotorsubsystem
        self.speed = speed
        self.addRequirements(self.twomotorsub)

    def execute(self):
        self.subsystem.run_motor2_only(self.speed)

    def end(self, interrupted: bool):
        self.subsystem.stop()

    def isFinished(self):
        return False
