import stm_main  
import copy
from common import *
#from stm_main import *

class STATEMENT:
    name=None
    stmt=None
    executed=None #Attempt to execute
    completed=None # Able to find atleat 1 path to complete
    constraint_list=None
    var_list=[] #Variables effected by statement
    reg=None
    def __init__(self,name,stmt,constraint_list,var_list,reg):
        self.name=name
        self.stmt=stmt
        self.constraint_list=constraint_list
        self.var_list=var_list
        self.reg=reg
        self.executed=0
        self.completed=0
        


class CONSTRAINT:
    name=None
    constraint=None
    var_list=None
    def __init__(self,name,constraint,var_list):
        self.name=name
        self.constraint=constraint
        self.var_list=var_list

class INSTRUCTION:
    reg=None
    data=None
    def __init__(self,reg,data):
        self.reg=reg
        self.data=data

class PATH:
    data_list=None
    data_example=None
    instr_executed=None
    instr_count=None
    flow_list=None
    flow_list_stmt_index=None
    flow_list_contraint_index=None
    flow_list_instr_index=None
    def __init__(self):
        self.data_list=[]
        self.data_example=[]
        self.instr_executed=[]
        self.instr_count=0
        self.flow_list=[]
        self.flow_list_stmt_index=0
        self.flow_list_constraint_index=0
        self.flow_list_instr_index=0
        
    def give_copy(self):
        return copy.deepcopy(self)

class FLOW:
    element=None
    typ=None
    instr=1
    constraint=2
    stmt=3
    new=4
    def __init__(self,element,typ):
        self.element=element
        self.typ=typ
        self.instr=1
        self.constraint=2
        self.stmt=3
        self.new=4

def add_stmt_to_path(path,statement):
    global solver

    statement.executed=1
    # Get data
    data_count=len(path.data_list)
    data_name='data'+str(data_count+1)
    current_data=solver.bitvec(data_name,32)
    path.data_list.insert(0,current_data)

    # Add 'new' in the beginnin - Marks beginning
    flow=FLOW(None,FLOW.new)
    path.flow_list.insert(0,flow)
    
    # Add instruction - Added in the starting always
    instr=INSTRUCTION(statement.reg,current_data)
    path.instr_executed.insert(0,instr)
    path.instr_count=path.instr_count+1
    flow=FLOW(instr,FLOW.instr)
    path.flow_list.insert(1,flow)    
    path.flow_list_stmt_index=2
    path.flow_list_constraint_index=1
    path.flow_list_instr_index=2
    
    # Add statement
    flow=FLOW(statement,FLOW.stmt)
    path.flow_list.insert(path.flow_list_stmt_index,flow)
    path.flow_list_stmt_index=path.flow_list_stmt_index+1
    
    return check_path_possible(path,None)

def add_constraint_to_path(path,constraint):

    # Add instruction - Added in the starting always
    flow=FLOW(constraint,FLOW.constraint)
    path.flow_list.insert(path.flow_list_constraint_index,flow)    
    path.flow_list_constraint_index=path.flow_list_constraint_index+1
    path.flow_list_stmt_index=path.flow_list_stmt_index+1
    path.flow_list_instr_index=path.flow_list_instr_index+1
    
    return check_path_possible(path,None)


def check_path_possible(path,do_model):
    global solver

    solver.push() 
    stm_main.init_reg_por()
    data_index=0
    current_data=None
    for flow in path.flow_list:
        if(flow.typ==FLOW.new):
            if( do_model != None ):
                if( data_index>0 ):
                    path.data_example.insert(data_index-1,solver.model()[current_data.name])
            solver.pop()
            solver.push()
            current_data=path.data_list[data_index]
            data_index=data_index+1
 
        elif(flow.typ==FLOW.instr):
            reg=flow.element.reg
            write_reg_with_mask(reg,current_data)
           
        elif(flow.typ==FLOW.constraint):
            solver.add( (flow.element.constraint)(current_data) )
            if( solver.check() != True ): 
                return False
        elif(flow.typ==FLOW.stmt):
            (flow.element.stmt)(current_data)
   
    if( do_model != None ):
        if( data_index>0 ):
            path.data_example.insert(data_index-1,int(solver.model()[current_data.name])) 
    solver.pop()
    return True

def create_test_txt(path,in_test_path,out_test_path,TESTCOUNT):
    check_path_possible(path,1)
    create_in_test_txt(path,in_test_path,TESTCOUNT)
    create_out_test_txt(path,out_test_path,TESTCOUNT)

def create_in_test_txt(path,in_test_path_dir,TESTCOUNT): 

    in_test_path_comp=in_test_path_dir+str("in_test")+str(TESTCOUNT)+str(".txt")
    in_test_fp= open(in_test_path_comp,'w')

    # Modelling data
    data_index=0
    for instr in path.instr_executed:
        in_string= str(data_index+1) + "  " + str(instr.reg.name) + "  " + str(hex(instr.reg.addr)) + "  " + str(hex(path.data_example[data_index])) +"\n"
        in_test_fp.write(in_string)
        data_index=data_index+1
    
    in_test_fp.close()


def out_all_regs(instr_no,out_test_fp):
    global solver
    # To get global variable from stm_main - Through a function
    local_all_regs=stm_main.get_all_regs()
    
    for reg in  local_all_regs:
        solver.push()
        temp=solver.bitvec("temp",32)
        solver.add(temp==reg.val)
        solver.check()
        reg_val=temp.value        
        solver.pop()
        out_string= str(instr_no) + "  " + str(reg.name) + "  " + str(hex(reg.addr)) + "  " + str(hex(int(reg_val))) +"\n"
        out_test_fp.write(out_string)
    

def create_out_test_txt(path,out_test_path_dir,TESTCOUNT):
    out_test_path_comp=out_test_path_dir+str("out_test")+str(TESTCOUNT)+str(".txt")
    out_test_fp= open(out_test_path_comp,'w')
    
    stm_main.init_reg_por()
    data_index=0
    for flow in path.flow_list:
        if(flow.typ==FLOW.new):
            # Output all Regs info after previous instruction execution complete
            out_all_regs(data_index,out_test_fp)
            current_data=path.data_example[data_index]
            current_data_stp=solver.bitvecval(32,current_data)
            data_index=data_index+1

        elif(flow.typ==FLOW.instr):
            reg=flow.element.reg
            write_reg_with_mask(reg,current_data_stp)

        elif(flow.typ==FLOW.constraint):
            pass
        elif(flow.typ==FLOW.stmt):
            (flow.element.stmt)(current_data)

    out_all_regs(data_index,out_test_fp)

    out_test_fp.close()
    pass
 
