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

                    

                   
                    gl=0
                    w=1590904043117983597909504317833589909108214261558493560152878025583597170790994793761833238313746714438563217760761021318185392914680567654946911604622813401377333684367030821477521615431377548714003777903466735886038996099755007843318330568998121903361463127092845345619991066997607252608323524833005393560352818357912123148158934344873739639348551765116658160577928117757736516405416059002048112291268665296776053825385586865515330915518894974146330002912468768894612994110068211432261359636877057555602530960273056825235372450285337259037111647233090012701745087036047932412728657820763143018017185534997197995705377603217756193204929065325864828749536198606187219703576670639024325718842262038894633935380482727514232258163682127527657226440834440600353929458763353700183458964362975365187782392518540894851825734224414952415842378832686357527130758799350334262043316046196741587757971302514669152498636632205651324162410006598735036065372207508214108101413401919895325636354940920535693006609137127995356020073499253596775140266441958549921224378243230763955476633382124690340069174762214199387776080311109721225040801259152061307806372811261004528893965402450244699000310628198150839144754122749381155921031334704016945977699582198303926225456724207163106218005189877801588630263984450533497556861489656297943420364774167620936532276103181312382295945356499982096200888485436242799220547098153092806256985093734483461743285421246264009557822950504238987199620681935021939924047209670920649247036084625828576909232250741680906787823068737896504971182659880033145103559761207700359385386412555283497527783280123162467675925721469718338611024976498389574972165578014997141123426979416301279510397652280229315573099206841028314747845953064562454520066017043210891239828620909373460511863261934852585259609926101027871095508146465423982186617555188559990235991678930353574208562263783846118237564024842092976395720560954138357141119323357995154154093766843768018941206872452639653687919489608944433293286017636779605726900461613706182322505931122524403505748399629682829354717797256471727090699475874344983496578506017364828221564239683884439765065475494705836417389745951123095649989947027361655754150121847911177253233684724413201563895726148224170868839906535019424924439162491981290050167920455918942028473415367864134440144452464087629732299106566984777356347741817700322126618906769543512836142744297729724451580957337743105306145675484226666590541055918407
                    r=570680970380700147286910002752565996723146922846311050693255455656583188695574169983564737872518638988438988273739870163544619251661597589394051377993945646646701680811168654352257781193191366082061441606205501534840333248731631914805688265893245261085333710873614168579211133300108065814930608821739898493572175848157903811172212641478089161230397746595213514140605983261247673566449947819952379482811647043753560096133525923488103151959332073199693141749640176005482347621566852523253970745393220050270928733482004119944592785928548319882868080150032894868996024107891961274826369112170553784039879908152117033879956403469413546817515878962298436940555671335834287365685998363185449281159389214168886468284572785813070049571959879095411262154713058283418443074119641639381663672622830304299200236597276251116150253255338378848917470364964907808329516339019635270991186150900162957335102630607453158098391884793105735024414217665310250180834460066255667944723090989802610291073564178773882519717578738885755769362393732992648958672958602042242769869244524616450092445039120784134596788075826619013428921355192279853863285674679520324986322878943758047079795530989017174990267902183848631367633747563446767657193319197693940070676868944109218278117827180816311086410458782278153694559793557089629236256839371830316804135874166271418199093787743651767790759217420329521727538664377306976572620397309966843482780106130600814322603691949497136324934243796304800221201305742055429394930683094525502746926798062515489412235859265600388913071780289984679206177156006660823964746930354383338615516685209109710753292245170358716056184286348699273660871509093378473407097983563994669068356325176520591567977512061793835387048140477870971680071342134452492083991164658002498458256560567312801090240748766295114685846480161642900225709428084111844484296909208902303986638684432362151426047935482248443349420448962436981895389925883636475585974289707677490143019124084035323651526991236660189507708264508403944431278843689005386447020332412089862505911306686395933621725306221804569913612243101589948379504440282545160749525801047969909786154406482863230989013790044095439070661598336986056976180132983916960682404096274929682824439781430122970699776839179040885814032482155023707866493865618467206706981416197636320917381235630617539848215267660974285189671009373860152765138394070262601593306297301629724302185392432104100882669541763223623385762872761114410375020784311609981
                    




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
                        iii=0

                        if nameas[nac-3:nac]==".b2":
                            iii=1
                            
                            
                        if nameas[nac-4:nac]!=".bin" and iii!=1:
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

                        if name[nac-4:nac]==".mp4":
                            if data[0:3]!=b'\x00\x00\x00' or data[0:4]==b'\x00\x00\x00\x00':
                                print("Sorry, this is incorrect file")
                                raise SystemExit
                        
                        elif data[0:1]==b'\x00':
                            print("Sorry, this is incorrect file")
                            raise SystemExit
                       
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

                                    if sda2[0:1]=="1":
                                        g=2

                                    if sda2[0:1]=="0":
                                        g=1

                                    if g==2 and iii==1:
                                        x=0
                                        x1=0
                                        x2=0
                                        x = time()
                                        #name = input("What is name of file? ")
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
                                                            eo=eo+2523105
                                                            takebitsize=sda[el:eo]
                                                            xssd=len(takebitsize)
                                                            el=eo-2523105
                                                            eo=eo-2523105
                                                            if xssd<=2523104:
                                                                wer=wer+takebitsize
                                                                   
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
                                                                    
                                                                wer=wer+takebit
                                                                sw=sw+1
                                                                   
                                                            wers=""    
                                                           
                                                    lenf=len(wer)
                                                    xc=8-lenf%8
                                                    z=0
                                                    if xc!=0 and xc!=8:
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
                                    
                                    if g==1 and iii!=1:

                                        sda3=sda2
                                        sda2=sda2[1:]

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

                                    
                                    
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""

                                    


                                    sda4=sda3[1:]#lenf2
                                    
                                    sda4=str(sda4)
                                    
                                    om=int(sda4, 2)


                                    d=r-0
                                    Bytes_row2=om+d

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


                                    if nameas[nac-4:nac]==".mp4":
                                        jl = b'\x00\x00\x00'+jl 

                                    nameasr=nameas
                                                            
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

                                    d=r-0

                                    bit_variotions="0"
                                    

                                    Bytes_row3=Bytes_row1-d
                                    
                                    if Bytes_row3<0:
                                         print("Sorry, this is incorrect file")
                                         raise SystemExit
                                         
                                         
                                         

                                    elif Bytes_row3>=0:
                                         Spin=1
                                         
                                         
                                        

                                 
                                    
                                    
                 
                                    
                                    
                                        
                                    #if  -1 count + round add then this to this number
                                    
                                    if Spin==1:
                                         
                                        
                                         
                                    #The colaider count information that got
                                    #n2 Long of the bytes that we got.

                                         sda4=bit_variotions+sda4
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
                                        jl1=binascii.unhexlify(qqwslenf % n)
                                        sssssw=len(jl1)

                                        
                                            

                                                        
                                        Circle_times=Circle_times+1
                                        szxzzza=""
                                        szxzs=""
                                        sda2=sda6
                                                        
                                        Circle_times2=Circle_times2+1

                                        x=0
                                        x1=0
                                        x2=0
                                        x = time()
                                        #name = input("What is name of file? ")
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
                                            
                                        
                                        namea=name+".bin"
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
                                            if lenf1<400000:
                                                jl=jl1
                                                f2.write(jl)
                                                x2 = time()
                                                x3=x2-x
                                                return print(x3)

                                                
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
                                                    jl3=jl1
                                                                
                                                    f2.write(jl3)
                                                    x2 = time()
                                                    x3=x2-x
                                                    return print(x3)
                                                
                                                if lenfg>0:
                                                    acvb=lenfg-1
                                                    ss=0
                                                    ww=0
                                                   
                                                    acvb=lenfg-1
                                                    notexist=k[0]
                                                    
                                                   
                                                    
                                                    if notexist>16383 or notexist<0:
                                                        jl3=jl1
                                                                    
                                                        f2.write(jl3)
                                                        x2 = time()
                                                        x3=x2-x
                                                        return print(x3)
                                                                        
                                                        
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
                                                            jl3=jl1
                                                                        
                                                            f2.write(jl3)
                                                            x2 = time()
                                                            x3=x2-x
                                                            return print(x3)
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
                                        jl2=binascii.unhexlify('%x' % n)

                                        
                                        nameas1=name+".b2"
                                        
                                        with open(nameas1, "wb") as f4:
                                            f4.write(jl2)
                                        
                                        f2.write(jl1)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

d=compression()

xw=d.cryptograpy_compression()
