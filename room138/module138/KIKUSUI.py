import pyvisa
import time
rm = pyvisa.ResourceManager()
inst1=rm.open_resource('TCPIP0::150.12.70.208::INSTR')
inst2=rm.open_resource('TCPIP0::150.12.70.156::INSTR')

############# KIKUSUI 右 ###################################

def currPlus(path1,curr2):
    path = path1
    curData1 = inst1.write("CURR"+"\t"+str(curr2))
    time.sleep(4)
    curData2 = inst1.query("MEAS:CURR?")
    Meas1 = repr(curData2)
    Meas2 = repr(curData2).strip('b')
    Meas3 = Meas2.replace("'","")
    print(Meas3)
    with open(path1, 'a') as f:
        print(Meas3,file=f)
    time.sleep(0.2)
    
def currMinus(path1,curr2):
    path = path1
    curData1 = inst1.write("CURR"+"\t"+str(curr2))
    time.sleep(4)
    curData2 = inst1.query("MEAS:CURR?")
    Meas1 = repr(curData2)
    Meas2 = repr(curData2).strip('b')
    Meas3 = Meas2.replace("'","")
    Meas4 = "-" + Meas3[1:]
    print(Meas4)
    with open(path1, 'a') as f:
        print(Meas4,file=f)
    time.sleep(0.2)
        
def curr0(path1):
    path = path1
    curData2 = inst1.query("MEAS:CURR?")
    Meas1 = repr(curData2)
    Meas2 = repr(curData2).strip('b')
    Meas3 = Meas2.replace("'","")
    print(Meas3)
    with open(path1, 'a') as f:
        print(Meas3,file=f)
    time.sleep(0.2)    
        
def volt(path1,volt2):
    path = path1
    curData1 = inst1.write("VOLT"+"\t"+str(volt2))
    time.sleep(4)
    curData2 = inst1.query("MEAS:VOLT?")
    Meas = repr(curData2)
    with open(path1, 'a') as f:
        print(Meas,file=f)
    time.sleep(0.2)    
    
def currOFF():
    curData=inst1.write("OUTP off")
    time.sleep(4)
    
def currON():
    curData=inst1.write("OUTP on")
    time.sleep(4)
    
############# KIKUSUI 左 ###################################

def teslaON():
    curData=inst2.write("OUTP on")
    time.sleep(4)
    
def teslaOFF():
    curData=inst2.write("OUTP off")
    time.sleep(4)
        
