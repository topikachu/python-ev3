from ctypes import sizeof
from mmap import mmap, MAP_SHARED, PROT_READ, PROT_WRITE
import os
import struct

from . import lms2012


_initialized=False
_pwmfile=None
_motorfile=None
_motormm=None
_motodata=None

"""
opOUTPUT_GET_TYPE     LAYER   NO       *TYPE                                   // Get output device type
opOUTPUT_SET_TYPE     LAYER   NO       TYPE                                    // Set output device type
opOUTPUT_RESET        LAYER   NOS                                              // Reset position  (POS=0)
opOUTPUT_STOP         LAYER   NOS      BRAKE                                   // Stop outputs    (brake or coast)
opOUTPUT_POWER        LAYER   NOS      POWER                                   // Set power       (suspend regulation and positioning)
opOUTPUT_SPEED        LAYER   NOS      SPEED                                   // Set speed (relative to polarity - enables regulation if tacho)
opOUTPUT_START        LAYER   NOS                                              // Starts outputs from present values
opOUTPUT_POLARITY     LAYER   NOS      POL                                     // Set polarity    (0=toggle)
opOUTPUT_READ         LAYER   NOS      *SPEED *STEPS                           // Read actual speed and steps from last reset
opOUTPUT_TEST         LAYER   NOS      *Busy                                   //
opOUTPUT_READY        LAYER   NOS                                              // Wait for new action completed or overruled
opOUTPUT_POSITION     LAYER   NOS      POS                                     // Set position    (absolute from last reset)

opOUTPUT_STEP_POWER   LAYER   NOS      POWER   STEP1   STEP2   STEP3   BRAKE   // Set all parameters, start if not started and power != 0
opOUTPUT_TIME_POWER   LAYER   NOS      POWER   TIME1   TIME2   TIME3   BRAKE   // Set all parameters, start if not started and power != 0
opOUTPUT_STEP_SPEED   LAYER   NOS      SPEED   STEP1   STEP2   STEP3   BRAKE   // Set all parameters, start if not started and power != 0
opOUTPUT_TIME_SPEED   LAYER   NOS      SPEED   TIME1   TIME2   TIME3   BRAKE   // Set all parameters, start if not started and power != 0
opOUTPUT_STEP_SYNC    LAYER   NOS      SPEED   TURN    STEP    BRAKE           // Set all parameters, start if not started and power != 0
opOUTPUT_TIME_SYNC    LAYER   NOS      SPEED   TURN    TIME    BRAKE           // Set all parameters, start if not started and power != 0
opOUTPUT_CLR_COUNT    LAYER   NOS                                              // Clears the tacho count used when in sensor mode
opOUTPUT_GET_COUNT    LAYER   NO       *STEPS                                  // Gets the tacho count used in sensor mode
"""

def open_device():
    global _initialized
    if not _initialized:
        global _pwmfile
        _pwmfile=os.open(lms2012.PWM_DEVICE_NAME,os.O_RDWR)
        global _motorfile
        _motorfile=os.open(lms2012.MOTOR_DEVICE_NAME,os.O_RDWR)
        MOTORDATAArrray=lms2012.MOTORDATA * 4
        global _motormm
        _motormm=mmap(fileno=_motorfile, length=sizeof(MOTORDATAArrray),flags=MAP_SHARED,prot=PROT_READ | PROT_WRITE, offset=0)    
        global _motodata
        _motodata=MOTORDATAArrray.from_buffer(_motormm)
        _initialized=True
        os.write(_pwmfile, struct.pack('B',lms2012.opPROGRAM_START))

def set_types(types):
    os.write(_pwmfile, struct.pack('5B',lms2012.opOUTPUT_SET_TYPE, *types))
def reset(ports):
    os.write(_pwmfile, struct.pack('2B',lms2012.opOUTPUT_RESET, ports))
def start(ports):
    os.write(_pwmfile, struct.pack('2B',lms2012.opOUTPUT_START,ports))
def stop(ports,brake=0):
    os.write(_pwmfile, struct.pack('3B',lms2012.opOUTPUT_STOP,ports,brake))
