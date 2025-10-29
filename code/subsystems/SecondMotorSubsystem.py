"""""
import logging
log = logging.Logger('P212-robot')

import commands2
import phoenix6  
from phoenix6.controls import VoltageOut

from constants import ELEC


class SecondMotorSubsystemClass(commands2.Subsystem):

    def __init__(self) -> None:
        super().__init__()
        self.second_motor = phoenix6.hardware.TalonFX(ELEC.second_motor_CAN_ID)
        self.request = VoltageOut(0)

    def run(self, speed: float):
        self.second_motor.set_control(self.request.with_output(speed * 12.0))

    def go_forward(self):
        self.run(1.0)

    def go_reverse(self):
        self.run(-1.0)

    def stop(self):
        self.run(0.0)
"""""