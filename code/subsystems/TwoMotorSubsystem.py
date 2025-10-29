import logging
log = logging.Logger('P212-robot')

import commands2
from phoenix6.controls import DutyCycleOut
import phoenix6


from constants import ELEC

class TwoMotorSubsystemClass(commands2.Subsystem):

    def __init__(self):
        super().__init__()
        self.motor1 = phoenix6.hardware.TalonFX(ELEC.first_motor_CAN_ID)
        self.motor2 = phoenix6.hardware.TalonFX(ELEC.second_motor_CAN_ID)

    # Run both motors at the same speed
    def run_both(self, speed: float):
        self.motor1.set(DutyCycleOut(speed))
        self.motor2.set(DutyCycleOut(speed))

    # Run only motor1
    def run_motor1_only(self, speed: float):
        self.motor1.set(DutyCycleOut(speed))
        self.motor2.set(DutyCycleOut(0))

    # Run only motor2
    def run_motor2_only(self, speed: float):
        self.motor1.set(DutyCycleOut(0))
        self.motor2.set(DutyCycleOut(speed))

    # Stop both motors
    def stop(self):
        self.motor1.set(DutyCycleOut(0))
        self.motor2.set(DutyCycleOut(0))
