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

namez = input("Please, enter x or y ")
#@Author Jurijus pacalovas
class compression:
                
    def cryptograpy_compression(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="x" or namez=="y":
                    if namez=="x":
                        i=1
                    if namez=="y":
                        i=1
                    
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

                                if lenf2>(2**40)-1:
                                    raise SystemExit
                                if lenf2<135:
                                    raise SystemExit
                                
                                
                                    
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:
                                    
                                    sda2=sda2[1:]
                                    lenf5=len(sda2)
                                   
                                    if sda2[lenf5-8:lenf5]=="10000000":

                                        sda2=sda2[:lenf5-8]

                                    elif sda2[lenf5-7:lenf5]=="1000000":

                                        sda2=sda2[:lenf5-7]

                                    elif sda2[lenf5-6:lenf5]=="100000":

                                        sda2=sda2[:lenf5-6]

                                    elif sda2[lenf5-5:lenf5]=="10000":

                                        sda2=sda2[:lenf5-5]


                                    elif sda2[lenf5-3:lenf5]=="100":

                                        sda2=sda2[:lenf5-3]

                                    elif sda2[lenf5-2:lenf5]=="10":

                                        sda2=sda2[:lenf5-2]

                                    elif sda2[lenf5-1:lenf5]=="1":

                                        sda2=sda2[:lenf5-1]

                                        
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

                                    #Number2=Number1
                                    #5 bytes
                                    
                                    
                                    #n5=0
                                    #while n5<1023:
                                            #Number2=Number2*2
                                            #n5=n5+1

                                    #Number3=Number2

                                    #while Number2==Bytes_row8:
                                        #n4=0
                                        #while n4<lenf_count_times:
                                            #Number3=Number3*2
                                            #n4=n4+1
                                        #Number4=Number3
                                        #n6=0
                                        #while n6<lenf_count_times:
                                            #Number4=Number4//2
                                            #n6=n6+1

                                        #Bytes_row8=Number3-Number4

                                        #Number2=Number2+1
                                        #Number3=Number2
                                    

                                    #Number1

                                    # Bytes_row8 you write this number of size that we got from 5 bytes.

                                    
                                        

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


                                    #Compression

                                    Bytes_row1=int(sda2, 2)

                                    count=0

                                    Bytes_row2=Bytes_row1

                                    lenf_count_times=lenf2*(2**480)

                                    Bytes_row8=Fraction(Bytes_row1, lenf_count_times)
                                    m=math.floor(Bytes_row8)
                                   

                                    Bytes_row12=m*lenf_count_times
                                    Bytes_row14=Bytes_row1-Bytes_row12
                                    Bytes_row16=Bytes_row1//m
                                    Bytes_row17=Bytes_row1-(Bytes_row16*m)

                                    #Bytes_row17, Bytes_row16, Bytes_row14, Bytes_row14


                                    Bytes_row2=(0+Bytes_row14+(m*lenf_count_times)//m*m)

                                    if Bytes_row2!= Bytes_row1:
                                        raise SystemExit
                                    


                                    #print(Bytes_row2)

                                    

                                    
                                  

                                    
                                    

                                    #Bytes_row16*m=Bytes_row1, x m/lenf_count_times  Bytes_row14=Bytes_row1-Bytes_row12
                                    
                                    #print(Bytes_row17)
                                    if Bytes_row14==0:
                                       raise SystemExit
                                    if Bytes_row14!=0:
                                        ii=1
                                        Spin=1
                                    
                 
                                    
                                    
                                        
                                    #if  -1 count + round add then this to this number
                                    
                                    if Spin==1:
                                         round_bytes2=math.floor(Bytes_row14)#%
                                        
                                         Bytes_row19=Bytes_row12+round_bytes2
                                         
                                         
                          
                                         Bytes_row20=Bytes_row1-Bytes_row19
                                         
                                         #print(Bytes_row20)
                                         if Bytes_row20!=0:
                                         	raise SystemExit
                                       
                                         
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.
                                    

                                         szx=""
                                         Colaider3=bin(round_bytes2)[2:]
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
                                         
                                         
                                         round_bytes=math.floor(Bytes_row16)#%
                                        
                                        

                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.



                                         
                                         szx=""
                                         Colaider3=bin(Bytes_row17)[2:]
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
                                        
                                       
                                         Colaider3=bin(Bytes_row17)[2:]
                                         lenf=len(Colaider3)
                                         Colaider3=bin(lenf)[2:]
                                         
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
                                         
                                    

                                         szx=""
                                         Colaider3=bin(round_bytes)[2:]
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
                                        
                                       
                                         Colaider3=bin(round_bytes2)[2:]
                                         lenf=len(Colaider3)
                                         Colaider3=bin(lenf)[2:]
                                         
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
                                        wer=sda4

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                   
                                        wer="1"+wer+"1"
                                        lenf=len(wer)
                                                        
                                        xc=8-lenf%8
                                        z=0
                                        if xc!=0:
                                            if xc!=8:
                                                while z<xc:
                                                    szx="0"+szx
                                                    z=z+1
                                        wer=wer+szx
                                                                                    
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
                                            names2="c"+name
                                            with open(names2, "ab") as f3:
                                                f3.write(dj)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

d=compression()

xw=d.cryptograpy_compression()
print(xw)
