import stp 
import common

SOLVER=None
STATE_DEBUG=None; # 1 bit
PSEUDO_DEBUG_REG=None
PSEUDO_DEBUG_BIT=None
PSEUDO_WAIT_REG=None

def init_solver():
    global SOLVER;
    SOLVER=stp.Solver()

def init_regs():
    global PSEUDO_DEBUG_REG
    PSEUDO_DEBUG_REG=common.REG(0x4)
    global PSEUDO_WAIT_REG
    PSEUDO_WAIT_REG=common.REG(0x0)

def statement_debug_off():
    global STATE_DEBUG
    global SOLVER
    PSEUDO_DEBUG_REG.value=SOLVER.bitvecval(1,0)

def statement_debug_on():
    global STATE_DEBUG
    global SOLVER
    STATE_DEBUG=SOLVER.bitvecval(1,1)

def condition_true():
    return 1
