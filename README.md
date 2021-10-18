Qwiic_Alphanumeric_Py
===============

<p align="center">
   <img src="https://cdn.sparkfun.com/assets/custom_pages/2/7/2/qwiic-logo-registered.jpg"  width=200>  
   <img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png"  width=240>   
</p>
<p align="center">
	<a href="https://pypi.org/project/sparkfun-qwiic-alphanumeric/" alt="Package">
		<img src="https://img.shields.io/pypi/pyversions/sparkfun-qwiic-alphanumeric.svg" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Alphanumeric_Py/issues" alt="Issues">
		<img src="https://img.shields.io/github/issues/sparkfun/Qwiic_Alphanumeric_Py.svg" /></a>
	<a href="https://qwiic-alphanumeric-py.readthedocs.io/en/latest/?" alt="Documentation">
		<img src="https://readthedocs.org/projects/qwiic-alphanumeric-py/badge/?version=latest&style=flat" /></a>
	<a href="https://github.com/sparkfun/Qwiic_Alphanumeric_Py/blob/master/LICENSE" alt="License">
		<img src="https://img.shields.io/badge/license-MIT-blue.svg" /></a>
	<a href="https://twitter.com/intent/follow?screen_name=sparkfun">
        	<img src="https://img.shields.io/twitter/follow/sparkfun.svg?style=social&logo=twitter"
           	 alt="follow on Twitter"></a>

</p>


<img src="https://cdn.sparkfun.com/assets/parts/1/5/8/5/5/16919-SparkFun_Qwiic_Alphanumeric_Display_-_Pink-01.jpg"  align="right" width=300 alt="SparkFun Qwiic Alphanumeric - Pink">

Python module for the [SparkFun Qwiic Alphanumeric Display].

It is compatible with the following products:
* [SparkFun Qwiic Alphanumeric Display - Pink](https://www.sparkfun.com/products/16919)
* [SparkFun Qwiic Alphanumeric Display - Red](https://www.sparkfun.com/products/16916)
* [SparkFun Qwiic Alphanumeric Display - Purple](https://www.sparkfun.com/products/16918)
* [SparkFun Qwiic Alphanumeric Display - Blue](https://www.sparkfun.com/products/16917)
* [SparkFun Qwiic Alphanumeric Display - Green](https://www.sparkfun.com/products/18566)
* [SparkFun Qwiic Alphanumeric Display - White](https://www.sparkfun.com/products/18656)

This python package is a port of the existing [SparkFun Qwiic Alphanumeric Arduino Library](https://github.com/sparkfun/SparkFun_Alphanumeric_Display_Arduino_Library)

This package can be used in conjunction with the overall [SparkFun qwiic Python Package](https://github.com/sparkfun/Qwiic_Py)

New to qwiic? Take a look at the entire [SparkFun qwiic ecosystem](https://www.sparkfun.com/qwiic).

## Contents

* [Supported Platforms](#supported-platforms)
* [Dependencies](#dependencies)
* [Installation](#installation)
* [Documentation](#documentation)
* [Example Use](#example-use)

Supported Platforms
--------------------
The Qwiic LED Stick Python package currently supports the following platforms:
* [Raspberry Pi](https://www.sparkfun.com/search/results?term=raspberry+pi)

Dependencies
--------------
This driver package depends on the qwiic I2C driver:
[Qwiic_I2C_Py](https://github.com/sparkfun/Qwiic_I2C_Py)

Documentation
-------------
The SparkFun Qwiic LED Stick module documentation is hosted at [ReadTheDocs](https://qwiic-alphanumeric-py.readthedocs.io/en/latest/index.html)

Installation
---------------
### PyPi Installation

This repository is hosted on PyPi as the [sparkfun-qwiic-alphanumeric](https://pypi.org/project/sparkfun-qwiic-alphanumeric/) package. On systems that support PyPi installation via pip, this library is installed using the following commands

For all users (note: the user must have sudo privileges):
```sh
sudo pip install sparkfun-qwiic-alphanumeric
```
For the current user:

```sh
pip install sparkfun-qwiic-alphanumeric
```
To install, make sure the setuptools package is installed on the system.

Direct installation at the command line:
```sh
python setup.py install
```

To build a package for use with pip:
```sh
python setup.py sdist
 ```
A package file is built and placed in a subdirectory called dist. This package file can be installed using pip.
```sh
cd dist
pip install sparkfun-qwiic-alphanumeric-<version>.tar.gz
```

Example Use
 -------------
See the examples directory for more detailed use examples.

```python
from __future__ import print_function
import qwiic_alphanumeric
import time
import sys

def run_example():

    print("\nSparkFun Qwiic Alphanumeric - Example 4: Print String")
    my_display = qwiic_alphanumeric.QwiicAlphanumeric()

    if my_display.begin() == False:
        print("\nThe Qwiic Alphanumeric isn't connected to the system. Please check your connection.", \
            file=sys.stderr)
        return
    
    print("\nQwiic Alphanumeric ready!")

    my_display.print("Milk")

if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 4")
        sys.exit(0)
```
<p align="center">
<img src="https://cdn.sparkfun.com/assets/custom_pages/3/3/4/dark-logo-red-flame.png" alt="SparkFun - Start Something">
</p>
