class CRC():
    def __init__(self,T:list[int],gen:list[int]):
        self.t=T
        self.gen=gen

    def polynomial_division_calc_crc(self):
        #Turn polynomial to generator str to list[int]

        #Get Generator
        g=[0]*(max(self.gen)+1)

        for i in range(len(g)):
            if i in self.gen:
                g[i]=1

        g.reverse()

        remainder=list(self.t)+[0]*max(self.gen)

        #Calculate CRC bits
        for i in range(len(self.t)):
            if remainder[i]==1:
                for j in range(len(g)):
                    remainder[i+j]^=g[j]

        return remainder[-max(self.gen):]

class FrameManager:
    def __init__(self,destin:str,source:str,data:str,crc_gen:list[int]):
        binary_msg=self.convert_msg_bin(data)
        crc=CRC([int(bit)for bit in binary_msg],crc_gen)

        self.frame={
            "Preamble":[10101010]*7,
            "SFD":[10101011],
            "Destination Address":destin,
            "Source Address":source,
            "Length":len(binary_msg),
            "Data":binary_msg,
            "Padding":self.get_padding(binary_msg),
            "Custom CRC":crc.polynomial_division_calc_crc()
        }

    def convert_msg_bin(self,data:str):
        return "".join(format(b,'08b') for b in bytearray(data,'utf-8'))

    def get_padding(self,data:str):
        return "" if len(data)>=46 else "".join([0]*46-len(data))

    def output(self):
        for i in self.frame.keys():
            print("\n"+i+":",self.frame[i])


GoX_str="X12 + X8 + X7 + X5 + X2 + 1"
frame=FrameManager("30-89-4A-4C-91-40","74:d4:dd:58:df:ee","Hello World!",[0,2,5,7,8,12])

frame.output()



