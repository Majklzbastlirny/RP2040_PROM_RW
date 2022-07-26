#PROM programmer reader&writer
#Author: Michal Basler
#Start date: 26.07.2022
#Last update: 26.07.2022
#Version: 1.0
#License: GPLv3

#importing modules
import sys
import os
import time
import serial
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
RP_Baudrate = 115200

print("PROM programmer reader&writer")
print("Author: Michal Basler\n")
print("Select COM port, on which the programmer is connected to:")

for i in range(0,len(ports)):
        print("{}: {} ".format(i+1, ports[i]))

Selected_port = int(input("Enter number: "))
print("You selected: {}".format(ports[Selected_port-1]))

print("Establishing connection...")
time.sleep(1)
Serial = serial.Serial(ports[Selected_port-1].device, RP_Baudrate)
print("Connection established!")
time.sleep(1)

print("What do you want to do?")
print("1: Read PROM")
print("2: Write PROM")
print("3: Exit")

Choice = int(input("Enter number: "))

if Choice == 3:
        print("Exiting...")
        time.sleep(1)
        sys.exit()
elif Choice == 1:
    print("Entering read mode...\n")
elif Choice == 2:
    print("Entering write mode...\n")
else:
    print("Invalid choice!")
    time.sleep(1)
    sys.exit()

ReadLibrary = open("Library.txt", "r")
ReadLibrary_lines = len(ReadLibrary.readlines())
print("Number of PROMs in library: {}".format(ReadLibrary_lines))
print("\nChoose PROM:")

ReadLibrary.seek(0)
for i in range(0,ReadLibrary_lines):
    print("{}: {}".format(i+1, ReadLibrary.readline()))

ReadLibrary.seek(0)
PROM_Choice = int(input("Enter number: "))
print("\nYou selected: {}".format(ReadLibrary.readlines()[PROM_Choice-1]))


