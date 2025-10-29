import logging
import commands2
import phoenix6
from phoenix6.controls import DutyCycleOut
from constants import ELEC

logger = logging.getLogger("TwoMotorSubsystem")

class TwoMotorSubsystemClass(commands2.Subsystem):

    def __init__(self) -> None:
        super().__init__()
        self.motor1 = phoenix6.hardware.TalonFX(ELEC.first_motor_CAN_ID)
        self.motor2 = phoenix6.hardware.TalonFX(ELEC.second_motor_CAN_ID)
        self.dco = DutyCycleOut(0)
        logger.info("TwoMotorSubsystem initialized")

    def run_motor1(self, speed: float):
        self.motor1.set_control(self.dco.with_output(speed))
        logger.debug(f"Motor 1 running at speed {speed}")

    def run_motor2(self, speed: float):
        self.motor2.set_control(self.dco.with_output(speed))
        logger.debug(f"Motor 2 running at speed {speed}")

    def stop(self):
        self.motor1.set_control(self.dco.with_output(0))
        self.motor2.set_control(self.dco.with_output(0))
        logger.debug("Both motors stopped")
