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
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""

                                    sda4=sda3[0:]#lenf2
                                    
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
                                    

                                    Bytes_row3=Bytes_row1-d
                                    
                                    if Bytes_row3<0:
                                         raise SystemExit
                                        

                                 
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
                                        
                                        
                                                                                                									

                                        wer="1"+wer+"1"
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

                                    
                                                        
                                        
                                        f2.write(jl)
                                        x2 = time()
                                        x3=x2-x
                                        return print(x3)

d=compression()

xw=d.cryptograpy_compression()
