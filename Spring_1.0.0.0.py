from time import time
from fractions import Fraction
import math
import sys

cvf=0
import os
import binascii

Circle_times=0
END_working=0
lenf=0
namea=""
szx=""
wer=""

namez = input("c for compress or e for extract? ")
#@Author Jurijus pacalovas
class compression:
                
    def cryptograpy_compression(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)



                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-4]
                        nac=len(nameas)
                    
                    if i==1:
                       
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    block=1
                    block2=0
                    block3=0
                    Spin=0
                    count=0
                    
                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        END_working=0
                        Circle_times=0
                        Circle_times2=0
                        ii=0
                        
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)

                                if lenf2>30000:
                                    raise SystemExit
                                if lenf2<306:
                                    raise SystemExit
                                
                                
                                    
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:
                                    
                                    lenf5=len(sda2)
                                        
                                    block2=0
                                    ei4=0
                                    ei5=1

                                    Spin=0
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    Spin3=0

                                    Spin2=0
                                    #Extract
                                    
                                    

                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""

                                    sda4=sda3[0:48]#lenf2
                                    sda5=sda3[48:48+30]               #Bytes_row14
                                    sda7=sda3[48+30:]#om
                                    
                                    sda4=str(sda4)
                                    sda5=str(sda5)
                                    sda7=str(sda7)
                                    
                                    lenf2=int(sda4,2)
                                    Bytes_row14=int(sda5,2)
                                    om=int(sda7,2)
                                    
                                    lenf_count_times=lenf2*(2**480)
                                    B2=Bytes_row14*lenf_count_times
                                    B3=B2*B2
                                    m=om-B3
                                    Bytes_row12=m*lenf_count_times
                                    Bytes_row1=Bytes_row14+Bytes_row12
                                    szx=""
                                    
                                    
                                          ##############################################################################################################################################
                                    

                                
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                
                                    
                                   
                                lenf6=len(sda4)
                                lenf8=len(sda2)
                                                            
                                e2=e2+1
                                e3=e3+1

                                e4=""
  
                                if i==1:
                                    Spin=0
                                    sda3=sda2
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    Bytes_row1=int(sda2, 2)

                                    count=0

                                    Bytes_row2=Bytes_row1

                                    lenf_count_times=lenf2
                                    k=Fraction(Bytes_row1, lenf_count_times)  
                                    m=math.floor(k)
                                   
                                    Bytes_row12=m*lenf_count_times
                                    Bytes_row14=Bytes_row1-Bytes_row12
                                    
                                    
                                    lenf_count_times=lenf2*(2**480)
                                                                  
                                    k=Fraction(Bytes_row1, lenf_count_times)  
                                    m=math.floor(k)
                                   
                                    Bytes_row12t=m*lenf_count_times
                                    Bytes_row14t=Bytes_row1-Bytes_row12t
                                    
                                    #print(Bytes_row14)
                                    
                                    #print(Bytes_row14t)
                                    
                                    B2=(Bytes_row14*lenf_count_times)
                                    B3= B2*B2
                                  
                                    om=m-(B3)
                                   
                                 
                                    Spin=1
                                    
                 
                                    
                                    
                                        
                                    #if  -1 count + round add then this to this number
                                    
                                    if Spin==1:
                                         round_bytes2=Bytes_row14#%
                                        
                                         
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.
                                        
                                        
                                         szx=""
                                         BT=32
                                         
  									   
  					
                                         Colaider3=bin(round_bytes2)[2:]
                                         lenf=len(Colaider3)
                                         print(lenf)
                                         if lenf>(32):
                                         	raise SystemExit
                                       
                                         xc=BT-lenf%BT
                                         z=0
                                         if xc!=0:
                                            if xc!=BT:
                                                while z<xc:
                                                    szx="0"+szx
                                                    z=z+1
                                                                                                
                                         Colaider3=szx+Colaider3
                                                                           
                                         sda4=sda4+Colaider3
                                    
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.

                                         szx=""
                                         Colaider3=bin(om)[2:]
                                         lenf=len(Colaider3)
                                         
                                  
                                         xc=lenf-lenf%lenf
                                         z=0
                                         if xc!=0:
                                            if xc!=lenf:
                                                while z<xc:
                                                    szx="0"+szx
                                                    z=z+1
                                                                                                
                                         Colaider3=szx+Colaider3
                                                                           
                                         sda4=sda4+Colaider3


                                         szx=""
                                         #print(round_bytes2)
                                         #print(round_bytes)
                                         #round3=round_bytes2*round_bytes*lenf_count_times
                                         #print(round3)
                                        
                                       
  
                                         
                                         
                                         szx=""
                                         Colaider3=bin(lenf2)[2:]
                                         lenf=len(Colaider3)
                                         xc=48-lenf%48
                                         z=0
                                         if xc!=0:
                                             if xc!=48:
                                                 while z<xc:
                                                     szx="0"+szx
                                                     z=z+1
                                                    
                                         Colaider3=szx+Colaider3
                
                                                                           
                                         sda4=Colaider3+sda4
                                         Colaider3=""

                                         sda6=sda4
                                        
                                         Spin=0
                                         
                                    
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    Spin=1
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    if i==2:
                                        wer=""
                                        szx=""
                                        wer=sda6

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                                                             
                                        n = int(wer, 2)
                                        qqwslenf=len(wer)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        jl=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl)


                                        n = int(sda2, 2)
                                        qqwslenf=len(wer)
                                        qqwslenf=(qqwslenf/8)*2
                                        qqwslenf=str(qqwslenf)
                                        qqwslenf="%0"+qqwslenf+"x"
                                        dj=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl)
                                                    
                                        Circle_times=Circle_times+1
                                        szxzzza=""
                                        szxzs=""
                                        sda2=sda6
                                                    
                                        Circle_times2=Circle_times2+1
                                                    
                                        if Circle_times2==1:
                                            END_working=10 
                                        if END_working==10:        
                                              
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

d=compression()

xw=d.cryptograpy_compression()
