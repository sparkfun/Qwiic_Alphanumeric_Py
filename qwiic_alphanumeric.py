#-----------------------------------------------------------------------------
# qwiic_alphanumeric.py
#
# Python library for the SparkFun Qwiic Alphanumeric displays.
#   https://www.sparkfun.com/products/16916
#   https://www.sparkfun.com/products/16917
#   https://www.sparkfun.com/products/16918
#   https://www.sparkfun.com/products/16919
#   https://www.sparkfun.com/products/18565
#   https://www.sparkfun.com/products/18566
#
#------------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, August 2021
# 
# This python library supports the SparkFun Electroncis qwiic 
# qwiic sensor/board ecosystem 
#
# More information on qwiic is at https:// www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun. Buy a board!
#==================================================================================
# Copyright (c) 2020 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#==================================================================================

"""
qwiic_alphanumeric
==================
Python module for the SparkFun Qwiic Alphanumeric displays.

This package is a port of the existing [SparkFun Alphanumeric Display Arduino Library](https://github.com/sparkfun/SparkFun_Alphanumeric_Display_Arduino_Library).

This package can be used in conjunction with the overall [SparkFun Qwiic Python Package](https://github.com/sparkfun/Qwiic_Py).

New to qwiic? Take a look at the entire [SparkFun Qwiic Ecosystem](https://www.sparkfun.com/qwiic).
"""
# ---------------------------------------------------------------------------------

import time
import qwiic_i2c

_DEFAULT_NAME = "Qwiic Alphanumeric"

_QWIIC_ALPHANUMERIC_DEFAULT_ADDRESS = 0x70
_AVAILABLE_I2C_ADDRESS = [QWIIC_ALPHANUMERIC_DEFAULT_ADDRESS, 0x71, 0x72, 0x73]

