"""import logging
logger = logging.getLogger("firstmotorsubsystemlogger")



import commands2
import constants
from constants import OP



from subsystems.FirstMotorSubsystem import FirstMotorSubsystemClass


class  ForwardSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:

        
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.go_forward()
        logger.info("Forward Command Initialized")  


    def isFinished(self):

        return True


class  ReverseSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:

        
        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.go_reverse()
        logger.info("Reverse Command Initialized")


    def isFinished(self):

        return True


class  StopSpin(commands2.Command):

    def __init__(self, firstmotorsubsystem: FirstMotorSubsystemClass) -> None:

        self.firstmotorsub = firstmotorsubsystem
        self.addRequirements(self.firstmotorsub)

    def initialize(self):
        self.firstmotorsub.stop()
        logger.info("Stop Command Initialized")




    def isFinished(self):

        return True
"""
