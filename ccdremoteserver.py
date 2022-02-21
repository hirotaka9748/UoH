# Import the .NET class library
import clr

# Import python sys module
import sys

# Import os module
import os

# Import System.IO for saving and opening files
from System.IO import *

# Import c compatible List and String
from System import String
from System.Collections.Generic import List

# Add needed dll references
sys.path.append(os.environ['LIGHTFIELD_ROOT'])
sys.path.append(os.environ['LIGHTFIELD_ROOT']+"\\AddInViews")
clr.AddReference('PrincetonInstruments.LightFieldViewV5')
clr.AddReference('PrincetonInstruments.LightField.AutomationV5')
clr.AddReference('PrincetonInstruments.LightFieldAddInSupportServices')

# PI imports
from PrincetonInstruments.LightField.Automation import Automation
from PrincetonInstruments.LightField.AddIns import ExperimentSettings
from PrincetonInstruments.LightField.AddIns import DeviceType

# TCP communication
import socket
from datetime import datetime
from time import sleep

s = socket.socket()
port = 7834
s.bind(('localhost', port))

def save_file(filename):    
    # Set the base file name
    experiment.SetValue(
        ExperimentSettings.FileNameGenerationBaseFileName,
        Path.GetFileName(filename))
    
    # Option to Increment, set to false will not increment
    experiment.SetValue(
        ExperimentSettings.FileNameGenerationAttachIncrement,
        False)

    # Option to add date
    experiment.SetValue(
        ExperimentSettings.FileNameGenerationAttachDate,
        False)

    # Option to add time
    experiment.SetValue(
        ExperimentSettings.FileNameGenerationAttachTime,
        False)

def device_found():
    # Find connected device
    for device in experiment.ExperimentDevices:
        if (device.Type == DeviceType.Camera):
            return True
     
    # If connected device is not a camera inform the user
    print("Camera not found. Please add a camera and try again.")
    return False  

def ccdexposure(filename):
    if (device_found()==True):        
        # Check this location for saved spe after running
        _file_name = filename

        # Pass location of saved file
        save_file(_file_name)

        # Acquire image
        experiment.Acquire()

        # Sleep for data recording
        sleep(3)

def setexptime(exposuretime):
    if (device_found()==True): 
        #Set exposure time
        set_value(CameraSettings.ShutterTimingExposureTime, exposuretime)

def isreadytorun():
    if (device_found()==True): 
        return experiment.IsReadyToRun
    
# Create the LightField Application (true for visible)
# The 2nd parameter forces LF to load with no experiment 
#auto = Automation(True, List[String]())

# Get experiment object
#experiment = auto.LightFieldApplication.Experiment

# ==========================================================

while True:
    print('listening')
    s.listen(5)
    c, addr = s.accept()
    print('receiving')
    rcvmsg=(c.recv(4096)).decode()
    print(rcvmsg)
    if (rcvmsg[0]=="a"):
        print("acquire "+rcvmsg[1:])
        #ccdexposure(rcvmsg[1:])
        c.send(b"acquire")
    elif (rcvmsg[0]=="e"):
        exposuretime=float(rcvmsg[1:])
        print("exposure time "+str(exposuretime))
        #setexptime(exposuretime)
        c.send(b"exposure time setting")
    elif (rcvmsg=="d"):
        print("d")
        c.send(b"d")
        break;
    elif (rcvmsg[0]=="r"):
        print("IsReadyToRun?")
        #putmsg=isreadytorun()
        putmsg=1
        print(putmsg)
        try:
            c.send((str(putmsg)).encode())
        except:
            break
    else :
        print(rcvmsg)
    c.close()
s.close()

