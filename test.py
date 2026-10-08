import random as rn

class problem1:
    def __init__(self,message:str):
        self.message = message
        self.error_pos=0

        print("Problem 1")
        self.error_detection(self.error_injection(self.framing_at_the_sender_side()))

    def framing_at_the_sender_side(self):
        bit_list=[int(bit) for bit in self.message]

        #Adding Blank Parity Bits (0)
        p=0
        parity_vals=[]
        while 2**p<p+len(bit_list)+1:
            bit_list.insert(2**p-1,0)
            parity_vals.append(2**p)
            p+=1

        self.p=p

        #Setting Parity Values
        for i in range(p):
            pos=2**i
            m_sum=0

            for j in range(1,len(bit_list)+1):
                if(j & pos)!=0:
                    m_sum+=bit_list[j-1]

            if m_sum%2==0:
                bit_list[pos-1]=1 
            else:
                bit_list[pos-1]=0

        return "".join(str(bit) for bit in bit_list)

    def error_injection(self,recieved_message:str):
        #Inject Error
        print('Before Error:',recieved_message)
        error_pos=rn.randint(0,len(recieved_message)-1)
        self.error_pos=error_pos+1
        bit_list=[int(bit) for bit in recieved_message]
        bit_list[error_pos]^=1

        print("After Error:", "".join(str(bit) for bit in bit_list))
        return "".join(str(bit) for bit in bit_list)

    def error_detection(self,message_error:str):
        bit_list=[int(bit) for bit in message_error]

        groupings=[]

        #Decoding
        for i in range(self.p):
            pos=2**i
            m_sum=0

            for j in range(1,len(bit_list)+1):
                if(j & pos)!=0:
                    m_sum+=bit_list[j-1]

            if m_sum%2==0:
                groupings.append(1) 
            else:
                groupings.append(0)

        #Reverse and find syndrome        
        groupings.reverse()
        syndrome="".join(str(bit) for bit in groupings)   

        print("Outputted:",syndrome)
        print("Detected Error Pos:",int(str(syndrome),2))
        print("Actual Error Pos:",self.error_pos)


class problem2():
    def __init__(self,T:list[int],GoX_str:str):
        self.t=T
        self.GoX_str=GoX_str

        print("Problem 2")
        sent_rx,generator=self.polynomial_division_calc_crc()
        sent_rx_error=self.error_injection(sent_rx)
        self.decode(sent_rx_error,generator)

    def polynomial_division_calc_crc(self):
        #Turn polynomial to generator str to list[int]
        self.GoX_str=self.GoX_str.replace("X","")
        self.GoX_str=self.GoX_str.replace("+","")
        self.GoX_str=self.GoX_str.replace(" ","")
        GoX_coeff=[int(val)-1 if int(val) == 1 else int(val) for val in self.GoX_str]
        self.generator_coeff=GoX_coeff

        #Get Generator
        g=[0]*(max(GoX_coeff)+1)

        for i in range(len(g)):
            if i in GoX_coeff:
                g[i]=1

        g.reverse()

        remainder=list(self.t)+[0]*max(GoX_coeff)

        #Calculate CRC bits
        for i in range(len(self.t)):
            if remainder[i]==1:
                for j in range(len(g)):
                    remainder[i+j]^=g[j]

        return list(self.t)+[remain_bit for remain_bit in remainder[-max(GoX_coeff):]],g

    def error_injection(self,recieved_message:list[int]):
            #Inject Error
            print("Before Error:",recieved_message)
            error_pos=rn.randint(0,len(recieved_message)-1)
            self.error_pos=error_pos+1
            bit_list=[int(bit) for bit in recieved_message]
            bit_list[error_pos]^=1

            print("After Error:",bit_list)
    
            return bit_list

    def decode(self,sent_rx:list[int],generator:list[int]):
        crc_bits=list(sent_rx)

        #Decode using R(x)/G(x)
        for i in range(len(self.t)):
            if crc_bits[i]==1:
                for j in range(len(generator)):
                    crc_bits[i+j]^=generator[j]

        crc_bits_remainder=crc_bits[-max(self.generator_coeff):]
        print("Decoded Remainder:",crc_bits_remainder)
        print("Detected Error:",(True if crc_bits_remainder.count(1)>=1 else False))

problem1("0100101")
problem2([0,0,1,1,0,1,0,0,1,1],"X5 + X3 + X2 + 1")





