from time import time
cvf=0
Portal=2
import os
import binascii
import math

zzaax=""
szxzzzas=""
asaaq=""
assa=0
adwll1=0
ddf=0
cvz31=0
rw=0
qqw1q=""
lenfzzz=0
fffgjv=""
fffgjv1=""
zzaax1=""
qqqs=0
a=0
blockw=5
blockw1=4
cvb=0
aqw1=0
zsaqq=""
qqqwz=0
assx=0
ass=0
asss=0
b=0
aaqw=""
aaqws=""
l=""
j=0
b=0
aq=0
qfl=0
t=0
h=0
byteb=""
notexist=""
lenf=0
numberschangenotexistq = []
numberschangenotexistqz = []
qwa=0
add=0
m = []
p=0
namea=""
d=1
a=0
asd=""
b=0
szx=""
asf2="0b"
while b<1790:
    m+=[-1]
    b=b+1
k = []
wer=""
qtqweqw=""
numberschangenotexist = []
numbers = []
namez = input("c,c3 c2  ul2 or for compress cl for extract for e, e3 cl2, u2? ")

#@Author Jurijus pacalovas
class compression:


    def Areacu2(self):
                    if namez=="u2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        namea="file.W"
                        namem=""
                        namema="?"
                       
                        blockw=5
                        blockw1=4
                        nameas=name
                        nac=len(nameas)
                        if nameas[nac-8:nac]==".bin.bin":
                            nameas=nameas[0:nac-8]
                        countraz=0
                        C=0
                        s=""
                        assx=0
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                       
            
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        with open(nameas, "a") as f3:
                                f3.write(s)
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            data = binary_file.read()
                            s=str(data)
                            lenf2=len(data)
                            lenf1=len(data)
                            if lenf1<6:
                                ##print("This file is too small");
                                raise SystemExit
                            if lenf1>(2**32)-1:
                                ##print("This file is too big");
                                raise SystemExit
            
                            while assx<10:
                                qqqwz=0
                                
                                a=0
                                ass=0
                                asss=0
                                b=0
                                aaqw=""
                                aaqws=""
                                l=""
                                j=0
                                b=0
                                aq=0
                                qfl=0
                                t=0
                                h=0
                                byteb=""
                                notexist=""
                                lenf=0
                                numberschangenotexistq = []
                                numberschangenotexistqz = []
                                qwa=0
                                m = []
                                p=0
                                
                                d=1
                                a=0
                                asd=""
                                b=0
                                szx=""
                                asf2="0b"
                                while b<1790:
                                    m+=[-1]
                                    b=b+1
                                k = []
                                wer=""
                                numberschangenotexist = []
                                numbers = []
                                assa=0
                                asaaq=""
                                szxzzzas=""
                                s=""
                                blockw=4
                                blockw1=3
                                sdaa=""
                                aas=0
                                asaaq=""
                                asaaqq=""
                                asaaql=""
                                asaaqll=""
                                en=0
                                assa=0
                                assas=0
                                wer=""
                                asaaqt=""
                                countraz=countraz+1
                                ddm=0
                                wers=""
                                asaaqllw=""
                                asaaqll=""
                                qqqslls=""
                                qqqslls=""
                                asaaqlls=""
                                asaaqllsq=""
                                ww=10
                                rr1=0
                                rr12=0
                                wers=""
                                countraz=0
            
            
                                
                               
            
                               
                                with open(nameas, "ab") as f2:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    
                                    lenf1=len(data) 
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                          
                                    for byte in sda:
                                        if sda[0:1]=="1":
                                            sda=sda[1:]
                                        elif sda[0:2]=="01":
                                            sda=sda[2:]
                                        elif sda[0:3]=="001":
                                            sda=sda[3:]
                                        elif sda[0:4]=="0001":
                                            sda=sda[4:]
                                        elif sda[0:5]=="00001":
                                            sda=sda[5:]
            
                                        elif sda[0:6]=="000001":
                                            sda=sda[6:]
                                        elif sda[0:7]=="0000001":
                                            sda=sda[7:]
            
                                        elif sda[0:8]=="00000001":
                                            sda=sda[8:]
            
                                            
                                        sdalong=len(sda)
            
                                        
                                        if sda[sdalong-1:sdalong]=="1":
                                            sda=sda[:sdalong-1]
                                        elif sda[sdalong-2:sdalong]=="10":
                                            sda=sda[:sdalong-2]
                                        elif sda[sdalong-3:sdalong]=="100":
                                            sda=sda[:sdalong-3]
                                        elif sda[sdalong-4:sdalong]=="1000":
                                            sda=sda[:sdalong-4]
                                        elif sda[sdalong-5:sdalong]=="10000":
                                            sda=sda[:sdalong-5]
                                        elif sda[sdalong-6:sdalong]=="100000":
                                            sda=sda[:sdalong-6]
            
                                        elif sda[sdalong-7:sdalong]=="1000000":
                                            sda=sda[:sdalong-7]
            
                                        elif sda[sdalong-8:sdalong]=="10000000":
                                            sda=sda[:sdalong-8]
            
                                            
                                        sdad=len(sda)
                                        
                                        eo=0
                                        el=0
                                        
                                        while eo<sdad:
                                            wers=""
                                            
                                            
                                            el=eo
                                            eo=eo+2523109
                                            takebitsize=sda[el:eo]
                                            xssd=len(takebitsize)
                                            el=eo-2523109
                                            eo=eo-2523109

                                            
                                            if xssd<=2523108:
                                                wer=wer+takebitsize
                                                C=C+2523108
                                                   
                                                n = int(wer, 2)
                                        
                                                qqwslenf=len(wer)
                                                qqwslenf=(qqwslenf/8)*2
                                                qqwslenf=str(qqwslenf)
                                                qqwslenf="%0"+qqwslenf+"x"
                                             
                                                jl=binascii.unhexlify(qqwslenf % n)
                                                sssssw=len(jl)
                                                data=jl
                                                qqqwz=qqqwz+1
                                                szxzzza=""
                                                szxzs=""
                                        
                                                blockw=4
                                                blockw1=3
                                    
                                                    #print(sssssw)
                                            
                                                wer=""
                                       
                                                assx=10
                                        
                                                f2.write(jl)
                                                raise SystemExit
                                                  
                                            el=eo
                                            eo=eo+14
                                            takebit2=sda[el:eo]
                                            takebitdw2=int(takebit2, 2)
                                            
                                            el=eo
                                            eo=eo+2523092
                                            takebit=sda[el:eo]
             
                                            takebitdw=int(takebit, 2)
                                            sw=0
                                            numbertc=takebitdw
                                            
                                               
                                            while sw<180222:
                                                    
                                                numbertc3=numbertc%16383
                                                numbertc1=numbertc//16383
                                                numbertc2=int(numbertc1)
                                                    
                                                    
                                                if takebitdw2==numbertc3:
                                                    numbertc3=16383
                                                        #print(takebitdw2)
                                                       # print(numbertc3)
                                                        
                                                    
                                                szxzzz=""
                                                szxzzz=bin(numbertc3)[2:]
                                                dd=len(szxzzz)
                                                xc=14-dd%14
                                                z=0
                                                if xc!=0 and dd!=14:
                                                    while z<xc:
                                                        szxzzz="0"+szxzzz
                                                        z=z+1
                                                wers=wers+szxzzz
                                                    
                                                numbertc=numbertc2
                                                sw=sw+1
                                                    #print(sw)
                                                
                                            ddr=len(wers)
                                            
                                            sw=0
                                            el1=2523108
                                            eo1=2523108
                                           
                                            while sw<180222:
                                                    
                                                el1=eo1
                                                eo1=eo1-14
                                                takebit=wers[eo1:el1]
                                                C=el1
                                                    
                                                wer=wer+takebit
                                                sw=sw+1
                                                   
                                            wers=""
                                        


                                    wer=wer+sda[C:]
                                   
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
                                    data=jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                   
                                    
                                    blockw=4
                                    blockw1=3
                                
                                    #print(sssssw)
                                        
                                    wer=""
                                    
                      
                                    assx=10
                                    
                                    f2.write(jl)
                                    x2 = time()
                                    x3 = x2-x
                                    return print(x3) 

    
    def Areac2(self):
                    if namez=="c2":
                        x=0
                        x1=0
                        x2=0
                        x = time()
                        name = input("What is name of file? ")
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                        
                        block=180222
                        blockw=180221
                        blockw1=16384
                        virationc=16383
                        bitc=14
                        a=0
                        qfl=0
                        h=0
                        lenf1=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        qwa=0
                        z=0
                        m = []
                        p=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<blockw1:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        numberschangenotexist = []
                        numbers = []
                            
                        
                        namea=name+".bin.bin"
                        namem=name+"/"
            
                        nameas=name
                        nac=len(nameas)
            
                        s=""
                        qwt=""
                        sda=""
                        ert=0
                        aqwer=0
                        aqwq=0
                        aqwers=0
                        qwaw=""
                        qwaw1=""
                        xx=0
                        xx3=0
                        with open(namea, "w") as f4:
                            f4.write(s)
                        with open(namea, "a") as f3:
                            f3.write(s)
                        with open(name, "rb") as binary_file:
                            data = binary_file.read()
                            lenf1=len(data)
                            #if lenf1<400000:
                                #print("This file is too small");
                                #raise SystemExit
                            s=str(data)
                            lenf=len(data)
                        sda=bin(int(binascii.hexlify(data),16))[2:]
                        szx=""
                        lenf=len(sda)
                        xc=8-lenf%8
                        z=0
                        if xc!=0:
                            if xc!=8:
                                while z<xc:
                                    szx="0"+szx
                                    z=z+1
                        sda=szx+sda     
                        lenf=len(sda)
                        szx=""
            
                        for byte in sda:
                            aqwer=aqwer+1
                            aqwers=aqwers+1
                            qwaw=qwaw+byte
                            qwaw1=qwaw1+byte
                            
                                    
                            if aqwer<=bitc:
                                qwt=qwt+byte
                            if aqwer==bitc:
                                qwaw1=""
                                xx3=xx3+1
                                aqwq=int(qwt,2)
                                qwt=""
                                a=a+1
                                h=h+1  
                            av=bin(aqwq)
                            if a<=block and aqwer==bitc:
                                aqwer=0
                                m[aqwq] = aqwq
                                numbers.append(aqwq)  
                            if a == block:
                                
                                p=0
                                while p<blockw1:
                                    if p!=m[p]:
                                        k.append(p)     
                                    p=p+1
                                lenfg=len(k)
                                
                                if lenfg==0:
                                    xx=0
                                    raise SystemExit
                                if lenfg>0:
                                    acvb=lenfg-1
                                    ss=0
                                    ww=0
                                   
                                    acvb=lenfg-1
                                    notexist=k[0]
                                    
                                   
                                    
                                    if notexist>16383 or notexist<0:
                                        raise SystemExit
                                        
                                        
                                        xx=0
                                       
                                    else:
                                        xx=1
                                        szx=bin(notexist)[2:]
                                        lenf=len(szx)
                                        
                                        xc=14-lenf
                                            
                                        z=0
                                        if xc!=0 and lenf!=14:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        takebitdw2=int(szx, 2)
                                        
                                        szxw1=""
                                        szxw1=szx
                                        
                                        lenf=len(szx)
                                       
                                        szx=""  
                                        if lenfg==0:
                                            raise SystemExit
                                b=-1
                                kl=blockw+1
                                bnkw=16383**(kl)
                                
                                
                                
                                cb=0        
                                er=-1
                                ghj=0
                                ghjd=1
                                bnk=1
                                p=0
                                cvz=0
                                if xx==1:
                                    
                                    for p in range(blockw+1):
                                        if lenfg>0:
                                            if 16383!=byteb:
                                                byteb=numbers[p]
                                                
                                                ghj=byteb
                                            if 16383==byteb:
                                                byteb=notexist
                                                
                                                ghj=byteb
                                                #print(ghj)
                                                #os.system("pause")
                                        qfl=qfl+1
                                        ghjd=ghj
                                        bnk=1
                                        
                                        bnkd=1        
                                        kl=kl-1
                                                
                                                
                                                
                                                  
                                        if lenfg>0:
                                                    
                                            bnkw=bnkw//16383
                                            #print(bnkw)
                                            #os.system("pause")
                                           
                                            
                                        
                                                        
                                                
            
                                            ghjd=0
                                            ghjd=ghj*bnkw
                                            #print(ghj)
                                                    
                                        cvz=cvz+ghjd
                                                
                                    
                                    bnkw=1023**(kl)
                                    
                                    szx=bin(cvz)[2:]
                                    cvz=0
                                    lenf=len(szx)
                                    
                                    if lenfg>0:
                                        xc=2523092-lenf
                                        z=0
                                        if xc!=0 and lenf!=2523092:
                                            while z<xc:
                                                szx="0"+szx
                                                z=z+1
                                        
                                        if xx==1:  
                                            wer=wer+szxw1+szx
                                            szxw1=""
                                       
                                            
                                        
            
                                    
                                        lenf=len(szx)
                                        
                                        szx=""
                                
                                
                                        
                                qwaw=""
                                
                                a=0
                                numberschangenotexist = []    
                                del k[:]     
                                del numbers[:]
                                m = []
                                b=0
                                while b<blockw1:
                                    m+=[-1]
                                    b=b+1
                                b=0
                                        
                        a=0
            
                        wer=wer+qwaw
                        qwaw=""
            
            
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
                        lenf=len(szx)                      
                        szx=""        
                        wer="0b"+wer
                        n = int(wer, 2)
                        qqwslenf=len(wer)
                        qqwslenf=(qqwslenf/8)*2
                        qqwslenf=str(qqwslenf)
                        qqwslenf="%0"+qqwslenf+"x"
                        jl=binascii.unhexlify(qqwslenf % n)
                        sssssw=len(jl)
                        with open(namea, "ab") as f2ww:             
                            f2ww.write(jl)
                            jls=jl
                            x2 = time()
                            x3 = x2-x


                            
                        name = namea
                        namea="file.W"
                        namem=""
                        namema="?"
                       
                        blockw=5
                        blockw1=4
                        nameas=name
                        nac=len(nameas)
                        if nameas[nac-8:nac]==".bin.bin":
                            nameas=nameas[0:nac-8]
                        countraz=0
                        C=0
                        s=""
                        assx=0
                        zzaax=""
                        szxzzzas=""
                        asaaq=""
                        assa=0
                        adwll1=0
                        ddf=0
                        cvz31=0
                        rw=0
                        qqw1q=""
                        lenfzzz=0
                        fffgjv=""
                        fffgjv1=""
                        zzaax1=""
                        qqqs=0
                        a=0
                        blockw=5
                        blockw1=4
                        cvb=0
                        aqw1=0
                        zsaqq=""
                        qqqwz=0
                        assx=0
                        ass=0
                        asss=0
                        b=0
                        aaqw=""
                        aaqws=""
                        l=""
                        j=0
                        b=0
                        aq=0
                        qfl=0
                        t=0
                        h=0
                        byteb=""
                        notexist=""
                        lenf=0
                        numberschangenotexistq = []
                        numberschangenotexistqz = []
                        qwa=0
                        add=0
                        m = []
                        p=0
                        namea=""
                        d=1
                        a=0
                        asd=""
                        b=0
                        szx=""
                        asf2="0b"
                        while b<1790:
                            m+=[-1]
                            b=b+1
                        k = []
                        wer=""
                        qtqweqw=""
                        numberschangenotexist = []
                        numbers = []
                       
            
                        with open(nameas, "w") as f4:
                                f4.write(s)
                        with open(nameas, "a") as f3:
                                f3.write(s)
                        with open(name, "rb") as binary_file:
                            # Read the whole file at once
                            data = binary_file.read()
                            s=str(data)
                            lenf2=len(data)
                            lenf1=len(data)
                            if lenf1<6:
                                ##print("This file is too small");
                                raise SystemExit
                            if lenf1>(2**32)-1:
                                ##print("This file is too big");
                                raise SystemExit
            
                            while assx<10:
                                qqqwz=0
                                
                                a=0
                                ass=0
                                asss=0
                                b=0
                                aaqw=""
                                aaqws=""
                                l=""
                                j=0
                                b=0
                                aq=0
                                qfl=0
                                t=0
                                h=0
                                byteb=""
                                notexist=""
                                lenf=0
                                numberschangenotexistq = []
                                numberschangenotexistqz = []
                                qwa=0
                                m = []
                                p=0
                                
                                d=1
                                a=0
                                asd=""
                                b=0
                                szx=""
                                asf2="0b"
                                while b<1790:
                                    m+=[-1]
                                    b=b+1
                                k = []
                                wer=""
                                numberschangenotexist = []
                                numbers = []
                                assa=0
                                asaaq=""
                                szxzzzas=""
                                s=""
                                blockw=4
                                blockw1=3
                                sdaa=""
                                aas=0
                                asaaq=""
                                asaaqq=""
                                asaaql=""
                                asaaqll=""
                                en=0
                                assa=0
                                assas=0
                                wer=""
                                asaaqt=""
                                countraz=countraz+1
                                ddm=0
                                wers=""
                                asaaqllw=""
                                asaaqll=""
                                qqqslls=""
                                qqqslls=""
                                asaaqlls=""
                                asaaqllsq=""
                                ww=10
                                rr1=0
                                rr12=0
                                wers=""
                                countraz=0
            
            
                                
                               
            
                               
                                with open(nameas, "ab") as f2:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    
                                    lenf1=len(data) 
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                          
                                    for byte in sda:
                                        if sda[0:1]=="1":
                                            sda=sda[1:]
                                        elif sda[0:2]=="01":
                                            sda=sda[2:]
                                        elif sda[0:3]=="001":
                                            sda=sda[3:]
                                        elif sda[0:4]=="0001":
                                            sda=sda[4:]
                                        elif sda[0:5]=="00001":
                                            sda=sda[5:]
            
                                        elif sda[0:6]=="000001":
                                            sda=sda[6:]
                                        elif sda[0:7]=="0000001":
                                            sda=sda[7:]
            
                                        elif sda[0:8]=="00000001":
                                            sda=sda[8:]
            
                                            
                                        sdalong=len(sda)
            
                                        
                                        if sda[sdalong-1:sdalong]=="1":
                                            sda=sda[:sdalong-1]
                                        elif sda[sdalong-2:sdalong]=="10":
                                            sda=sda[:sdalong-2]
                                        elif sda[sdalong-3:sdalong]=="100":
                                            sda=sda[:sdalong-3]
                                        elif sda[sdalong-4:sdalong]=="1000":
                                            sda=sda[:sdalong-4]
                                        elif sda[sdalong-5:sdalong]=="10000":
                                            sda=sda[:sdalong-5]
                                        elif sda[sdalong-6:sdalong]=="100000":
                                            sda=sda[:sdalong-6]
            
                                        elif sda[sdalong-7:sdalong]=="1000000":
                                            sda=sda[:sdalong-7]
            
                                        elif sda[sdalong-8:sdalong]=="10000000":
                                            sda=sda[:sdalong-8]
            
                                            
                                        sdad=len(sda)
                                        
                                        eo=0
                                        el=0
                                        
                                        while eo<sdad:
                                            wers=""
                                            
                                            
                                            el=eo
                                            eo=eo+2523109
                                            takebitsize=sda[el:eo]
                                            xssd=len(takebitsize)
                                            el=eo-2523109
                                            eo=eo-2523109

                                            
                                            if xssd<=2523108:
                                                wer=wer+takebitsize
                                                C=C+2523108
                                                   
                                                n = int(wer, 2)
                                        
                                                qqwslenf=len(wer)
                                                qqwslenf=(qqwslenf/8)*2
                                                qqwslenf=str(qqwslenf)
                                                qqwslenf="%0"+qqwslenf+"x"
                                             
                                                jl=binascii.unhexlify(qqwslenf % n)
                                                sssssw=len(jl)
                                                data=jl
                                                qqqwz=qqqwz+1
                                                szxzzza=""
                                                szxzs=""
                                        
                                                blockw=4
                                                blockw1=3
                                    
                                                    #print(sssssw)
                                            
                                                wer=""
                                       
                                                assx=10
                                        
                                                f2.write(jl)
                                                raise SystemExit
                                                  
                                            el=eo
                                            eo=eo+14
                                            takebit2=sda[el:eo]
                                            takebitdw2=int(takebit2, 2)
                                            
                                            el=eo
                                            eo=eo+2523092
                                            takebit=sda[el:eo]
             
                                            takebitdw=int(takebit, 2)
                                            sw=0
                                            numbertc=takebitdw
                                            
                                               
                                            while sw<180222:
                                                    
                                                numbertc3=numbertc%16383
                                                numbertc1=numbertc//16383
                                                numbertc2=int(numbertc1)
                                                    
                                                    
                                                if takebitdw2==numbertc3:
                                                    numbertc3=16383
                                                        #print(takebitdw2)
                                                       # print(numbertc3)
                                                        
                                                    
                                                szxzzz=""
                                                szxzzz=bin(numbertc3)[2:]
                                                dd=len(szxzzz)
                                                xc=14-dd%14
                                                z=0
                                                if xc!=0 and dd!=14:
                                                    while z<xc:
                                                        szxzzz="0"+szxzzz
                                                        z=z+1
                                                wers=wers+szxzzz
                                                    
                                                numbertc=numbertc2
                                                sw=sw+1
                                                    #print(sw)
                                                
                                            ddr=len(wers)
                                            
                                            sw=0
                                            el1=2523108
                                            eo1=2523108
                                           
                                            while sw<180222:
                                                    
                                                el1=eo1
                                                eo1=eo1-14
                                                takebit=wers[eo1:el1]
                                                C=el1
                                                    
                                                wer=wer+takebit
                                                sw=sw+1
                                                   
                                            wers=""
                                        


                                    wer=wer+sda[C:]
                                   
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
                                    data=jl
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                                   
                                    
                                    blockw=4
                                    blockw1=3
                                
                                    #print(sssssw)
                                        
                                    wer=""
                                    
                      
                                    assx=10
                                    
                                    f2.write(jls)
                                    x2 = time()
                                    x3 = x2-x
                                    return print(x3) 


                            
                            

                        

    def cryptograpy_compression3(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c3" or namez=="e3":
                    if namez=="c3":
                        i=1
                    if namez=="e3":
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

                                    
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    Spin3=0

                                    Spin2=0
                                    #Extract
                                    g=1
                                    
                                    if g==1:

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

                                    
                                    
                                    sda3=sda2
                                    lenf6=len(sda3)
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    Bytes_row4=""
                                    ei=0

                                    while ei<lenf6:

                                        sda7=sda3[ei:ei+1]

                                        

                                        if sda7=="0":
                                            ei=ei+1

                                            sda9=sda3[ei:ei+4]
                                        
                                            sda4=sda4+sda9
                                            ei=ei+4

                                        if sda7=="1":
                                    
                                            sda8=sda3[ei:ei+1]
                                            ei=ei+1

                                            if sda8=="1":
                                                sda5=sda3[ei:ei+2]
                                                ei=ei+2

                                                
                                                Bytes_row4=int(sda5, 2)
                                                #print(Bytes_row4)

                                                count=0

                                                u=0
                                                code=256



                                                szx=""
                                                szx1=""
                                              
                                                szx1=bin(Bytes_row4)[2:]
                                                lenf=len(szx1)
                                                #print(lenf)
                                                
                                                #print(lenf)
                                                xc=4-lenf%4
                                                z=0
                                                if xc!=0:
                                                     if xc!=4:
                                                           while z<xc:
                                                                szx="0"+szx
                                                                z=z+1
                                        
                                                sda4=sda4+szx+szx1




                                    #print(ei)
                                    sda6=sda4
                                        
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

                                    if Circle_times2==1:                   
                                            
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)
                                        
                                
  
                                if i==1:
                                    
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

                                    sda9=""

                                    sda9=""

                                    ei=0
                                    
                                    

                                    while ei<lenf6:

                                        sda9=sda2[ei:ei+4]

                                        ei=ei+4

                                        Bytes_row1=int(sda9, 2)

                                        count=0

                                   

          


                                        szx=""
                                             

                                        Colaider3=bin(Bytes_row1)[2:]
                                        lenf=len(Colaider3)
                                        #print(lenf)
                                        

                                       

                                        if lenf<=2:
                                                sda7=""
                                                szx=""
                                                lenf=len(Colaider3)
                                                xc=2-lenf
                                                z=0
                                                if xc!=0:
                                                    if xc!=2:
                                                            while z<xc:
                                                                szx="0"+szx
                                                                z=z+1                                         	     														

                                             
                                             
                                        if lenf<=2:   
                                        
                                            sda4=sda4+"1"+szx+Colaider3
                                                                        
                                        else:

                                            sda4=sda4+"0"+sda9



                                        
                                    #print(ei)
                                    sda6=sda4
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    
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
                                        
                                        wer=wer+"1"
                                        lenf=len(wer)
                                        #print(lenf)
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


                                                        
                                        Circle_times=Circle_times+1
                                        szxzzza=""
                                        szxzs=""
                                        sda2=sda6
                                                        
                                        Circle_times2=Circle_times2+1
                                       


                                    
                                        if Circle_times2==1:                   
                                            
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)






    def cryptograpy_compression(self):
              
                
                if namez=="ul2" or namez=="cl2":
                    if namez=="ul2":
                        i=1
                    if namez=="cl2":
                        i=2
                        
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-12:nac]!=".bin.bin.bin":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                        
                        nameas=name[:nac-12]
                        nac=len(nameas)
                    
                    
                    if nameas[nac-5:nac]==".docx":
                        Portal=1
                    if nameas[nac-4:nac]==".pdf":
                        Portal=3
                    if nameas[nac-4:nac]==".doc":
                        Portal=1
                    if nameas[nac-4:nac]==".png":
                        Portal=7
                    if nameas[nac-4:nac]==".jpg":
                        Portal=9
                    if nameas[nac-4:nac]==".mp4":
                        Portal=8
                      
                    if i==1:
                       
                        nameas=name+".bin.bin.bin"
                    
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=1
                    e4=""
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()

                      
                        if i==1:
                            if Portal==9 and data[0:3]!=b'\xff\xd8\xff':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==9 and data[0:3]==b'\xff\xd8\xff': 
                                    data=data[3:]
                            if Portal==7 and data[0:4]!=b'\x89\x50\x4e\x47' :
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==7 and data[0:4]==b'\x89\x50\x4e\x47' :             
                                    data=data[4:]
                            if Portal==8 and data[0:11]!=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':
                                    print("Program close because this is file incorrect")
                                    raise SystemExit
                            if Portal==8 and data[0:11]==b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34':             
                                    data=data[11:]
      
                        s=str(data)
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:

                                 
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

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

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
                                                
                                e4=sda2[e2:e3]
                                
                                block=block+1

                                if assxw>=e3%8:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""

                                

                                if assxw<=e3%8:
                                                
                                            if e4=="0":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""
                                                 
                                  

                                if assxw>=e3%4:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""

                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""    
                                


                                if assxw>=e3%4:
                                                
                                            if e4=="0":
                                                sda3=sda3+"1"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""    
                                
                                if assxw>=e3%2:
                                                
                                            if e4=="1":
                                                sda3=sda3+"0"
                                                e4="0"
                                                e4=""
                                                 
                                if e4=="1":
                                	sda3=sda3+"1"
                                	e4="1"
                                	e4=""
                                    
                                if e4=="0":
                                    sda3=sda3+"1"
                                    e4="0"
                                    e4=""     
                               
                                e2=e2+1
                                e3=e3+1

                                e4=""
                          
                                if e3==cvf:
                                    e2=0
                                    e3=1
                                    
                                    cvf=cvf+1

                                    cvf=sw
                                    sw=sw+1
                             
                                if cvf==lenf5*8+4:
                                    sw=sw+2
                                    cvf=c
                                    cvf1=cvf1+1
                                     
                                    c=c+2

                                if cvf1==1:
                                   
                                    n = int(sda3, 2)
                                
                                    qqwslenf=len(sda3)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    data=jl
                                    
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==200:
                                        assx=10
                                        if assx==10:
                                            
                                                if i==2:
                                                    if Portal==7:
                                                        jl= b'\x89\x50\x4e\x47'+jl
                                                    if Portal==8:
                                                        jl=b'\x00\x00\x00\x18\x66\x74\x79\x70\x6d\x70\x34'+jl
                                                    if Portal==9:
                                    	                jl=b'\xff\xd8\xff'+jl
                                    	                
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)




    def cryptograpy_compression2(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)

                  
                    c=0
                    A=0
                    Spin=0
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
                        lenf7=len(data)
                        
                        END_working=0
                        Circle_times2=0
                        ii=0
                        sda20=""
                        
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
                                if i==1:
                                    if lenf7>=(2**32)-1:
                                        raise SystemExit
                                        
                                    if lenf7==0:
                                        raise SystemExit 
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:

                                    
                                    
                                    lenf5=len(sda2)

                                    
                                    
                                        
                                    block2=0
                                    ei4=0
                                    ei5=1

                                    
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    Spin3=0

                                    Spin2=0
                                    #Extract
                                    g=1
                                    
                                    s

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    Bytes_row4=""
                                    ei=0

                                    

                                    if Circle_times2==0:
                                        lenf8a=sda3[0:48]
                                        lenf8b=sda3[48:96]
 
                                        Count1=int(lenf8a, 2)

                                        lenf8=int(lenf8b, 2)
                                        
                                        ei=0
                                        while ei<lenf8:
                                            sda5=sda5+"1"

                                            ei=ei+1

                                        sda3=sda5
                                        
                                    
                                    ei=0
                                    

                                    count_times4=0

                                    if Circle_times2%3:
                                        c=1
                                    if Circle_times2%4:
                                        c=5
                                    if Circle_times2%5:
                                        c=7
                                    if Circle_times2%6:
                                        c=8

                                    if Circle_times2%7:
                                        c=3

                                    if Circle_times2%8:
                                        c=4

                                    if Circle_times2%9:
                                        c=6
                                        
                                    
                                    if Circle_times2%10:
                                        c=9
                                        
                                    if Circle_times2%11:
                                        c=2
                                    if Circle_times2%12:
                                        c=11
                                    if Circle_times2%13:
                                        c=10
                                    
                                    

                                    while ei<lenf8:
                                        
                                        sda10=sda3[ei:ei+1]
 
                                        ei=ei+1

                                        if Circle_times2==Circle_times2%3:

                                        
                                            if sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei<=Circle_times2:
                                                sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei<=Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                            
                                            
                                        elif Circle_times2==Circle_times2%1*(lenf8):

                                            if sda10=="1" and ei==Circle_times2%c:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei==Circle_times2%c: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei!=Circle_times2%c:
                                                    sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei!=Circle_times2%c: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                
                                        elif Circle_times2==Circle_times2%2*(lenf8):
                                            
                                            if sda10=="1" and ei==Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei==Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1

                                        else:

                                            if sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei==Circle_times2:
                                                sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei==Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                            
                                            



                                    

                                                
                                       
                                    #print(sda4)
                                    sda2=sda4
                                    wer=sda4
                                    sda4=""

                                    Circle_times2=Circle_times2+1
                                    Count1=Count1-1
                                    
                                    c=c+1
                                    if c==256:
                                        c=0

                             
                                        
                                    
                                    if  Count1==0:
                                       
                                         n = int(wer, 2)
                                         qqwslenf=len(wer)
                                         qqwslenf=(qqwslenf/8)*2
                                         qqwslenf=str(qqwslenf)
                                         qqwslenf="%0"+qqwslenf+"x"
                                         jl=binascii.unhexlify(qqwslenf % n)
                                         sssssw=len(jl)

                                         szxzzza=""
                                         szxzs=""
                                            
                                         f2.write(jl)
                                         x2 = time()
                                         x3=x2-x
                                         return print(x3)
                                        
                                
  
                                if i==1:
                                    
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

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""

                                    ei=0
                                    
                                    if Circle_times2>=1:

                                        sda2=sda20

                                    count_times4=0
                                    
                                    if Circle_times2%3:
                                        c=1
                                    if Circle_times2%4:
                                        c=5
                                    if Circle_times2%5:
                                        c=7
                                    if Circle_times2%6:
                                        c=8

                                    if Circle_times2%7:
                                        c=3

                                    if Circle_times2%8:
                                        c=4

                                    if Circle_times2%9:
                                        c=6
                                        
                                    
                                    if Circle_times2%10:
                                        c=9
                                        
                                    if Circle_times2%11:
                                        c=2
                                    if Circle_times2%12:
                                        c=11
                                    if Circle_times2%13:
                                        c=10
                                    

                                    while ei<lenf6:
                                        

                                        sda10=sda3[ei:ei+1]
                                        ei=ei+1

                                        if Circle_times2==Circle_times2%3:

                                        
                                            if sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei<=Circle_times2:
                                                sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei<=Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                            
                                            
                                        elif Circle_times2==Circle_times2%1*(lenf7*8):

                                            if sda10=="1" and ei==Circle_times2%c:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei==Circle_times2%c: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei!=Circle_times2%c:
                                                    sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei!=Circle_times2%c: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                
                                        elif Circle_times2==Circle_times2%2*(lenf7*8):
                                            
                                            if sda10=="1" and ei==Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei==Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1

                                        else:

                                            if sda10=="1" and ei!=Circle_times2:
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                                    

                                            elif sda10=="0" and ei!=Circle_times2: 
                                                    sda4=sda4+"0"
                                                    

                                            elif sda10=="1" and ei==Circle_times2:
                                                sda4=sda4+"0"
                                                    
                                                    

                                            elif sda10=="0" and ei==Circle_times2: 
                                                    sda4=sda4+"1"
                                                    count_times4=count_times4+1
                                            
                                        
                                            
                                            
                                        
                                    #print(count_times4)
                                    #print(sda4)
                                    #print(ei)
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    
                                    sda2=sda6

                                    
                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                        Circle_times2=Circle_times2+1


                                        if  Circle_times2==(2**48)-1:
                                            raise SystemExit
                                            
                                        c=c+1
                                        
                                        if c==256:
                                            c=0


                                       
                                        
                                        if  count_times4==(lenf7*8):
                                            

                                            szx=""
                                            #print(count_times4)
                                            szx1=bin(count_times4)[2:]
                                            #print(szx1)
                                            lenf=len(szx1)
                                            #print(lenf)

                                            sda14=""
                                                
                                            #print(lenf)
                                            xc=48-lenf%48
                                            z=0
                                            if xc!=0:
                                                if xc!=48:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1
                                        
                                            sda14=szx+szx1
                                            #print(sda14)

                                          
                                            szx1=bin(Circle_times2)[2:]
                                            lenf=len(szx1)
                                            #print(lenf)

                                            sda15=""
                                            szx=""    
                                            #print(lenf)
                                            xc=48-lenf%48
                                            z=0
                                            if xc!=0:
                                                if xc!=48:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1
                                        
                                            sda15=szx+szx1

                                            wer=sda15+sda14
                                            

                                            n = int(wer, 2)
                                            qqwslenf=len(wer)
                                            qqwslenf=(qqwslenf/8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                              
                                            
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)





d=compression()

xwc3=d.Areacu2()
print(xwc3)

xwc2=d.Areac2()
print(xwc2)

xw=d.cryptograpy_compression2()
print(xw)

xw2=d.cryptograpy_compression()
print(xw2)

xw3=d.cryptograpy_compression3()
print(xw3)
