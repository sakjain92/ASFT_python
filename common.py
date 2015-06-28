import stp

solver=stp.Solver()

class reg:
    name=None
    addr=None
    reg_size=None
    default=None
    rmask=None
    wmask=None
    w1c=None
    val=None
    def __init__(self,name,addr,reg_size,default,rmask,wmask,w1c,val):
        self.name=name
        self.addr=addr
        self.reg_size=reg_size
        self.default=default
        self.rmask=rmask
        self.wmask=wmask
        self.w1c=w1c
        self.val=solver.bitvecval(reg_size,val)

def write_reg_with_mask(Register,data):
    write_data = data.and_(Register.wmask)
    Register.val = ( Register.val.and_(~(Register.wmask)) ).or_(write_data)
    w1c_data = data.and_(Register.w1c)
    bits_to_clear = ( Register.val.and_(Register.w1c) ).and_(w1c_data)
    Register.val = Register.val.and_( bits_to_clear.not_() );

def change_bit_val(reg_val,new_val,bit,bit_size):
    #Both reg_val and new_val can be STP variables .
    mask=0x0
    start_bit=(31-bit)
    current_bit=start_bit;

    for i in range(0,bit_size):
        mask=mask|(1<<current_bit)
        current_bit=current_bit+1

    try:
        #Checking that new_val is STP variable
        new_val.name
    except:
        #Its a constant
        return ((reg_val.and_(~mask)).or_(new_val<<start_bit))
    else:
        #Its STP variable 
        return ((reg_val.and_(~mask)).or_(new_val.shl(start_bit)))

def get_bit_val(reg_val,bit,bit_size):
    mask=0x0
    start_bit=(31-bit)
    current_bit=start_bit
    
    for i in range(0,bit_size):
	mask=mask|(1<<current_bit);
        current_bit=current_bit+1

    return ((reg_val.and_(mask)).shr(start_bit))



#Testing
if __name__ == "__main__":

    a=reg("a",0x12345678,32,0xaabb5566,0xffffffff,0xffff0000,0x0000ffff,0xaabb5566)
    print "Step 1: Should be true:",solver.check()
    solver.push();solver.add(a.val==0x0);
    print "Step 2: Should be false:",solver.check();solver.pop()
    solver.push();b=solver.bitvecval(32,0x3210002);write_reg_with_mask(a,b);solver.add(a.val==0x3215564);
    print "Step 3: Should be true:",solver.check();solver.pop()
    solver.push();b=get_bit_val(a.val,30,2);solver.add(b==2);
    print "Step 4: Should be true:",solver.check();solver.pop()
    solver.push();b=solver.bitvecval(32,0x3);a.val=change_bit_val(a.val,b,30,2);solver.add(a.val==0x3215566);
    print "Step 5: Should be true:",solver.check();solver.pop()
    






    

    