def power(ports,power):
    os.write(_pwmfile, struct.pack('3B',lms2012.opOUTPUT_POWER,ports,power))
def speed(ports,speed):
    os.write(_pwmfile, struct.pack('3B',lms2012.opOUTPUT_SPEED,ports,speed))
def polarity(ports,polarity=1):
    os.write(_pwmfile, struct.pack('3B',lms2012.opOUTPUT_POLARITY,ports,polarity))
    
def test(ports):
    pass
def ready(ports):
    pass

#def position(ports,pos):
#    os.write(_pwmfile, struct.pack('2B',lms2012.opOUTPUT_START,ports))
       
def step_power(ports, power, ramp_up_steps, const_speed_steps,ramp_down_steps,brake=0):
    steppoweer=lms2012.STEPPOWER()
    steppoweer.Cmd=lms2012.opOUTPUT_STEP_POWER
    steppoweer.Nos    =  ports
    steppoweer.Power  = power
    steppoweer.Step1  =  ramp_up_steps
    steppoweer.Step2  =  const_speed_steps;
    steppoweer.Step3  =  ramp_down_steps;
    steppoweer.Brake  =  brake;
    os.write(_pwmfile,steppoweer)
    
    
def time_power(ports, power, ramp_up_time, const_speed_time,ramp_down_time,brake=0):
    timepower=lms2012.TIMEPOWER()
    timepower.Cmd    =  lms2012.opOUTPUT_TIME_POWER;
    timepower.Nos    =  ports
    timepower.Power  =  power
    timepower.Time1  =  ramp_up_time
    timepower.Time2  =  const_speed_time
    timepower.Time3  =  ramp_down_time
    timepower.Brake  =  brake
    os.write(_pwmfile,timepower)
    
def step_speed(ports, speed, ramp_up_steps, const_speed_steps,ramp_down_steps,brake=0):
    stepspeed = lms2012.STEPSPEED()
    stepspeed.Cmd    =   lms2012.opOUTPUT_STEP_SPEED;
    stepspeed.Nos    =  ports;
    stepspeed.Speed  = speed;
    stepspeed.Step1  =  ramp_up_steps;
    stepspeed.Step2  =  const_speed_steps;
    stepspeed.Step3  =  ramp_down_steps;
    stepspeed.Brake  =  brake;
    os.write(_pwmfile,stepspeed)
def time_speed(ports, speed, ramp_up_time, const_speed_time,ramp_down_time,brake=0):
    timespeed = lms2012.TIMESPEED()
    timespeed.Cmd    =  lms2012.opOUTPUT_TIME_SPEED;
    timespeed.Nos    =  ports
    timespeed.Speed  =  speed
    timespeed.Time1  = ramp_up_time
    timespeed.Time2  =  const_speed_time
    timespeed.Time3  =  ramp_down_time
    timespeed.Brake  =  brake
    os.write(_pwmfile,timespeed)
    
def step_sync(ports, speed, turn=0, step=0,brake=0):
    stepsync= lms2012.STEPSYNC()
    stepsync.Cmd   =   lms2012.opOUTPUT_STEP_SYNC;
    stepsync.Nos   =  ports
    stepsync.Speed =  speed
    stepsync.Turn  =  turn
    stepsync.Step  =  step
    stepsync.Brake =  brake
    os.write(_pwmfile,stepsync)

def time_sync(ports, speed, turn=0, time=0,brake=0):
    timesync=lms2012.TIMESYNC()
    timesync.Cmd   =  lms2012.opOUTPUT_TIME_SYNC;
    timesync.Nos   =  ports
    timesync.Speed =  speed
    timesync.Turn  =  turn
    timesync.Time  =  time
    timesync.Brake =  brake
    os.write(_pwmfile,timesync)


def clear_steps(ports):
    pass

def get_speed(port):
    return _motodata[port].Speed
def get_steps(port):
    return _motodata[port].TachoCounts



def close_device():
    global _initialized
    if _initialized:
        os.write(_pwmfile, struct.pack('B',lms2012.opPROGRAM_STOP))
        _motormm.close()
        os.close(_motorfile)
        os.close(_pwmfile)
        _initialized=False












