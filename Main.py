#PROM programmer reader&writer
#Author: Michal Basler
#Start date: 26.07.2022
#Last update: 26.07.2022
#Version: 1.0
#License: GPLv3

#importing modules
from ast import While
import sys
import os
import time
import serial
import serial.tools.list_ports
from pathlib import Path

debug = False
if len(sys.argv) > 1:
        if sys.argv[1] == "--debug":
            debug = True
    
         

ports = serial.tools.list_ports.comports()
RP_Baudrate = 115200

print("PROM programmer reader&writer")
print("Author: Michal Basler\n")

if debug == True:
    print("Debug mode enabled")
    print("\n")  
elif len(ports) == 0:
    print("No COM ports found. Please connect the programmer to the computer.")
    sys.exit()
else:
    print("Select COM port, on which the programmer is connected to:")

    for i in range(0,len(ports)):
            print("{}: {} ".format(i+1, ports[i]))

    while True:
        try:
                Selected_port = int(input("Enter number: "))
                if Selected_port > len(ports) or Selected_port < 0:
                        print("Invalid number")
                        continue
                break
        except ValueError:
                print("Invalid number")
                continue

    if Selected_port != 0:
        print("You selected: {}\n".format(ports[Selected_port-1]))
        print("Establishing connection...")
        time.sleep(1)
        Serial = serial.Serial(ports[Selected_port-1].device, RP_Baudrate)
        print("Connection established!\n")
        time.sleep(1)
    else:
        print("Fast debugging mode")
        DEBUGFLAG = True   
    

print("\nWhat do you want to do?")
print("1: Read PROM")
print("2: Write PROM")
print("3: Exit\n")


while True:
        try:
                Choice = int(input("Enter number: "))
                if Choice > 3 or Choice < 1:
                        print("Invalid number")
                        continue
                break
        except ValueError:
                print("Invalid number")
                continue




if Choice == 3:
        print("Exiting...")
        time.sleep(1)
        sys.exit()
elif Choice == 1:
    print("Entering read mode...\n")
elif Choice == 2:
    print("Entering write mode...\n")

time.sleep(1)

ReadLibrary = open(os.path.join(sys.path[0],"Library.txt"), "r")
ReadLibrary_lines = len(ReadLibrary.readlines())
print("Number of PROMs in library: {}".format(ReadLibrary_lines))
print("\nChoose PROM:")

ReadLibrary.seek(0)
for i in range(0,ReadLibrary_lines):
    print("{}: {}".format(i+1, (ReadLibrary.readline()).split("_")[0]))

ReadLibrary.seek(0)

while True:
        try:
                PROM_Choice = int(input("Enter number: "))
                ReadLibrary.seek(0)
                if PROM_Choice > ReadLibrary_lines or PROM_Choice < 1:
                        print("Invalid number")
                        continue
                break
        except ValueError:
                print("Invalid number")
                continue


#PROM_Choice = int(input("\nEnter number: "))
ReadLibrary.seek(0)
Chosen = (ReadLibrary.readlines()[PROM_Choice-1])
print("\nYou have selected: {}".format(Chosen.split("_")[0]))
print("Prepairing programmer with following settings: {}".format(Chosen.split("_")[1]))


