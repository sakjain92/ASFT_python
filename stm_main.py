from common import *
from stm_header import *
import execution_header


# STM Declaration 
STM=STM_tag()

# INTC Declaration 
INTC=INTC_tag()

# MC_CGM Declaration
MC_CGM=MC_CGM_tag()

# PSEDUO_REG Declaration
PSEUDO_REG=PSEUDO_REG_tag()

# STM_STATE declaration
STM_STATE=STM_STATE_tag()

STM.CR              =reg("STM_CR"            ,0x00+STM_BASE_ADDR     ,32     ,0x00000000,0x0000ff03,0x0000ff03,0x000000,0x00000000)
STM.CNT             =reg("STM_CNT"           ,0x04+STM_BASE_ADDR     ,32     ,0x00000000,0xffffffff,0x00000000,0x000000,0x00000000)

STM.CHANNEL[0].CCR  =reg("STM_CHANNEL0_CCR"  ,0x10+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
STM.CHANNEL[0].CIF  =reg("STM_CHANNEL0_CIF"  ,0x14+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000000,0x000001,0x00000000)
STM.CHANNEL[0].CMP  =reg("STM_CHANNEL0_CMP"  ,0x18+STM_BASE_ADDR     ,32     ,0x00000000,0xffffffff,0xffffffff,0x000000,0x00000000)
STM.CHANNEL[1].CCR  =reg("STM_CHANNEL1_CCR"  ,0x20+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
STM.CHANNEL[1].CIF  =reg("STM_CHANNEL1_CIF"  ,0x24+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000000,0x000001,0x00000000)
STM.CHANNEL[1].CMP  =reg("STM_CHANNEL1_CMP"  ,0x28+STM_BASE_ADDR     ,32     ,0x00000000,0xffffffff,0xffffffff,0x000000,0x00000000)

STM.CHANNEL[2].CCR  =reg("STM_CHANNEL2_CCR"  ,0x30+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
STM.CHANNEL[2].CIF  =reg("STM_CHANNEL2_CIF"  ,0x34+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000000,0x000001,0x00000000)
STM.CHANNEL[2].CMP  =reg("STM_CHANNEL2_CMP"  ,0x38+STM_BASE_ADDR     ,32     ,0x00000000,0xffffffff,0xffffffff,0x000000,0x00000000)

STM.CHANNEL[3].CCR  =reg("STM_CHANNEL3_CCR"  ,0x40+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
STM.CHANNEL[3].CIF  =reg("STM_CHANNEL3_CIF"  ,0x44+STM_BASE_ADDR     ,32     ,0x00000000,0x00000001,0x00000000,0x000001,0x00000000)
STM.CHANNEL[3].CMP  =reg("STM_CHANNEL3_CMP"  ,0x48+STM_BASE_ADDR     ,32     ,0x00000000,0xffffffff,0xffffffff,0x000000,0x00000000)

# TODO: Reset value might be different as initializing in SoC  
#INTC.IACKR0         =reg("INTC_IACKRO"       ,0x20+INTC_BASE_ADDR    ,32     ,0x00000000,0xfffffffc,0xfffff000,0x000000,0x00000000)

MC_CGM.SC_DC2       =reg("MC_CGM_SC_DC2"     ,0xF0+MC_CGM_BASE_ADDR  ,32     ,0x80000000,0x803f0000,0x803f0000,0x000000,0x80000000)

#Making PSEUDO Regs non-writtable
PSEUDO_REG.WAIT     =reg("PSEUDO_REG_WAIT"  ,0x0+PSEUDO_REG_BASE_ADDR,32     ,0x00000000,0xffffffff,0x00000000,0x000000,0x00000000)
#PSEUDO_REG.POR      =reg("PSEUDO_REG_POR"   ,0x4+PSEUDO_REG_BASE_ADDR,32     ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
#PSEUDO_REG.DEBUG_ON =reg("PSEUDO_REG_DEBUG_ON",0x8+PSEUDO_REG_BASE_ADDR,32   ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
#PSEUDO_REG.DEBUG_OFF=reg("PSEUDO_REG_DBUG_OFF",0xC+PSEUDO_REG_BASE_ADDR,32   ,0x00000000,0x00000001,0x00000001,0x000000,0x00000000)
PSEUDO_REG.DEBUG    =reg("PSEUDO_REG_DEBUG",0xC+PSEUDO_REG_BASE_ADDR,32   ,0x00000000,0x00000001,0x00000000,0x000000,0x00000000) 
PSEUDO_REG.INTC     =reg("PSEUDO_REG_INTC"  ,0x10+PSEUDO_REG_BASE_ADDR,32    ,0x00000000,0xffffffff,0x00000000,0x000000,0x00000000)

ALL_REGS=[STM.CR ,STM.CNT ,STM.CHANNEL[0].CCR ,STM.CHANNEL[0].CIF ,STM.CHANNEL[0].CMP ,STM.CHANNEL[1].CCR ,STM.CHANNEL[1].CIF ,STM.CHANNEL[1].CMP ,STM.CHANNEL[2].CCR ,STM.CHANNEL[2].CIF ,STM.CHANNEL[2].CMP ,STM.CHANNEL[3].CCR ,STM.CHANNEL[3].CIF ,STM.CHANNEL[3].CMP ,MC_CGM.SC_DC2 ,PSEUDO_REG.WAIT ,PSEUDO_REG.DEBUG ,PSEUDO_REG.INTC ] 

STM_STATE.DEBUG_MODE    =reg("STATE_DEBUG_MODE"  ,0x100+PSEUDO_REG_BASE_ADDR,32    ,0x00000000,0xffffffff,0x00000000,0x000000,0x00000000)

def get_all_regs():
    global ALL_REGS
    return ALL_REGS

def init_reg_por():
    global ALL_REGS
    for reg in ALL_REGS:
        reg.val = change_bit_val(reg.val, reg.default, 31, 32)  
    STM_STATE.DEBUG_MODE.val=  change_bit_val(STM_STATE.DEBUG_MODE.val, STM_STATE.DEBUG_MODE.default, 31, 32)  
     

def set_interrupt(channel_no):
    # Set STM channel flag 
    STM.CHANNEL[channel_no].CIF.val=change_bit_val(STM.CHANNEL[channel_no].CIF.val,0x1,STM_INTERRUPT_FLAG_BIT,1)
    # Set INTC Vec Number 
    PSEUDO_REG.INTC.val=change_bit_val(PSEUDO_REG.INTC.val, 36 + channel_no,31,32)

def clear_interrupt(channel_no):
    # Clear STM channel interrupt flag 
    # TODO) Assuming STM channel disable doesn't effect interrupt 
    STM.CHANNEL[channel_no].CIF.val=change_bit_val(STM.CHANNEL[channel_no].CIF.val,0x0,STM_INTERRUPT_FLAG_BIT,1);
    # Use Pseudo Variable to store PC values to read if interrupt and which interrupt
    PSEUDO_REG.INTC.val=change_bit_val(PSEUDO_REG.INTC.val,0,31,32)

def stm_channel_ccr_statement_1(channel_no):
    set_interrupt(channel_no)

def stm_channel_cif_statement_1(channel_no):
    clear_interrupt(channel_no);

def stm_channel_cmp_statement_1(channel_no):
    set_interrupt(channel_no);


#----------Statements and Constraints------------#

#Enable Debug Mode
def debug_on_statement(data):
    STM_STATE.DEBUG_MODE.val=change_bit_val(STM_STATE.DEBUG_MODE.val, 0x1, 31, 32); 

def debug_on_constraint_1(data):
    #If LSB of data is 1:
    return (data.and_(0x1) == 0x1)


#Disable Debug Mode
def debug_off_statement(data):
    STM_STATE.DEBUG_MODE.val=change_bit_val(STM_STATE.DEBUG_MODE.val, 0x0, 31, 32); 

def debug_off_constraint_1(data):
    #If LSB of data is 0
    return ((data.and_(0x1)) == 0x0)


STATEMENT_LIST=[]
def get_statement_list():
    #Function to share global variable across modules
    global STATEMENT_LIST
    return STATEMENT_LIST

def init_stmt_constraints():
    global STATEMENT_LIST

    debug_on_CONSTRAINT_1= execution_header.CONSTRAINT("DEBUG_ON_1",debug_on_constraint_1,[])
    debug_on_STATEMENT= execution_header.STATEMENT("DEBUG_ON",debug_on_statement,[debug_on_CONSTRAINT_1],[STM_STATE.DEBUG_MODE],PSEUDO_REG.DEBUG)
    STATEMENT_LIST.append(debug_on_STATEMENT)

    debug_off_CONSTRAINT_1= execution_header.CONSTRAINT("DEBUG_OFF_1",debug_off_constraint_1,[])
    debug_off_STATEMENT= execution_header.STATEMENT("DEBUG_OFF",debug_off_statement,[debug_off_CONSTRAINT_1],[STM_STATE.DEBUG_MODE],PSEUDO_REG.DEBUG)
    STATEMENT_LIST.append(debug_off_STATEMENT)

#Testing
if __name__ == "__main__":
    init_reg_por()
    init_stmt_constraints();
