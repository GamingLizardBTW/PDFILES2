#
# Copyright (c) FIRST and other WPILib contributors.
# Open Source Software; you can modify and/or share it under the terms of
# the WPILib BSD license file in the root directory of this project.
#

import logging
log = logging.Logger('P212-robot')
import wpilib
import commands2
import commands2.button
from commands2.button import Trigger
from constants import OP
#from wpilib import XboxController
from wpilib import PS5Controller

#Subsystems
import subsystems.MotorSubsystem 


#Commands
from commands.MotorCommands import ForwardSpin, ReverseSpin, StopSpin

class RobotContainer:

    def __init__(self):

        #Controllers
        self.stick = commands2.button.CommandXboxController(OP.joystick_port)
        self.PS5 = PS5Controller(OP.joystick_port)
        
        
        #Subsystems
        self.motorsub = subsystems.MotorSubsystem.MotorSubsystemClass()


        self.configureButtonBindings()


    def configureButtonBindings(self):
        #Xbox controller
        #self.stick.leftBumper().whileTrue(ForwardSpin(self.motorsub))
        #self.stick.leftBumper().whileFalse(StopSpin(self.motorsub))
        #self.stick.rightBumper().whileTrue(ReverseSpin(self.motorsub))
        #self.stick.rightBumper().whileFalse(StopSpin(self.motorsub))
        
        #PS5 controller
        Trigger(lambda: self.stick.getL1Button()).whileTrue(ForwardSpin(self.motorsub))
        Trigger(lambda: self.stick.getL1Button()).whileFalse(StopSpin(self.motorsub))

        Trigger(lambda: self.stick.getR1Button()).whileTrue(ReverseSpin(self.motorsub))
        Trigger(lambda: self.stick.getR1Button()).whileFalse(StopSpin(self.motorsub))


        # run the example command when the X button is pressed


    def all_subsystems(self):
        """
        Return every attribute of this RobotContainer which is an instance of
        a commands2.Subsystem subclass.
        """
        subsystems = []
        for attribute_name in dir(self):
            attribute = getattr(self, attribute_name)
            if isinstance(attribute, commands2.Subsystem):
                subsystems.append(attribute)
        return subsystems


    def get_autonomous_command(self):
        pass
