# !/usr/bin/env python
# ----------------------------------------------------------------------
# qwiic_alphanumeric_ex2_turn_on_one_segment.py
#
# This example tests illuminating individual segments of the display. Pass
# in the segment and digit you wish to illuminate into illuminate_segment().
# ----------------------------------------------------------------------
#
# Written by Priyanka Makin @ SparkFun Electronics, September 2021
#
# This python library supports the SparkFun Electronics qwiic sensor/
# board ecosystem on a Raspberry Pi (and compatable) single board 
# computers.
#
# More information on qwiic is at https://www.sparkfun.com/qwiic
#
# Do you like this library? Help support SparkFun by buying a board!
#
# ======================================================================
# Copyright (c) 2021 SparkFun Electronics
#
# Permission is hereby granted, free of charge, to any person obtaining 
# a copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to 
# the following conditions:
#
# The above copyright notice and this permission notice shall be 
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#=======================================================================
# Example 2

from __future__ import print_function
import qwiic_alphanumeric
import time
import sys

def run_example():

    print("\nSparkFun Qwiic Alphanumeric - Example 2: Turn On One Segment")
    my_display = qwiic_alphanumeric.QwiicAlphanumeric()

    if my_display.begin() == False:
        print("\nThe Qwiic Alphanumeric isn't connected to the system. Please check your connection", \
            file=sys.stderr)
        return
    
    print("\nQwiic Alphanumeric ready!")
    
    # while True:
        # for display_num in range(0, 4):
            # my_display.illuminate_segment('A', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('B', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('C', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('D', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('E', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('F', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('G', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('H', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('I', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('J', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('K', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('L', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('M', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
            # my_display.illuminate_segment('N', display_num)
            # my_display.update_display()
            # time.sleep(1)
            # my_display.clear()
    
    my_display.illuminate_segment('A', 0)
    my_display.illuminate_segment('L', 1)
    my_display.illuminate_segment('I', 2)
    my_display.illuminate_segment('G', 3)

    my_display.update_display()

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 2")
        sys.exit(0)
