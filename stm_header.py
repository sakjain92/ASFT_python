#from common import *

# Base Address Definations 
STM_BASE_ADDR = 0xFBF58000
MC_CGM_BASE_ADDR = 0xFFFA8000
INTC_BASE_ADDR = 0xFFF50000
PSEUDO_REG_BASE_ADDR = 0x0

# STM bits Definations
STM_CHANNEL_EN_BIT = 31
STM_INTERRUPT_FLAG_BIT = 31
STM_TIMER_EN_BIT = 31
STM_FRZ_BIT = 30
STM_PRESCALER_BIT = 23
STM_PRESCALER_BIT_SIZE = 8

STM_INTERRUPT_BASE_VECTOR = 36

# INTC bits Defination 
INTC_VEC_BIT = 29
INTC_VEC_BIT_SIZE = 10

# MC_CGM bits Defination 
MC_CGM_DIVIDER_EN_BIT =  0
MC_CGM_DIV_BIT = 15
MC_CGM_DIV_BIT_SIZE = 6

# STM Channel defination 
class STM_channel_tag:
    CCR = None #Channel Control
    CIF = None #Channel Interrupt
    CMP = None #Channel Compare
    def __init__(self):
        self.CCR = None
        self.CIF = None
        self.CMP = None

# STM Defination 
class STM_tag:
    CR = None #Control
    CNT = None #Count
    CHANNEL = None
    def __init__(self):
        self.CR = None
        self.CNT = None
        self.CHANNEL = [STM_channel_tag(),STM_channel_tag(),STM_channel_tag(),STM_channel_tag()]

# INTC Definition 
class INTC_tag:
    IACKR0 = None
    def __init__(self):
        self.IACKR0=None


# MC_CGM Definition
class MC_CGM_tag:
    SC_DC2 = None
    def __init__(self):
        self.SC_DC2 = None

# Pseudo Regs Definition 
class PSEUDO_REG_tag:
    WAIT = None # PSEDUO for time increment 
    DEBUG = None; # Go into Debug Mode 
    # DEBUG_OFF; # Get out of Debug Mode # Single for Debug on and off 
    #POR # Issue POR # No longer supported 
    def __init__(self):
        self.WAIT = None
        self.DEBUG = None


# STM_STATE Deifinition 
class STM_STATE_tag:
    DEBUG_MODE=None
    def __init__(self):
        self.DEBUG_MODE=None

#Testing
if __name__ == "__main__":
    a=STM_STATE_tag()
    b=PSEUDO_REG_tag()
    c=MC_CGM_tag()
    d=INTC_tag()
    e=STM_tag()
    f=STM_channel_tag()