class QwiicAlphanumeric(object):
    """
    QwiicAlphanumeric

        :param address: The I2C address to use for the device.
                        If not provided, the default address is used.
        :param i2c_driver: An existing i2c driver object. If not provided a
                        a driver is created.
        :return: The QwiicAlphanumeric device object.
        :rtype: Object
    """
    # Constructor
    device_name = _DEFAULT_NAME
    available_addresses = _AVAILABLE_I2C_ADDRESS

    DEFAULT_NOTHING_ATTACHED = 0xFF

    # Define constants for segment bits
    SEG_A = 0x0001
    SEG_B = 0x0002
    SEG_C = 0x0004
    SEG_D = 0x0008
    SEG_E = 0x0010
    SEG_F = 0x0020
    SEG_G = 0x0040
    SEG_H = 0x0080
    SEG_I = 0x0100
    SEG_J = 0x0200
    SEG_K = 0x0400
    SEG_L = 0x0800
    SEG_M = 0x1000
    SEG_N = 0x2000

    # Blink rate
    ALPHA_BLINK_RATE_NOBLINK = 0b00
    ALPHA_BLINK_RATE_2HZ = 0b01
    ALPHA_BLINK_RATE_1HZ = 0b10
    ALPHA_BLINK_RATE_0_5HZ = 0b11

    # Display settings
    ALPHA_DISPLAY_ON = 0b1
    ALPHA_DISPLAY_OFF = 0b0

    # Decimal settings
    ALPHA_DECIMAL_ON = 0b1
    ALPHA_DECIMAL_OFF = 0b0

    # Colon settings
    ALPHA_COLON_ON = 0b1
    ALPHA_COLON_OFF = 0b0

    # Commands
    ALPHA_CMD_SYSTEM_SETUP = 0b00100000
    ALPHA_CMD_DISPLAY_SETUP = 0b10000000
    ALPHA_CMD_DIMMING_SETUP = 0b11100000

    # Lookup table of segments for various characters
    alphanumeric_segs = []
    # nmlkjihgfedcba
    alphanumeric_segs.append(0b00000000000000)  # ' ' (space)
    alphanumeric_segs.append(0b00001000001000)  # '!'
    alphanumeric_segs.append(0b00001000000010)  # '"'
    alphanumeric_segs.append(0b01001101001110)  # '#'
    alphanumeric_segs.append(0b01001101101101)  # '$'
    alphanumeric_segs.append(0b10010000100100)  # '%'
    alphanumeric_segs.append(0b00110011011001)  # '&'
    alphanumeric_segs.append(0b00001000000000)  # '''
    alphanumeric_segs.append(0b00000000111001)  # '('
    alphanumeric_segs.append(0b00000000001111)  # ')'
    alphanumeric_segs.append(0b11111010000000)  # '*'
    alphanumeric_segs.append(0b01001101000000)  # '+'
    alphanumeric_segs.append(0b10000000000000)  # ','
    alphanumeric_segs.append(0b00000101000000)  # '-'
    alphanumeric_segs.append(0b00000000000000)  # '.'
    alphanumeric_segs.append(0b10010000000000)  # '/'
    alphanumeric_segs.append(0b00000000111111)  # '0'
    alphanumeric_segs.append(0b00010000000110)  # '1'
    alphanumeric_segs.append(0b00000101011011)  # '2'
    alphanumeric_segs.append(0b00000101001111)  # '3'
    alphanumeric_segs.append(0b00000101100110)  # '4'
    alphanumeric_segs.append(0b00000101101101)  # '5'
    alphanumeric_segs.append(0b00000101111101)  # '6'
    alphanumeric_segs.append(0b01010000000001)  # '7'
    alphanumeric_segs.append(0b00000101111111)  # '8'
    alphanumeric_segs.append(0b00000101100111)  # '9'
    alphanumeric_segs.append(0b00000000000000)  # ':'
    alphanumeric_segs.append(0b10001000000000)  # ';'
    alphanumeric_segs.append(0b00110000000000)  # '<'
    alphanumeric_segs.append(0b00000101001000)  # '='
    alphanumeric_segs.append(0b01000010000000)  # '>'
    alphanumeric_segs.append(0b01000100000011)  # '?'
    alphanumeric_segs.append(0b00001100111011)  # '@'
    alphanumeric_segs.append(0b00000101110111)  # 'A'
    alphanumeric_segs.append(0b01001100001111)  # 'B'
    alphanumeric_segs.append(0b00000000111001)  # 'C'
    alphanumeric_segs.append(0b01001000001111)  # 'D'
    alphanumeric_segs.append(0b00000101111001)  # 'E'
    alphanumeric_segs.append(0b00000101110001)  # 'F'
    alphanumeric_segs.append(0b00000100111101)  # 'G'
    alphanumeric_segs.append(0b00000101110110)  # 'H'
    alphanumeric_segs.append(0b01001000001001)  # 'I'
    alphanumeric_segs.append(0b00000000011110)  # 'J'
    alphanumeric_segs.append(0b00110001110000)  # 'K'
    alphanumeric_segs.append(0b00000000111000)  # 'L'
    alphanumeric_segs.append(0b00010010110110)  # 'M'
    alphanumeric_segs.append(0b00100010110110)  # 'N'
    alphanumeric_segs.append(0b00000000111111)  # 'O'
    alphanumeric_segs.append(0b00000101110011)  # 'P'
    alphanumeric_segs.append(0b00100000111111)  # 'Q'
    alphanumeric_segs.append(0b00100101110011)  # 'R'
    alphanumeric_segs.append(0b00000110001101)  # 'S'
    alphanumeric_segs.append(0b01001000000001)  # 'T'
    alphanumeric_segs.append(0b00000000111110)  # 'U'
    alphanumeric_segs.append(0b10010000110000)  # 'V'
    alphanumeric_segs.append(0b10100000110110)  # 'W'
    alphanumeric_segs.append(0b10110010000000)  # 'X'
    alphanumeric_segs.append(0b01010010000000)  # 'Y'
    alphanumeric_segs.append(0b10010000001001)  # 'Z'
    alphanumeric_segs.append(0b00000000111001)  # '['
    alphanumeric_segs.append(0b00100010000000)  # '\'
    alphanumeric_segs.append(0b00000000001111)  # ']'
    alphanumeric_segs.append(0b10100000000000)  # '^'
    alphanumeric_segs.append(0b00000000001000)  # '_'
    alphanumeric_segs.append(0b00000010000000)  # '`'
    alphanumeric_segs.append(0b00000101011111)  # 'a'
    alphanumeric_segs.append(0b00100001111000)  # 'b'
    alphanumeric_segs.append(0b00000101011000)  # 'c'
    alphanumeric_segs.append(0b10000100001110)  # 'd'
    alphanumeric_segs.append(0b00000001111001)  # 'e'
    alphanumeric_segs.append(0b00000001110001)  # 'f'
    alphanumeric_segs.append(0b00000110001111)  # 'g'
    alphanumeric_segs.append(0b00000101110100)  # 'h'
    alphanumeric_segs.append(0b01000000000000)  # 'i'
    alphanumeric_segs.append(0b00000000001110)  # 'j'
    alphanumeric_segs.append(0b01111000000000)  # 'k'
    alphanumeric_segs.append(0b01001000000000)  # 'l'
    alphanumeric_segs.append(0b01000101010100)  # 'm'
    alphanumeric_segs.append(0b00100001010000)  # 'n'
    alphanumeric_segs.append(0b00000101011100)  # 'o'
    alphanumeric_segs.append(0b00010001110001)  # 'p'
    alphanumeric_segs.append(0b00100101100011)  # 'q'
    alphanumeric_segs.append(0b00000001010000)  # 'r'
    alphanumeric_segs.append(0b00000110001101)  # 's'
    alphanumeric_segs.append(0b00000001111000)  # 't'
    alphanumeric_segs.append(0b00000000011100)  # 'u'
    alphanumeric_segs.append(0b10000000010000)  # 'v'
    alphanumeric_segs.append(0b10100000010100)  # 'w'
    alphanumeric_segs.append(0b10110010000000)  # 'x'
    alphanumeric_segs.append(0b00001100001110)  # 'y'
    alphanumeric_segs.append(0b10010000001001)  # 'z'
    alphanumeric_segs.append(0b10000011001001)  # '{'
    alphanumeric_segs.append(0b01001000000000)  # '|'
    alphanumeric_segs.append(0b00110100001001)  # '}'
    alphanumeric_segs.append(0b00000101010010)  # '~'
    alphanumeric_segs.append(0b11111111111111)  # Unknown character (DEL or RUBOUT)

    # Globals
    _device_address_display_one = 0    # Address of primary alphanumeric display
    _device_address_display_two = 0
    _device_address_display_three = 0
    _device_address_display_four = 0
    digit_position = 0  # Tracks the position of the current digit
    number_of_displays = 1 # Tracks the number of displays connected to the I2C bus, default is one display
    display_on_off = 0  # Tracks the on/off state of the display
    decimal_on_off = 0  # Tracks the on/off state of the decimal segment
    colon_on_off = 0    # Tracks the on/off state of the colon segment
    blink_rate = ALPHA_BLINK_RATE_NOBLINK   # Tracks the current blinking status

    # TODO: Not sure this will work
    displayRAM[16 * 4]
    display_content[4 * 4 + 1] = ""

    def __init__(self, address=None, i2c_driver=None):

        # Did the user specify an I2C address?
        self.address = address if address != None else self.available_addresses[0]

        # Load the I2C driver if one isn't provided
        if i2c_driver == None:
            self._i2c = qwiic_i2c.getI2CDriver()
            if self._i2c == None:
                print("Unable to load I2C driver for this platform.")
                return
        else:
            self._i2c = i2c_driver
    
    # ---------------------------------------------------------------------------------
    # begin(address_left, address_left_center, address_right_center, address_right)
    #
    # Initialize the system and validate the baord.
    def begin(self, address_display_one = _QWIIC_ALPHANUMERIC_DEFAULT_ADDRESS, address_display_two = DEFAULT_NOTHING_ATTACHED, address_display_three = DEFAULT_NOTHING_ATTACHED, address_display_four = DEFAULT_NOTHING_ATTACHED):
        """
            Initialize the operation of the Qwiic Alphanumeric.
            Assign addresses to displays and determine the number of displays connected to the bus.
            Run is_connected().
            Initialize and clear displays.
            
            :param address_display_one: I2C address of left-most display
            :param address_display_two: I2C address of the left-center display
            :param address_dispplay_three: I2C address of the right-center display
            :param address_display_four: I2C address of the right-most display
            :return: Returns true if a Qwiic Alphanumeric is connected to the system.
                    False otherwise.
            :rtype: bool
        """
        self._device_address_display_one = address_display_one # Grab the address(es) of the alphanumeric(s)
        self._device_address_display_two = address_display_two
        self._device_address_display_three = address_display_three
        self._device_address_display_four = address_display_four

        # Figure out how many displays are attached by the number of addresses the user specified
        if self._device_address_display_four != DEFAULT_NOTHING_ATTACHED:
            self.number_of_displays = 4
        elif self._device_address_display_three != DEFAULT_NOTHING_ATTACHED:
            self.number_of_displays = 3
        elif self._device_address_display_two != DEFAULT_NOTHING_ATTACHED:
            self.number_of_displays = 2
        else:
            self.number_of_displays = 1

        for i in range(1, self.number_of_displays + 1):
            if self.is_connected(i) == False:
                return False
            time.sleep(0.01)
        
        if self.initialize() == False:
            return False
        
        if self.clear() == False:
            return False
        
        self.display_content[4 * 4] = '\0'  # Terminate the array because we are doing direct prints
    
    # ---------------------------------------------------------------------------------
    # is_connected(display_number)
    #
    # Check if there are acutal boards connected to the system
    def is_connected(self, display_number):
        """
            Check that dispplays are responding on the I2C bus.

            :param display_number: The number of the display on the bus
            :return: True if the device is connected, false otherwise.
            :rtype: bool
        """
        tries_before_giveup = 5 
        
        # The LED driver IC sometimes fails to respond. This attempts multiple times before giving up.
        for x in range(0, tries_before_giveup):
            if qwiic_i2c.isDeviceConnected(self.look_up_display_address(display_number)) == True:
                return True
            time.sleep(0.01)
        return False

    # ---------------------------------------------------------------------------------
    # initialize()
    #
    # Run through initialization sequence for each display connected on the I2C bus
    def initialize(self):
        """
            Run through initialization sequence for each display connected on the I2C bus
            Enable clocks, set brightness default to full brightness, turn off blinking, and
            turn all displays on

            :return: True if all function calls passed, False if there's a failure somewhere
            :rtype: bool
        """
        # Turn on system clock of all displays
        if self.enable_system_clock() == False:
            return False
        
        # Set brightness of all displays to full brightness
        if self.set_brightness(15) == False:
            return False

        # Turn blinking off for all displays
        if self.set_blink_rate(self.ALPHA_BLINK_RATE_NOBLINK) == False:
            return False
        
        # Turn on all displays
        if self.display_on() == False:
            return False
        
        return True
    
    # ---------------------------------------------------------------------------------
    # enable_system_clock()
    #
    # Turn on the system oscillator for all displays on the I2C bus
    def enable_system_clock(self):
        """
            Turn on the system oscillator for all displays on the I2C bus

            :return: True if all clocks successfully enabled, false otherwise.
            :rtype: bool
        """
        status = True
        
        for i in range(1, self.number_of_displays + 1):
            if self.enable_system_clock_single(i) == False:
                status = False
        
        return status

    # ---------------------------------------------------------------------------------
    # disable_system_clock()
    #
    # Turn off the system oscillator for all displays on the bus
    def disable_system_clock(self):
        """
            Turn off the system oscillator for all displays on the bus

            :return: True if all clocks successfully disabled, false otherwise.
            :rtype: bool
        """
        status = True

        for i in range(1, self.number_of_displays + 1):
            if self.disable_system_clock_single(i) == False:
                status = False
        
        return status
    
    # ---------------------------------------------------------------------------------
    # enable_system_clock_single(display_number)
    #
    # Turn on the system oscillator for normal operation mode
    def enable_system_clock_single(self, display_number):
        """
            Turn on the system oscillator for normal operation mode

            :param display_number: number of display on I2C bus to enable the system clock
                for.
            :return: True if setting updated successfully, false otherwise.
            :rtype: bool
        """
        data_to_write = self.ALPHA_CMD_SYSTEM_SETUP | 1 # Enable system clock  bit

        status = self.write_RAM(self.look_up_display_address(display_number), data_to_write)
        time.sleep(0.001)   # Allow display to start

        return status

    # ---------------------------------------------------------------------------------
    # disable_system_clock_single(display_number)
    #
    # Turn off the system oscillator for standby mode
    def disable_system_clock_single(self, display_number):
        """
            Turn off the system oscillator for standby mode

            :param display_number: number of display on I2C bus to disable the system
                clock for.
            :return: True if setting updated successfully, false otherwise.
            :rtype: bool
        """
        data_to_write = self.ALPHA_CMD_SYSTEM_SETUP | 0 # Standby mode

        return self.write_RAM(self.look_up_display_address(display_number), data_to_write)

    # ---------------------------------------------------------------------------------
    # look_up_display_address(display_number)
    #
    # This function connects the display number to its coressponding address
    def look_up_display_address(self, display_number):
        """
            This function connects the display number to its coressponding address

            :param display_number: number of display on I2C bus. The left-most display is zero
                and display number increments by 1 with each additional display on bus.
            :return: The I2C address of given display. 0 if display_number is not valid
            :rtype: int
        """
        if display_number == 1:
            return self._device_address_display_one
        elif display_number == 2:
            return self._device_address_display_two
        elif display_number == 3:
            return self._device_address_display_three
        elif display_number == 4:
            return self._device_address_display_four
        
        return 0    # We shouldn't get here

    # ---------------------------------------------------------------------------------
    # clear()
    #
    # Turn off all segments of all displays connected to bus
    def clear(self):
        """
            Turn off all segments of all displays connected to bus

            :return: True if display was updated correctly, false otherwise
            :rtype: bool
        """
        # Clear the display_RAM array
        for i in range(0, 16 * self.number_of_displays):
            self.display_RAM[i] = 0
        
        # Reset digit position
        self.digit_position = 0

        return self.update_display()

    # ---------------------------------------------------------------------------------
    # set_brightness(duty)
    # 
    # This function sets the brightness of all displays on the bus
    def set_brightness(self, duty):
        """
            This function sets the brightness of all displays on the bus.
            Duty cycle over 16.

            :param duty: Valid between 0 (display off) and 15 (full brightness)
            :return: True if brightness is successfully updated, false otherwise.
            :rtype: bool
        """
        status = True

        for i in range(1, self.number_of_displays + 1):
            if self.set_brightness_single(i, duty) == False:
                status = False
        
        return status

    # ---------------------------------------------------------------------------------
    # set_brightness_single(display_number, duty)
    #
    # Set the brightness of a single display
    def set_brightness_single(self, display_number, duty):
        """
            Set the brightness of a single display

            :param display_number: The number of display on the I2C bus.
            :param duty: Over 16. Valid between 0 (display off) and 15 (full brightness)
            :return: True if brightness is successfully updated, false otherwise.
            :rtype: bool
        """
        # Error check
        if duty > 15:
            duty = 15
        elif duty < 0:
            duty = 0
        
        data_to_write = self.ALPHA_CMD_DIMMING_SETUP | duty
        return self.write_RAM(self.look_up_display_address(display_number), data_to_write)

    # ---------------------------------------------------------------------------------
    # set_blink_rate(rate)
    #
    # Set the blink rate of all displays on the bus
    def set_blink_rate(self, rate):
        """
            Set the blink rate of all displays on the bus as defined by the datasheet.

            :param rate: Blink frequency in Hz. Valid options are defined by datasheet:
                2, 1, or 0.5 Hz. Any other input to this function will result in steady
                alphanumeric display (no blink).
            :return: True if blink setting is successfully updated, false otherwise.
            :rtype: bool
        """
        status = True

        for i in range(1, self.number_of_displays + 1):
            if self.set_blink_rate_singe(i, rate) == False:
                status = False
        
        return status
    
    # ---------------------------------------------------------------------------------
    