import socket,json,time,serial
import serial.tools.list_ports
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import QTimer,QTime
import sys
import gui
import threading
import bluetooth


neuroSocket = None
ser = None
sock = None
direction = 0
flag=0
counter=2
isMoving = False
isArduinoSetup = False
blinkc=0
#sem = threading.Semaphore(1)

class WheelchairControl(QtGui.QMainWindow, gui.Ui_MainWindow):
    def __init__(self):
        
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined    
        self.imageLabel.setFont(QtGui.QFont("Droid Sans",48,QtGui.QFont.Bold))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.connectToArduino()
        self.setupDevice()
        self.tick()
        
    def setupHW(self):
        
        print "Connecting to Arduino"
        self.statusLabel.setText("Connecting to Arduino")
        self.connectToArduino()
        print "Connected to Arduino"
        self.statusLabel.setText("Connected to Arduino")
        self.setupDevice()

    def tick(self):
        
        self.timer=QTimer()
        self.timer.timeout.connect(self.lcdDisplay)
        self.timer.start(1000)

    def change(self):
        #print 'change'
        global isMoving, flag, direction 
        self.imageLabel.setFont(QtGui.QFont("Droid Sans",48,QtGui.QFont.Bold))
        self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)
        #for color change
        #self.imageLabel.setStyleSheet("color: rgb(255,0,0)")
        #print "Moving",isMoving
        #print "Flag",flag
        if isArduinoSetup:
            if isMoving:
                self.currentCommand("Moving")
                self.statusLabel.setText("Selected direction is")
                if direction==0:
                        self.imageLabel.setText("RIGHT")
                        #ser.write("4")
                        sock.send("4")
                        print "right selected"
                        #for image display
                        #self.imageLabel.setStyleSheet("image: url(:/Directions/images/right.jpg)")
                
                elif direction==1:
                    self.imageLabel.setText("LEFT")
                    print "left selected"
                    #ser.write("3")
                    sock.send("3")
                    #isMoving = False
                
                else:
                    self.imageLabel.setText("FORWARD")
                    print "forward selected"
                    #ser.write("2")
                    sock.send("2")
                    #isMoving = False
                
            else:
                    self.currentCommand("Stopped")
                    self.statusLabel.setText("Double blink to select direction")
                    #ser.write("1")
                    sock.send("1")
                    if flag==0:
                        self.imageLabel.setText("RIGHT")
                        direction = 0
                        flag=1
                    elif flag==1:
                        self.imageLabel.setText("LEFT")
                        direction = 1
                        flag=2
                    else:
                        #isMoving = True
                        self.imageLabel.setText("FORWARD")
                        direction = 2
                        flag=0
        #sem.release()

    def lcdDisplay(self):
        global counter,blinkc
        if counter==0:
            blinkc=0
            text=str(counter)
            self.lcdNumber.display(text)
            counter=2
            
            #sem.acquire()
            self.change()
        else:
           text=str(counter)
           counter-=1
           self.lcdNumber.display(text)

    def currentCommand(self, command):
        self.currentLabel.setFont(QtGui.QFont("Droid Sans",14,QtGui.QFont.Bold))
        self.currentLabel.setAlignment(QtCore.Qt.AlignCenter)
        #for color change
        self.currentLabel.setStyleSheet("color: rgb(85,0,255)")
        self.currentLabel.setText(command)

    def connectToArduino(self):
        global ser, sock

        #print "Searching for devices..."
        #print ""
        
        nearby_devices = bluetooth.discover_devices(duration=1,flush_cache=True)
        num = 0
        
        #print "Select your device by entering its coresponding number..."
        for i in nearby_devices:
                num+=1
                #print num , ": " , bluetooth.lookup_name( i )
                if(str(bluetooth.lookup_name(i)) == "HC-05"):
                    selection = int(num - 1)
                    break
        print "You have selected", bluetooth.lookup_name(nearby_devices[selection])
        bd_addr = nearby_devices[selection]
        sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        a = sock.connect((bd_addr, port))
        
    def setupDevice(self):

        global isArduinoSetup
        ######30 sec delay
        delay = 30
        print "Setting up device"
        self.statusLabel.setText("Setting up device")
        start=time.time()
        diff=0
        prevNum = delay

        
        
        '''
        while diff<delay and not stopEvent.is_set():
            rep = neuroSocket.recv(1024)
            diff=time.time()-start
            currNum = int(delay-diff)
            if(prevNum != currNum):
                prevNum = currNum
                print currNum
        '''
        '''
        while(sock.recv() != '1'):
            rep = neuroSocket.recv(1024)
        '''
        isArduinoSetup = True
        print "Done"

    def myfunc(self):
        print "I am func"
        self.statusLabel.setFont(QtGui.QFont("Droid Sans",14,QtGui.QFont.Bold))
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setText("Current Status")
    
    def setupHardware(self,stopEvent):
        global neuroSocket, isArduinoSetup

        try:

            self.myfunc()
            #connect to neurosky mindwave
            print "Waiting for MindWave"
            self.statusLabel.setText("Waiting for MindWave")
            self.connectToNeurosky()
            if(neuroSocket != None):
                print "Connected to Neurosky MindWave"
                self.statusLabel.setText("Connected to Neurosky MindWave")
                while(not isArduinoSetup):
                    pass
                self.receiveData(stopEvent)
                #connect to arduino
                #print "Connecting to Arduino"
                #self.statusLabel.setText("Connecting to Arduino")
                #self.connectToArduino()
                
                #receive data
                #if(sock != None):

                   # self.setupDevice(stopEvent)
                    
                   # print "Connected to Arduino"
                   # self.statusLabel.setText("Connected to Arduino")
                   # isArduinoSetup = True

                #else:
                #    print "Arduino not available"
                #    self.statusLabel.setText("Arduino not available")
            else:
                print "Error connecting to MindWave"
                self.statusLabel.setText("Error connecting to MindWave")

        except KeyboardInterrupt:
            print "Program Terminated"
        except Exception:
            tb = sys.exc_info()
            print "Exception"
            if("actively refused" in str(tb[1])):
                print "ThinkGear is not running!"
            elif("COM" in str(tb[1])):
                print "COM Port is busy"
            else:
                print tb[1]

    def connectToNeurosky(self):
        global neuroSocket
        neuroSocket = socket.create_connection(("127.0.0.1",13854))
        data = '{"appName":"appName","appKey":"appKey"}'
        formatt = '{"enableRawOutput":true,"format":"Json"}'
        r = neuroSocket.sendall(formatt)
        print "Device Response",r                     

        
    def receiveData(self, stopEvent):
        global isMoving, counter,blinkc,sock
        
        timeDiff=0
        flag = 1
        twoBlink=False
        blinkc=0
        while not stopEvent.is_set():
            rep = neuroSocket.recv(1024)    
            '''
            if("poor" in rep):
                rep = rep.split('\r')
                for data in rep:
                    if("raw" in data or "mental" in data):                                  #skip unwanted values
                        continue
                    if(len(data)>10):                                                       #avoid partial data, WIP
                        #print data
                        parsed_data=json.loads(data)
                        if('poorSignalLevel' in parsed_data):
                            if(parsed_data['poorSignalLevel'] > 0):
                                flag = 1
                                print "Poor Signal Detected. MindWave incorrectly placed."
                                print "Signal Strength :",parsed_data['poorSignalLevel']
                            else:
                                if(flag):
                                    flag = 0
                                    print "Connection Secured."
                        #if('blinkStrength' in parsed_data):
                        #    print "Blink Strength :",parsed_data['blinkStrength']
            '''
            if("blink" in rep):
                #if(counter == 0):
                    #start=time.time()
                 #   blinkc=0
                    
                print "blink"
                
                blinkc=blinkc+1
                print "Count :",blinkc
                if(blinkc == 2):
                    
                    #timeDiff=time.time()- start
                    #print "Start",start
                    #print "Diff",timeDiff
                    #if timeDiff<=1:                                 #1 sec interval for detecting 2 blinks
                    print "Two Blinks Detected ",blinkc
                        #twoblink=True
                    counter = 0
                    if(isMoving):                               #previous moving (any direction) then stop
                        print "Stop"
                        #sock.send("1")
                        isMoving = False
                        
                        #sem.acquire()
                        #self.change()                          #to immediately display stop (1 sec delay)
                        #self.imageLabel.setText("STOP")
                        #ser.write(stop)
                        
                    else:                                       #call gui for selecting direction
                        #GUI function
                        isMoving = True
                        #self.change()
                        pass
                    #timeDiff = 0
                    #blinkc=0
                    #else:
                     #   print "No Blink"
                      #  blinkc=0


    #        if("eSense" in rep):
    #            rep = rep.split('\r')
    #            for data in rep:
    #                print data


def main(app, form):

        #open an instance of QApplication
        
        #app = QtGui.QApplication(sys.argv)
        #form = WheelchairControl()
        form.show()
        #form.setupHW()
        app.exec_()
        
        
        

if __name__ == '__main__':

    try:
        app = QtGui.QApplication(sys.argv)
        form = WheelchairControl()
        
        stopEvent = threading.Event()
        t = threading.Thread(target=form.setupHardware,args=(stopEvent,))
        t.daemon = True
        t.start()

        main(app, form)
        
    except KeyboardInterrupt:
            print "Program Terminated"
    except Exception:
        tb = sys.exc_info()
        print "Exception"
        print tb

    finally:
        print "Clean up"
        stopEvent.set()
        if(ser != None):
            print "Port Closed"
            ser.close()
        if(neuroSocket != None):
            neuroSocket.close()
        print "System Shutdown"    

