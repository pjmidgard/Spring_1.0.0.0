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

                    d=22315443819177493991761944677104910315673457384239730460440511084212177431168819567825118541310851337465039821906316214198242510540438135727931142433419102243815018338265038023775194772528812787331571939965680311719084717291343233862955894049272678731696268537088340145232562432698790359351107274236956865691467562864254746590400908055997607323768910575586314931842306356893783919785242738568763068302972631443868796167707282236025649464982617196506015634100087670883958869621865690213972010752131134192091613321443847454374260250963778889791101336622602508543957005980765965761923060253502384209749428981857443076646911868604022909621045939492315738139203284607285233872351762944890635358405864516469909279921953352825275864483027964437696272666021595801491322605638432022395761054215557587943430877538797074231689862806502539625142471236905836818336358668327633294190071796104190147968086337913786965044235349060488334163670605976927523937199248843221232798256091178722425394900807432615776128709452190796560835301941995278271390190710390050478754482949862848837331243300539097287648300340325245232309227372126069127679341988505250865304257497679542949191538395545787044123289681360450472439816376506657114276265639645853519664409585329225511350930689939502128247746179203910451636723728150660625977576183529989270929712906459445714381505436965832349654520896614195215124659494306849031280118989569358273687334790516944677259652175024063934613147662944296759847425135082678931445193742901803627924225133455148664479400301157288293657411114861881187726880597947191382601523933463821453869711592650649457847840108040409853620234352280177652826947234245977007135330018643860027280915719051533565241421539610094489025363210675958456660404013216993501395380344402366696132890524781611554637532042479230257644125825992768663335253949112435451239001533052661917391917132935907464510609223351407784171515505406832873016954858343320796395559386259170375584965991528843010160994580866569090261418390126809620745663672469516689205006448266926796457251450848675257300874944603273494307031473387828490861252145972935098519858879848148291213050868702164806256554086197984533851296197533661658917550487938436260803746613211871215681457189615942243142121505143170888944739755052272670776490230136350197576100636437989450423812592121




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
                                #print(lenf2)

                               

                                
                                
                                
                                    
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

                                    sda4=sda3[0:]#lenf2
                                    
                                    sda4=str(sda4)
                                    
                                    om=int(sda4, 2)

                                    Bytes_row2=om-d

                                    szx=""

                                    Colaider3=bin(Bytes_row2)[2:]
                                    lenf=len(Colaider3)
                                    
                               
                                       
                                    xc=lenf-lenf%lenf
                                    z=0
                                    if xc!=0:
                                        if xc!=lenf:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                                                                                
                                    Colaider3=szx+Colaider3
                                                                           
                                    sda6=sda6+Colaider3
                                    sda7=sda6

                                    wer=sda6

                                    n = int(wer, 2)
                                    qqwslenf=len(wer)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)

                                                        
                                    Circle_times=Circle_times+1
                                    szxzzza=""
                                    szxzs=""
                                    sda2=sda6
                                                        
                                    Circle_times2=Circle_times2+1

                                    nameasr="a"+nameas
                                                        
                                    with open(nameasr, "wb") as f3:
                                        f3.write(jl)
                                    x2 = time()
                                    x3=x2-x
                                    return print(x3)
                                    
                                    
                                    
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

                                    Bytes_row3=Bytes_row1-d
                                    #print(Bytes_row3)
                                    
                                        

                                 
                                    Spin=1
                                    
                 
                                    
                                    
                                        
                                    #if  -1 count + round add then this to this number
                                    
                                    if Spin==1:
                                         
                                        
                                         
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.


                                         szx=""
                                         

                                         Colaider3=bin(Bytes_row3)[2:]
                                         lenf=len(Colaider3)
                                         #print(lenf)
                                         
                                       
                                         xc=lenf-lenf%lenf
                                         z=0
                                         if xc!=0:
                                            if xc!=lenf:
                                                while z<xc:
                                                    szx="0"+szx
                                                    z=z+1
                                                                                                
                                         Colaider3=szx+Colaider3
                                                                           
                                         sda4=sda4+Colaider3
                                         sda6=sda4
                                        
                         
                                         
                                         
                                         #szx=""
                                        # BT=493                                         
  									   
  					
                                        # Colaider3=bin(Bytes_row21)[2:]
                                        # lenf=len(Colaider3)
                                         #print(lenf)
                                         #if lenf>(493):
                                         	#raise SystemExit
                                       
                                        # xc=BT-lenf%BT
                                         #z=0
                                         #if xc!=0:
                                           # if xc!=BT:
                                                #while z<xc:
                                                    #szx="0"+szx
                                                    #z=z+1
                                                                                                
                                         #Colaider3=szx+Colaider3
                                                                           
                                        #sda4=sda4+Colaider3
                                        
                                                                                  
                                    
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.

                                         


                                         
                                         #print(round_bytes2)
                                         #print(round_bytes)
                                         #round3=round_bytes2*round_bytes*lenf_count_times
                                         #print(round3)
                                       
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

                                                        
                                        Circle_times=Circle_times+1
                                        szxzzza=""
                                        szxzs=""
                                        sda2=sda6
                                                        
                                        Circle_times2=Circle_times2+1
                                                        
                                        
                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

d=compression()

xw=d.cryptograpy_compression()
