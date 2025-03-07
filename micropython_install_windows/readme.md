# MicroPython

## Arduino Nano ESP32 ABX00083

The Arduino Nano ESP32 is a ESP32 microcontroller from Espressif, with a NORA-W106 WiFi and Bluetooth module from u-blox. It has a USB-C connector, 16 MB of Flash and is a budget development board which serves as an entry point for MicroPython. MicroPython uses the Python programming language to program a microcontroller.

My Arduino Nano ESP32 looks as follows:

<img src='./images/img_001.png' alt='img_001' width='400'/>

The reset button is shown in red. The green power LED is shown in green and the yellow test LED is shown in yellow.

BIOS Chip:
    GigaDevice 
    PJ2K40
    25B128EW1H
    C008784

Wi-Fi and BlueTooth:
    C37AFE
    10B-00 23/39
    NORA-W106

## Device Mananger

Attach the ESP32 to a computer using a USB-C or USB-C to USB 3.0 cable. RIght click the Start button and select Device Manager:

<img src='./images/img_002.png' alt='img_002' width='200'/>

The Arduino DFU displays under Other Devices and does not have a system driver:

<img src='./images/img_003.png' alt='img_003' width='600'/>

## Arduino IDE

Download the Arduino IDE for Windows:

* [Arduino IDE](https://www.arduino.cc/en/software)

<img src='./images/img_004.png' alt='img_004' width='600'/>

<img src='./images/img_005.png' alt='img_005' width='600'/>

Launch the setup application:

<img src='./images/img_006.png' alt='img_006' width='600'/>

Select I agree:

<img src='./images/img_007.png' alt='img_007' width='600'/>

Select next:

<img src='./images/img_008.png' alt='img_008' width='600'/>

Select install:

<img src='./images/img_009.png' alt='img_009' width='600'/>

Select finish and run the Arduino IDE:

<img src='./images/img_010.png' alt='img_010' width='600'/>

The Arduino IDE will prompt for access to networks, select allow:

<img src='./images/img_011.png' alt='img_011' width='600'/>

Select allow:

<img src='./images/img_012.png' alt='img_012' width='600'/>

Windows will display a User Account Control Prompt when the Arduino IDE driver installer launches. Select yes:

<img src='./images/img_013.png' alt='img_013' width='200'/>

Select Install and always trust software from Adafruit Industries:

<img src='./images/img_014.png' alt='img_014' width='300'/>

Select Install and always trust software from Arduino srl:

<img src='./images/img_015.png' alt='img_015' width='300'/>

Select Install and always trust software from Arduino sa:

<img src='./images/img_016.png' alt='img_016' width='300'/>

Select Install and always trust software from Arduino llc:

<img src='./images/img_017.png' alt='img_017' width='300'/>

Windows will display another User Account Control Prompt when the Arduino IDE driver installer launches. Select yes:

<img src='./images/img_018.png' alt='img_018' width='200'/>

The output at the bottom will display the status of the installed drivers:

<img src='./images/img_019.png' alt='img_019' width='600'/>

The drivers for the most common Arduino boards will be installed. Unfortunately the ESP32 Nano driver is not installed:

<img src='./images/img_020.png' alt='img_020' width='600'/>

Select Tools → Boards → Boards Manager:

<img src='./images/img_021.png' alt='img_021' width='600'/>

Search for Arduino ESP32 and select Install:

<img src='./images/img_022.png' alt='img_022' width='600'/>

Windows will display another User Account Control Prompt when the Arduino IDE driver installer launches. Select yes:

<img src='./images/img_023.png' alt='img_023' width='200'/>

Select Install and always trust software from ExpressIf Systems:

<img src='./images/img_024.png' alt='img_024' width='300'/>

The output at the bottom will display the status of the installed drivers:

<img src='./images/img_025.png' alt='img_025' width='600'/>

In the Device Manager, USB Serial Device Displays as COM3:

<img src='./images/img_026.png' alt='img_026' width='600'/>

Under select board, select the Arduino Nano ESP32 (1-6):

<img src='./images/img_027.png' alt='img_027' width='600'/>

The selected board will now display:

<img src='./images/img_028.png' alt='img_028' width='600'/>

Select File → Examples → 01. Basics → Blink:

<img src='./images/img_029.png' alt='img_029' width='600'/>

Upload the sketch by pressing the upload button:

<img src='./images/img_030.png' alt='img_030' width='600'/>

Upload progress will be down in the Arduino IDEs Output:

<img src='./images/img_031.png' alt='img_031' width='600'/>

If the upload is unsuccessful. Press the reset button on the ESP32 Nano twice and reconnect to the Arduino ESP32 and then retry the upload.

If successful the yellow test LED will blink:

<img src='./images/img_032.png' alt='img_032' width='400'/>

The Arduino IDE uses C++. The code can be examined, there is an initial setup function which essentially defines pins and variables and a loop which carries out a repeated set of tasks, in this case flashing the test LED. The time to turn the LED On and Off can be modified and changes should be observed on the test LED:

<img src='./images/img_033.png' alt='img_033' width='600'/>

## MicroPython Installer for Arduino

The ESP32 device firmware should be upgraded to the latest version, so that it recognises commands in the latest version of MicroPython. Firmware updates are listed on GitHub. On Windows download the Windows Setup:

* [GitHub: MicroPython Firmware Installer for Arduino](https://github.com/arduino/lab-micropython-installer/releases)

<img src='./images/img_034.png' alt='img_034' width='600'/>

<img src='./images/img_035.png' alt='img_035' width='600'/>

Launch the application:

<img src='./images/img_036.png' alt='img_036' width='400'/>

Select the Arduino Nano ESP32 board and select Install MicroPython:

<img src='./images/img_037.png' alt='img_037' width='400'/>

The firmware will flash:

<img src='./images/img_038.png' alt='img_038' width='400'/>

Select OK:

<img src='./images/img_039.png' alt='img_039' width='600'/>

## Arduino Lab for MicroPython

The Arduino Lab for MicroPython is essentially a lightweight version of the Arduino IDE which uses Python instead of C++ to program the MicroController. It can be downloaded from Arduino. On Windows select the Windows Application:

* [Arduino Lab for MicroPython](https://labs.arduino.cc/en/labs/micropython)

<img src='./images/img_040.png' alt='img_040' width='600'/>

<img src='./images/img_041.png' alt='img_041' width='600'/>

Right click the zip file and select extract all...

<img src='./images/img_042.png' alt='img_042' width='400'/>

Select extract:

<img src='./images/img_043.png' alt='img_043' width='600'/>

Right click the second zip file and select extract all...

<img src='./images/img_044.png' alt='img_044' width='600'/>

Select extract:

<img src='./images/img_045.png' alt='img_045' width='600'/>

Launch the Arduino Lab for MicroPython application:

<img src='./images/img_046.png' alt='img_046' width='600'/>

Click into the main window:

<img src='./images/img_047.png' alt='img_047' width='600'/>

Create an Arduino MicroPython folder in Documents and select, select folder:

<img src='./images/img_048.png' alt='img_048' width='600'/>

Select the connect button:

<img src='./images/img_049.png' alt='img_049' width='600'/>

Select COM4:

<img src='./images/img_050.png' alt='img_050' width='600'/>

This will start a MicroPython Session which is ran from the ESP32 Nano. To the bottom a MicroPython shell displays with `>>>` indicating a new prompt. If the following code is input:

```python
>>> print('Hello World!')
Hello World!
```

The function `help` can be used to view a docstring. If no argument is supplied details about the `machine` and `network` module are shown:

```python
>>> help()
```
```
Welcome to MicroPython on the ESP32!

For online docs please visit http://docs.micropython.org/

For access to the hardware use the 'machine' module:

import machine
pin12 = machine.Pin(12, machine.Pin.OUT)
pin12.value(1)
pin13 = machine.Pin(13, machine.Pin.IN, machine.Pin.PULL_UP)
print(pin13.value())
i2c = machine.I2C(scl=machine.Pin(21), sda=machine.Pin(22))
i2c.scan()
i2c.writeto(addr, b'1234')
i2c.readfrom(addr, 4)

Basic WiFi configuration:

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)
For a list of available modules, type help('modules')
```

To view the other modules:

```python
>>> help('modules')
```

```
__main__          asyncio/funcs     gc                senml/senml_base
_asyncio          asyncio/lock      hashlib           senml/senml_pack
_boot             asyncio/stream    heapq             senml/senml_record
_espnow           binascii          inisetup          senml/senml_unit
_onewire          bluetooth         io                socket
_thread           btree             json              ssl
_webrepl          builtins          logging           struct
aioble/__init__   cbor2/__init__    machine           sys
aioble/central    cbor2/_decoder    math              time
aioble/client     cbor2/_encoder    micropython       time
aioble/core       cmath             mip/__init__      tls
aioble/device     collections       neopixel          uasyncio
aioble/l2cap      cryptolib         network           uctypes
aioble/peripheral deflate           ntptime           umqtt/robust
aioble/security   dht               onewire           umqtt/simple
aioble/server     ds18x20           os                upysh
aioespnow         errno             platform          urequests
apa106            esp               random            vfs
array             esp32             re                webrepl
asyncio/__init__  espnow            requests/__init__ webrepl_setup
asyncio/core      flashbdev         select            websocket
asyncio/event     framebuf          senml/__init__
Plus any modules on the filesystem
```

From the previous tutorials you should be familar with many of the standard modules:

* builtins
* collections
* math
* cmath
* array
* json
* io
* os
* sys
* time

The Micropython counterparts are often simplified versions of these modules. For example if the `sys` module is imported:

```python
>>> import sys
```

Its identifiers can be viewed by inputting:

```python
>>> sys.↹
```

```
argv            byteorder       exit            implementation
maxsize         modules         path            platform
print_exception                 ps1             ps2
stderr          stdin           stdout          version
version_info
```

If the version is examined:

```python
sys.version
> '3.4.0; MicroPython v1.24.1 on 2024-11-29'
```

Notice that the Python version is 3.4.0 and MicroPython version is 1.24.1. This means that the version of Python, that the MicroPython syntax is compatible with is Python 3.4.0 which is a little outdated. fstrings for example introduced in Python 3.6.0 for example will not work:

```python
>>> x = 2
>>> print(f'hello {x}')
hello 2
```

The older style of formatted strings works:

```python
>>> print('hello %d' % (x,))
hello 2
```

The platform can also be observed:

```python
>>> sys.platform
'esp32'
```

The machine module is imported using:

```python
>>> import machine
```

Its identifiers can be viewed by inputting:

```python
>>> machine.↹
```

```
ADC             ADCBlock        DEEPSLEEP       DEEPSLEEP_RESET
EXT0_WAKE       EXT1_WAKE       HARD_RESET      I2C
I2S             PIN_WAKE        PWM             PWRON_RESET
Pin             RTC             SDCard          SLEEP
SOFT_RESET      SPI             Signal          SoftI2C
SoftSPI         TIMER_WAKE      TOUCHPAD_WAKE   Timer
TouchPad        UART            ULP_WAKE        WDT
WDT_RESET       __dict__        bitstream       bootloader
deepsleep       dht_readinto    disable_irq     enable_irq
freq            idle            lightsleep      mem16
mem32           mem8            reset           reset_cause
sleep           soft_reset      time_pulse_us   unique_id
wake_reason
```

More details about the identifiers can be seen by inputting:

```python
>>> help(machine)
```

```
object <module 'machine'> is of type module
  __name__ -- machine
  mem8 -- <8-bit memory>
  mem16 -- <16-bit memory>
  mem32 -- <32-bit memory>
  unique_id -- <function>
  soft_reset -- <function>
  bootloader -- <function>
  reset -- <function>
  reset_cause -- <function>
  idle -- <function>
  freq -- <function>
  lightsleep -- <function>
  deepsleep -- <function>
  disable_irq -- <function>
  enable_irq -- <function>
  bitstream -- <function>
  dht_readinto -- <function>
  time_pulse_us -- <function>
  Signal -- <class 'Signal'>
  SoftI2C -- <class 'SoftI2C'>
  SoftSPI -- <class 'SoftSPI'>
  ADC -- <class 'ADC'>
  ADCBlock -- <class 'ADCBlock'>
  I2C -- <class 'I2C'>
  I2S -- <class 'I2S'>
  PWM -- <class 'PWM'>
  SPI -- <class 'SPI'>
  UART -- <class 'UART'>
  WDT -- <class 'WDT'>
  sleep -- <function>
  Timer -- <class 'Timer'>
  SDCard -- <class 'SDCard'>
  Pin -- <class 'Pin'>
  TouchPad -- <class 'TouchPad'>
  RTC -- <class 'RTC'>
  SLEEP -- 2
  DEEPSLEEP -- 4
  HARD_RESET -- 2
  PWRON_RESET -- 1
  WDT_RESET -- 3
  DEEPSLEEP_RESET -- 4
  SOFT_RESET -- 5
  wake_reason -- <function>
  PIN_WAKE -- 2
  EXT0_WAKE -- 2
  EXT1_WAKE -- 3
  TIMER_WAKE -- 4
  TOUCHPAD_WAKE -- 5
  ULP_WAKE -- 6
```

The docstring for some of the less commonly used functions is basic:

```python
>>> help(machine.sleep)
object <function> is of type function
```

The `machine.Pin` class can be examined:

```python
>>> help(machine.Pin)
```

```
object <class 'Pin'> is of type type
  init -- <function>
  value -- <function>
  off -- <function>
  on -- <function>
  irq -- <function>
  board -- <class 'board'>
  IN -- 1
  OUT -- 3
  OPEN_DRAIN -- 7
  PULL_UP -- 2
  PULL_DOWN -- 1
  IRQ_RISING -- 1
  IRQ_FALLING -- 2
  WAKE_LOW -- 4
  WAKE_HIGH -- 5
  DRIVE_0 -- 0
  DRIVE_1 -- 1
  DRIVE_2 -- 2
  DRIVE_3 -- 3
```

Notice the initialisation method is shown as `init` opposed to `__init__`:

```python
>>> help(machine.Pin.init)
object <function> is of type function
```

```python
>>> help(machine.Pin.__init__)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: type object 'Pin' has no attribute '__init__'
``` 

The following Information from Arduino gives details about the Nano ESP32:

* [Nano ESP32 (ABX00083)](https://docs.arduino.cc/hardware/nano-esp32/)

Specifically the Pin Layout:

* [Nano ESP32 (ABX00083) Full Pinout](https://docs.arduino.cc/resources/pinouts/ABX00083-full-pinout.pdf)

The following link gives a more detailed overview of MicroPython commands that can be used with the ESP32:

* [MicroPython: Quick Reference for the ESP32](https://docs.micropython.org/en/latest/esp32/quickref.html)

The Pin layout shows `GPIO48 LED_BUILTIN` for the test LED. GPIO is an abbreviation for General Purpose Input Output and 48 is the pin number. The test LED is an output device, because it outputs light in response to an electrical signal. `LED_BUILTIN` is a variable name for the pin which is predefined but only in C++. 

The MicroPython: Quick Reference for the ESP32 Documentation, gives the following details about the `Pin` class:

```
from machine import Pin

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation
p6 = Pin(6, Pin.OUT, drive=Pin.DRIVE_3) # set maximum drive strength
```

Therefore `Pin` can be imported directly and the `test_led` can be intialised using its pin number `48` and assigned to an output pin:

```python
>>> from machine import Pin
>>> test_led = Pin(48, Pin.OUT)
```

It can be turned on using:

```python
>>> test_led.on()
```

And back off using:

```python
>>> test_led.off()
```


The `machine` module has a `sleep`, `lightsleep` and `deepsleep` function. Using `sleep` and `deepsleep` will put the esp32 into a power saving mode and disconnect the communication between the ArduinoLab for MicroPython and the ESP32 board. Instead it is recommended to import the `time` module separately:

```python
>>> import time
>>> time.↹
```

```
const           __dict__        __file__        gmtime
localtime       mktime          sleep           sleep_ms
sleep_us        ticks_add       ticks_cpu       ticks_diff
ticks_ms        ticks_us        time            time_ns
__version__     strftime
```

It is common to enable an output device and then sleep for a specified of time, for example 10 seconds. During the 10 seconds, the cursor will look as follows:

```python
>>> test_led.on()
>>> time.sleep(10)
▮
```

Before displaying a new prompt:

It is common to enable an output device and then sleep for a specified of time, for example 10 seconds. During the 10 seconds, the cursor will look as follows:

```python
>>> test_led.on()
>>> time.sleep(10)
>>>
```

So now the test_led can be turned off using:

```
It is common to enable an output device and then sleep for a specified of time, for example 10 seconds. During the 10 seconds, the cursor will look as follows:

```python
>>> test_led.off()
```

If the following is placed in the script editor:

```python
test_led.on()
time.sleep(10)
test_led.off()
```

The script can be run and now the LED will be on for 10 seconds before switching off.


These commands can be added to the script editor and run:

```python
for num in range(10):
    print(num)
    test_led.on()
    time.sleep(1)
    test_led.off()
```

Putting this together:

```python
# Initialise
from machine import Pin
import time
test_led = Pin(48, Pin.OUT)
print('\n') 
test_led.off()

# Active
print('test led')
time.sleep(3)
test_led.on()
```

This sketch turns the test LED off initially and then after 3 seconds turns it on. Instead of the test LED at pin 48, the red LED in pin 46 can be used:

```python
# Initialise
from machine import Pin
import time
red_led = Pin(46, Pin.OUT)
print('\n') 
red_led.off()

# Active
print('red led')
time.sleep(3)
red_led.on()
```

This sketch works different to the above because the red LED is active low, so switching the pin off, will illuminate the LED and switching the pin on, will turn the LED off. The red pin can be initialised to on and the LED can be made to flash for 3 seconds:

```python
# Initialise
from machine import Pin
import time

red_led = Pin(46, Pin.OUT)
print('\n') 
red_led.on()

# Active
print('red led')
time.sleep(3)
red_led.off()
time.sleep(3)
red_led.on()
```

the red LED is part of a RGB LED, which has red at pin 46, green at pin 0 and blue at pin 45:

```python
# Initialise
from machine import Pin
import time

red_led = Pin(46, Pin.OUT)
green_led = Pin(0, Pin.OUT)
blue_led = Pin(45, Pin.OUT)
print('\n') 
red_led.on()
green_led.on()
blue_led.on()

# Active
print('RGB led')
time.sleep(3)
red_led.off()
time.sleep(3)
red_led.on()

time.sleep(3)
green_led.off()
time.sleep(3)
green_led.on()

time.sleep(3)
blue_led.off()
time.sleep(3)
blue_led.on()
```

The above sketches turns the red LED on for 3 s, the green LED on for 3 s and then the blue LED on for 3 s.



These LEDs are primary colors and secondary colors can be created by turning on two of the LEDs at the same time:

```python
# Initialise
from machine import Pin
import time

red_led = Pin(46, Pin.OUT)
green_led = Pin(0, Pin.OUT)
blue_led = Pin(45, Pin.OUT)
print('\n') 
red_led.on()
green_led.on()
blue_led.on()

# Active
print('RGB led')
print('primary: red')
time.sleep(3)
red_led.off()
time.sleep(3)
red_led.on()

print('primary: green')
time.sleep(3)
green_led.off()
time.sleep(3)
green_led.on()

print('primary: blue')
time.sleep(3)
blue_led.off()
time.sleep(3)
blue_led.on()

print('secondary: cyan')
time.sleep(3)
blue_led.off()
green_led.off()
time.sleep(3)
blue_led.on()
green_led.on()

print('secondary: magenta')
time.sleep(3)
red_led.off()
blue_led.off()
time.sleep(3)
red_led.on()
blue_led.on()

print('secondary: yellow')
time.sleep(3)
red_led.off()
green_led.off()
time.sleep(3)
red_led.on()
green_led.on()

print('white')
time.sleep(3)
red_led.off()
green_led.off()
blue_led.off()
time.sleep(3)
red_led.on()
green_led.on()
blue_led.on()
```









































<img src='./images/img_051.png' alt='img_051' width='600'/>
<img src='./images/img_052.png' alt='img_052' width='600'/>
<img src='./images/img_053.png' alt='img_053' width='600'/>
<img src='./images/img_054.png' alt='img_054' width='600'/>
<img src='./images/img_055.png' alt='img_055' width='600'/>
<img src='./images/img_056.png' alt='img_056' width='600'/>
<img src='./images/img_057.png' alt='img_057' width='600'/>
<img src='./images/img_058.png' alt='img_058' width='600'/>
<img src='./images/img_059.png' alt='img_059' width='600'/>
<img src='./images/img_060.png' alt='img_060' width='600'/>
<img src='./images/img_061.png' alt='img_061' width='600'/>
<img src='./images/img_062.png' alt='img_062' width='600'/>
<img src='./images/img_063.png' alt='img_063' width='600'/>
<img src='./images/img_064.png' alt='img_064' width='600'/>
<img src='./images/img_065.png' alt='img_065' width='600'/>
<img src='./images/img_066.png' alt='img_066' width='600'/>
<img src='./images/img_067.png' alt='img_067' width='600'/>
<img src='./images/img_068.png' alt='img_068' width='600'/>
<img src='./images/img_069.png' alt='img_069' width='600'/>












## Blink Test

The blink test was previously examined using C++ and the Arduino IDE. It can now be done with Python:

```python
from machine import Pin, sleep

# Set Variables
# Define the GPIO pins for the yellow LED
yellow_pin = Pin(48, Pin.OUT)


# Turn the LED On
yellow_pin.value(1)
```
























## Installing the Driver

Details about establishing a Serial Conenction is available in:

* [ExpressIf Connect ESP32-S3 to PC](https://docs.espressif.com/projects/esp-idf/en/stable/esp32s3/get-started/establish-serial-connection.html#flash-using-uart)

##

```
conda create -n esptool-env esptool
conda activate esptool-env
python -m esptool
```















To install the driver for the Arduino Nano ESP32, install the Arduino IDE:

* [Arduino IDE](https://www.arduino.cc/en/software)








## Stuff

https://dl.espressif.com/dl/esp-idf/



















```python
from machine import Pin, sleep

# Set Variables

# Define the GPIO pins for the yellow LED
yellow_pin = Pin(48, Pin.OUT)

# Define the GPIO pins for the RGB LED
red_pin = Pin(46, Pin.OUT)
green_pin = Pin(0, Pin.OUT)
blue_pin = Pin(45, Pin.OUT)

# Turn Test LEDs Off
def turn_leds_off():
    # Yellow LED is Active High
    yellow_pin.value(0)
    # RGB LED is Active Low
    red_pin.value(1)
    green_pin.value(1)
    yellow_pin.value(1)

try:
    turn_leds_off()
    yellow_pin.value(1)
    sleep(1000)


except KeyboardInterrupt:
    turn_leds_off()

















# Turn Test LEDs Off
# Yellow LED is Active High
yellow_pin.value(0)
# RGB LED is Active High
red_pin.value(0)
green_pin.value(0)
yellow_pin.value(0)


# Turn Yellow LED on for 1 second
yellow_pin.value(1)
sleep(1000)
yellow_pin.value(0)

# Turn Red LED on for 1 second
red_pin.value(0)
sleep(1000)
red_pin.value(1)

# Turn Green LED on for 1 second
green_pin.value(0)
sleep(1000)
green_pin.value(1)

# Turn Green LED on for 1 second
blue_pin.value(0)
sleep(1000)
blue_pin.value(1)
```