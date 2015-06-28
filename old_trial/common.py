class BIT:
    size=0
    offset=0
    value=0
    size_mask=0
    def __init__(self,size,offset,value):
        self.size=size
        self.offset=31-offset
        self.value=value
        for i in range(0,size):
            size_mask=(size_mask|(1<<i))

    def change_value(self,new_value):
        self.value= (new_value & self.size_mask)

    def get_value(self):
        return (self.value & self.size_mask)
    
    def get_offset_value(self):
        return (self.get_value()<<self.offset)

class REG:
    #Assuming a default size of 32 bits
    elements=[]
    value=0
    size=32
    size_mask=0xFFFFFFFF
    address=None
    def __init__(self,address):
        self.elements=[]
        self.value=0
        self.size=32
        self.size_mask=0xFFFFFFFF
        self.address=address

    def get_value(self):
        for e in elements:
            cur_element=self.elements[e]
            self.value= ((self.value & self.size_mask) | (cur_element.get_offset_value()))

class STM_CHANNEL:
    base_address=None
    cen_bit=None
    ccr_reg=None
    cif_bit=None
    cir_reg=None
    cmp_bit=None
    cmp_reg=None
    def __init__(self,base_address):
        self.base_adress=base_address
        cen_bit=BIT(1,31,0)
        cif_bit=BIT(1,31,0)
        cmp_bit=BIT(32,31,0)
        ccr_reg=REG(base_address+0x0)
        ccr_reg.elements['cen']=cen_bit
        cir_reg=REG(base_address+0x4)
        cir_reg.elements['cif']=cif_bit
        cmp_reg=REG(base_address+0x8)
        cmp_reg.elements['cmp']=cmp_bit
    
class STM:
    base_address=None
    cr_reg=None
    ten_bit=None
    frz_bit=None
    cps_bit=None
    cnt_reg=None
    cnt_bit=None
    channel0=None
    channel1=None
    channel2=None
    channel3=None
    def __init__(self,base_address):
        self.base_adress=base_address
        ten_bit=BIT(1,31,0)
        frz_bit=BIT(1,30,0)
        cps_bit=BIT(8,23,0)
        cr_reg=REG(base_address+0x0)
        cr_reg.elements['ten']=ten_bit
        cr_reg.elements['frz']=frz_bit
        cr_reg.elements['cps']=cps_bit
        cnt_bit=BIT(32,31,0)
        cnt_reg=REG(base_address+0x4)
        cnt_reg.element['cnt']=cnt_bit
        channel0=STM_CHANNEL(base_address+0x10)
        channel1=STM_CHANNEL(base_address+0x20)
        channel2=STM_CHANNEL(base_address+0x30)
        channel3=STM_CHANNEL(base_address+0x40)
        



       
