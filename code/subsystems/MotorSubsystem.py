import logging
log = logging.Logger('P212-robot')
import wpilib
from wpilib import DigitalInput
import commands2
from constants import ELEC
import phoenix6



class MotorSubsystemClass(commands2.Subsystem):

    def __init__(self) -> None:

        super().__init__()

        self.my_motor = phoenix6.hardware.TalonFX(
            ELEC.my_motor_CAN_ID 
        )

    def go_forward(self):
        self.my_motor.set(ELEC.my_motor_speed)

    def go_reverse(self):
        self.my_motor.set(ELEC.my_motor_speed_reverse)

    def stop(self):
 
        self.my_motor.set(0.0)
