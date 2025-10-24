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
import subsystems.Motor_ss 
from subsystems.Motor_ss import Motor_Subsystem

import commands.motor_commands
from commands.motor_commands import ForwardSpin, ReverseSpin, StopSpin

#from wpilib import XboxController
from wpilib import PS5Controller

class RobotContainer:
    """
    This class is where the bulk of the robot should be declared.  Since
    Command-based is a "declarative" paradigm, very little robot logic should
    actually be handled in the :class:`.Robot` periodic methods (other than
    the scheduler calls). Instead, the structure of the robot (including
    subsystems, commands, and button mappings) should be declared here.
    """

    def __init__(self):
        """
        The container for the robot. Contains subsystems, user controls,
        and commands.
        """
        # The driver's controller
        #
        # It's best not to create controller objects anywhere else.  If your
        # subsystem needs to access the controller, pass self.stick in to
        # the subsystem's constructor.
        #
        self.stick = commands2.button.CommandXboxController(OP.joystick_port)
        self.PS5 = PS5Controller(OP.joystick_port)

        

        # The robot's subsystems
        #
        ## TODO: Change this for your robot!
        ##       (Use your subsystems, and change the variable name.)
        ##
        #motorsub = subsystems.Motor_ss.Motor_Subsystem()
        self.motorsub = subsystems.Motor_ss.Motor_Subsystem

        # Configure the button bindings
        self.configureButtonBindings()


    def configureButtonBindings(self):
        """
        Use this method to define your button->command mappings. Buttons can
        be created via the button factories on
        commands2.button.CommandGenericHID or one of its subclasses
        (commands2.button.CommandJoystick or
        command2.button.CommandXboxController).
        """
        ## TODO: Change this for your robot!
        ##       (Use your commands and subsystems, and bind them to
        ##       buttons you choose.)
        ##
        # run the example command when the left bumper is pressed

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
