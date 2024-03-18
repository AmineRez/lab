from django.shortcuts import render
from django.http import HttpResponse
import math
donnees_90 = {
    -45: {'F': {'cpe10': -1.4, 'cpe1': -2.0}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10': -1.0, 'cpe1': -1.3}, 'I': {'cpe10': -0.9, 'cpe1': -1.2}},
    -30: {'F': {'cpe10': -1.5, 'cpe1': -2.1}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10': -1.0, 'cpe1': -1.3}, 'I': {'cpe10': -0.9, 'cpe1': -1.2}},
    -15: {'F': {'cpe10': -1.9, 'cpe1': -2.5}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10': -0.8, 'cpe1': -1.2}, 'I': {'cpe10': -0.8, 'cpe1': -1.2}},
    -5: {'F': {'cpe10': -1.8, 'cpe1': -2.5}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10': -0.7, 'cpe1': -1.2}, 'I': {'cpe10': -0.6, 'cpe1': -1.2}},
    5: {'F': {'cpe10': -1.6, 'cpe1': -2.2}, 'G': {'cpe10': -1.3, 'cpe1': -2.0}, 'H': {'cpe10': -0.7, 'cpe1': -1.2}, 'I': {'cpe10': -0.6, 'cpe1': -0.6}},
    15: {'F': {'cpe10': -1.3, 'cpe1': -2.0}, 'G': {'cpe10': -1.3, 'cpe1': -2.0}, 'H': {'cpe10': -0.6, 'cpe1': -1.2}, 'I': {'cpe10': -0.5, 'cpe1': -0.5}},
    30: {'F': {'cpe10': -1.1, 'cpe1': -1.5}, 'G': {'cpe10': -1.4, 'cpe1': -2.0}, 'H': {'cpe10': -0.8, 'cpe1': -1.2}, 'I': {'cpe10': -0.5, 'cpe1':-0.5}},
    45: {'F': {'cpe10': -1.1, 'cpe1': -1.5}, 'G': {'cpe10': -1.4, 'cpe1': -2.0}, 'H': {'cpe10': -0.9, 'cpe1': -1.2}, 'I': {'cpe10': -0.5, 'cpe1': -0.5}},
    60: {'F': {'cpe10': -1.1, 'cpe1': -1.5}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10':-0.8, 'cpe1': -1.0}, 'I': {'cpe10': -0.5, 'cpe1': -0.5}},
    75: {'F': {'cpe10': -1.1, 'cpe1': -1.5}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10':-0.8, 'cpe1': -1.0}, 'I': {'cpe10': -0.5, 'cpe1': -0.5}}
}
donnees_0 = {
       
    -45: {'F': {'cpe10': -0.6, 'cpe1': -0.6}, 'G': {'cpe10': 0.6, 'cpe1': 0.6}, 'H': {'cpe10': -0.8, 'cpe1': -0.8}, 'I': {'cpe10': -0.7, 'cpe1': -0.7}, 'J': {'cpe10': -1.0, 'cpe1': -1.5}},
    -30: {'F': {'cpe10': -1.1, 'cpe1': -2.0}, 'G': {'cpe10': -0.8, 'cpe1': -1.5}, 'H': {'cpe10': -0.8, 'cpe1': -0.8}, 'I': {'cpe10': -0.6, 'cpe1': -0.8}, 'J': {'cpe10': -1.4, 'cpe1': -0.8}},
    -15:{'F': {'cpe10': -2.5, 'cpe1': -2.8}, 'G': {'cpe10': -1.3, 'cpe1': -2.0}, 'H': {'cpe10': -0.9, 'cpe1': -1.2}, 'I': {'cpe10': -0.5, 'cpe1': -0.5}, 'J': {'cpe10': -0.7, 'cpe1': -1.2}},
    -5: {'F': {'cpe10': -2.3, 'cpe1': -2.5}, 'G': {'cpe10': -1.2, 'cpe1': -2.0}, 'H': {'cpe10': -0.8, 'cpe1': -1.2},'I': {'cpe10': [0.2, -0.6], 'cpe1': [0.2, -0.6]},'J': {'cpe10': [+0.2, -0.6], 'cpe1': [+0.2, -0.6]}},
    15: {'F': {'cpe10': [-0.9, +0.2], 'cpe1': [-2.0, +0.2]}, 'G': {'cpe10': [-0.8,+0.2], 'cpe1': [-1.5, 0.2]}, 'H': {'cpe10': [-0.3, 0.2], 'cpe1':  [-0.3, 0.2]},'I': {'cpe10': [-0.4, 0], 'cpe1': [-0.4, 0]},'J': {'cpe10': [-1, 0], 'cpe1': [-1.5, 0]}},
    5: {'F': {'cpe10': [-1.7, 0], 'cpe1': [-2.5, 0]}, 'G': {'cpe10': [-1.2, 0], 'cpe1': [-2.0, 0]}, 'H': {'cpe10': [-0.6, 0], 'cpe1': [-1.2, 0]},'I': {'cpe10': -0.6, 'cpe1': -0.6},'J': {'cpe10': [+0.2, -0.6], 'cpe1': [+0.2, -0.6]}},
    30: {'F': {'cpe10': [-0.5, 0.7], 'cpe1': [-1.5, 0.7]}, 'G': {'cpe10': [-0.5, 0.7], 'cpe1': [-1.5, 0.7]}, 'H': {'cpe10': [-0.2, 0.4], 'cpe1':[-0.2, 0.4]},'I': {'cpe10': [-0.4, 0], 'cpe1': [-0.4, 0]},'J': {'cpe10': [-0.5, 0], 'cpe1': [-0.5, 0]}},

    45: {'F': {'cpe10': [0, 0.7], 'cpe1': [0, 0.7]}, 'G': {'cpe10':[0, 0.7], 'cpe1': [0, 0.7]}, 'H': {'cpe10': [0, 0.6], 'cpe1':[-0.2, 0]},'I': {'cpe10': [-0.2, 0], 'cpe1': [-0.2, 0]},'J': {'cpe10': [-0.3, 0], 'cpe1': [-0.3, 0]}},
    60:{'F': {'cpe10': 0.7, 'cpe1': 0.7}, 'G': {'cpe10': 0.7, 'cpe1': 0.7}, 'H': {'cpe10': 0.7, 'cpe1': 0.7}, 'I': {'cpe10': 0.7, 'cpe1': 0.7}, 'J': {'cpe10': -0.2, 'cpe1': -0.3}},
    75:{'F': {'cpe10': 0.8, 'cpe1': 0.8}, 'G': {'cpe10': 0.8, 'cpe1': 0.8}, 'H': {'cpe10': 0.8, 'cpe1': 0.8}, 'I': {'cpe10': 0.8, 'cpe1': 0.8}, 'J': {'cpe10': -0.2, 'cpe1': -0.3}}
  


    
}
ensemble_nbr = [-45, -30, -5, -15, 5, 15, 30, 45, 60, 75]
donnees_parois={'A': {'cpe10': -1.0, 'cpe1': -1.3},
                'B': {'cpe10': -0.8, 'cpe1': -1.0},
                'C': {'cpe10': -0.5, 'cpe1': -0.5}
                }
                
def nuage(request):
    print(request.POST)
    if request.method == 'POST':
        zone = request.POST.get("zone")
        versent=request.POST.get('versent')
        degr1 = request.POST.get('deg1')
        degr2 = request.POST.get('deg2')
        hauteur = request.POST.get('hauteur')
        if versent == "Double versent" :
            if degr1 and hauteur and degr2 :
                deg1 = float(degr1)
                deg2 = float(degr2)
                h=float(hauteur)
                if 0 <= deg1 < 30:
                    u1 = 0.8
                elif 30 <= deg1 < 60:
                    u1 = 0.8 * ((60 - deg1) / 30)
                else:
                    u1 = 0
                if 0 <= deg2 < 30:
                    u2 = 0.8
                elif 30 <= deg2 < 60:
                    u2 = 0.8 * ((60 - deg1) / 30)
                else:
                    u2 = 0
                if zone == "Zone A":
                    sk = (0.07 * h + 15) / 100
                elif zone == "Zone B":
                    sk = (0.04 * h + 15) / 10
                elif zone == "Zone C":
                    sk = (0.0325 * h) / 100
                elif zone == "Zone D":
                    sk = 0
                
                sk = 0
                s1=u1*sk
                s2=u2*sk
                context = {
                            's1': s1,
                            's2': s2,
                            'u1':u1,
                            'u2':u2,
                    }
                return render(request,'Dashbord.html',context)
        else:
            return HttpResponse('Manque un variable a entree') 
    else:
        return render(request,'Dashbord.html')

def choix(request):
    
     return render(request,'choix.html')
def dessin(request):
     return render(request,'dessin.html')
def vent(request):
     if request.method == 'POST':
        
        v=request.POST.get('versent')
        ponte = request.POST.get('ponte')
        s=request.POST.get('s')
        de = request.POST.get('d')
        b = request.POST.get('b')
        h=request.POST.get('h')
        if v and ponte and b and de and s:
            v=int (v)
            b=float(b)
            de=float(de)
            s=float(s)
            h=float(h)
            e=min(b,2*h)
            ponte=float(ponte)
            

# Parcourir l'ensemble de nombres
            
            if ponte in ensemble_nbr:
                if v==90:
                    bool=1
                    d=donnees_90   
                else:
                    d=donnees_0
                    bool=0
                    if s<=1:
                     cpej=d[ponte]['J']['cpe10']
                    elif 1 < s < 10:
                     if isinstance(d[ponte]['J']['cpe1'], list):
                         cpej1=d[ponte]['J']['cpe1'][0] -(d[ponte]['J']['cpe1'][0]-d[ponte]['J']['cpe10'][0])*math.log(s, 10)
                         cpej2=d[ponte]['J']['cpe1'][1] -(d[ponte]['J']['cpe1'][1]-d[ponte]['J']['cpe10'][1])*math.log(s, 10)
                         cpej=[cpej1,cpej2]
                     else:
                         cpej=d[ponte]['J']['cpe1'] -(d[ponte]['J']['cpe1']-d[ponte]['J']['cpe10'])*math.log(s, 10)

                    elif s >= 10:
                     cpej=d[ponte]['J']['cpe10']

                if s<=1:
                    cpef=d[ponte]['F']['cpe1']
                    cpeg=d[ponte]['G']['cpe1']
                    cpeh=d[ponte]['H']['cpe1']
                    cpei=d[ponte]['I']['cpe1']
                elif 1 < s < 10:
                   
                    if isinstance(d[ponte]['F']['cpe1'] , list):
                     
                     cpef1=d[ponte]['F']['cpe1'][0] -(d[ponte]['F']['cpe1'][0]-d[ponte]['F']['cpe10'][0])*math.log(s, 10)
                     cpef2=d[ponte]['F']['cpe1'][1] -(d[ponte]['F']['cpe1'][1]-d[ponte]['F']['cpe10'][1])*math.log(s, 10)
                     cpef1 = "{:.2f}".format(cpef1)
                     cpef2 = "{:.2f}".format(cpef2)
                     cpef=[cpef1,cpef2]
                    else:
                     
                     cpef=d[ponte]['F']['cpe1'] -(d[ponte]['F']['cpe1']-d[ponte]['F']['cpe10'])*math.log(s, 10)
                     cpef = "{:.2f}".format(cpef)
                    if isinstance(d[ponte]['G']['cpe1'] , list):
                     cpeg1=d[ponte]['G']['cpe1'][0] -(d[ponte]['G']['cpe1'][0]-d[ponte]['G']['cpe10'][0])*math.log(s, 10)
                     cpeg2=d[ponte]['G']['cpe1'][1] -(d[ponte]['G']['cpe1'][1]-d[ponte]['G']['cpe10'][1])*math.log(s, 10)
                     cpeg1 = "{:.2f}".format(cpeg1)

                     cpeg2 = "{:.2f}".format(cpeg2)
                     cpeg=[cpeg1,cpeg2]
                    else:
                        cpeg=d[ponte]['G']['cpe1'] -(d[ponte]['G']['cpe1']-d[ponte]['G']['cpe10'])*math.log(s, 10)
                        
                        cpeg = "{:.2f}".format(cpeg)
                    if isinstance(d[ponte]['H']['cpe1'] , list):
                        cpeh1=d[ponte]['H']['cpe1'][0] -(d[ponte]['H']['cpe1'][0]-d[ponte]['H']['cpe10'][0])*math.log(s, 10)
                        cpeh2=d[ponte]['H']['cpe1'][1] -(d[ponte]['H']['cpe1'][1]-d[ponte]['H']['cpe10'][1])*math.log(s, 10)
                        cpeh1 = "{:.2f}".format(cpeh1)
                        cpeh2 = "{:.2f}".format(cpeh2)
                        cpeh=[cpeh1,cpeh2]
                    else:
                     cpeh=d[ponte]['H']['cpe1'] -(d[ponte]['H']['cpe1']-d[ponte]['H']['cpe10'])*math.log(s, 10)
                     
                     cpeh = "{:.2f}".format(cpeh)
                    if isinstance(d[ponte]['I']['cpe1'] , list):

                      cpei1=d[ponte]['I']['cpe1'][0] -(d[ponte]['I']['cpe1'][0]-d[ponte]['I']['cpe10'][0])*math.log(s, 10)
                      cpei2=d[ponte]['I']['cpe1'][1] -(d[ponte]['I']['cpe1'][1]-d[ponte]['I']['cpe10'][1])*math.log(s, 10)
                      cpei1 = "{:.2f}".format(cpei1)
                      cpei2 = "{:.2f}".format(cpei2)
                      cpei=[cpei1,cpei2]
                    else:
                         cpei=d[ponte]['I']['cpe1'] -(d[ponte]['I']['cpe1']-d[ponte]['I']['cpe10'])*math.log(s, 10)
                         
                         cpei = "{:.2f}".format(cpei)
                elif s >= 10:
                    cpef=d[ponte]['F']['cpe10']
                    cpeg=d[ponte]['G']['cpe10']
                    cpeh=d[ponte]['H']['cpe10']
                    cpei=d[ponte]['I']['cpe10']
            else:
                for i in range(len(ensemble_nbr) - 1):
                 if ensemble_nbr[i] <= ponte < ensemble_nbr[i + 1]:
                    max=ensemble_nbr[i]
                    mn=ensemble_nbr[i + 1]
                    print(f"La valeur {ponte} est entre {ensemble_nbr[i]} et {ensemble_nbr[i + 1]}")
                    
                print(mn)
                print(max)
                if v==90:
                    bool=1
                    d=donnees_90   
                else:
                    d=donnees_0
                    bool=0
                    if s<=1:
                        cpejmin=d[mn]['J']['cpe1']
                        cpejmax=d[max]['J']['cpe1']

                    elif 1 < s < 10:
                        cpejmin=d[mn]['J']['cpe1'] -(d[mn]['J']['cpe1']-d[mn]['J']['cpe10'])*math.log(s, 10)
                        cpejmax=d[max]['J']['cpe1'] -(d[max]['J']['cpe1']-d[max]['J']['cpe10'])*math.log(s, 10)
                        print(cpejmin)
                    elif s >= 10:
                        cpejmin=d[mn]['J']['cpe10']
                        cpejmax=d[max]['J']['cpe10']
                    cpej = (((max - mn) * cpejmax - (max - ponte) * (cpejmax - cpejmin)) / (max - mn))
                    cpej = "{:.2f}".format(cpej)


                if s<=1:
                    cpefmin=d[mn]['F']['cpe1']
                    cpefmax=d[max]['F']['cpe1']
                    cpegmin=d[mn]['G']['cpe1']
                    cpegmax=d[max]['G']['cpe1']
                    cpehmin=d[mn]['H']['cpe1']
                    cpehmax=d[max]['H']['cpe1']
                    cpeimin=d[mn]['I']['cpe1']
                    cpeimax=d[max]['I']['cpe1']
                elif 1 < s < 10:
                    cpefmin=d[mn]['F']['cpe1'] -(d[mn]['F']['cpe1']-d[mn]['F']['cpe10'])*math.log(s, 10)
                    cpegmin=d[mn]['G']['cpe1'] -(d[mn]['G']['cpe1']-d[mn]['G']['cpe10'])*math.log(s, 10)
                    cpehmin=d[mn]['H']['cpe1'] -(d[mn]['H']['cpe1']-d[mn]['H']['cpe10'])*math.log(s, 10)
                    cpeimin=d[mn]['I']['cpe1'] -(d[mn]['I']['cpe1']-d[mn]['I']['cpe10'])*math.log(s, 10)
                    cpefmax=d[max]['F']['cpe1'] -(d[max]['F']['cpe1']-d[max]['F']['cpe10'])*math.log(s, 10)
                    cpegmax=d[max]['G']['cpe1'] -(d[max]['G']['cpe1']-d[max]['G']['cpe10'])*math.log(s, 10)
                    cpehmax=d[max]['H']['cpe1'] -(d[max]['H']['cpe1']-d[max]['H']['cpe10'])*math.log(s, 10)
                    cpeimax=d[max]['I']['cpe1'] -(d[max]['I']['cpe1']-d[max]['I']['cpe10'])*math.log(s, 10)
                elif s >= 10:
                    cpefmin=d[mn]['F']['cpe10']
                    cpegmin=d[mn]['G']['cpe10']
                    cpehmin=d[mn]['H']['cpe10']
                    cpeimin=d[mn]['I']['cpe10']
                    cpefmax=d[max]['F']['cpe10']
                    cpegmax=d[max]['G']['cpe10']
                    cpehmax=d[max]['H']['cpe10']
                    cpeimax=d[max]['I']['cpe10']

                cpef=(((ensemble_nbr[i +1]-ensemble_nbr[i ]))*cpefmax-(ensemble_nbr[i+1 ]-ponte)*(cpefmax-cpefmin))/(ensemble_nbr[i+1]-ensemble_nbr[i])
                cpeg=(((ensemble_nbr[i +1]-ensemble_nbr[i ]))*cpegmax-(ensemble_nbr[i+1 ]-ponte)*(cpegmax-cpegmin))/(ensemble_nbr[i+1]-ensemble_nbr[i])
                cpeh=(((ensemble_nbr[i +1]-ensemble_nbr[i ]))*cpehmax-(ensemble_nbr[i+1 ]-ponte)*(cpehmax-cpehmin))/(ensemble_nbr[i+1]-ensemble_nbr[i])
                cpei=(((ensemble_nbr[i +1]-ensemble_nbr[i ]))*cpeimax-(ensemble_nbr[i+1 ]-ponte)*(cpeimax-cpeimin))/(ensemble_nbr[i+1]-ensemble_nbr[i])

                cpef = "{:.2f}".format(cpef)
                cpeg = "{:.2f}".format(cpeg)
                cpeh = "{:.2f}".format(cpeh)
                cpei = "{:.2f}".format(cpei)
            
            
            
            e4=e/4
            e10=e/10
            e2=e/2

            #bool=1 affiche 90
            #bool=0 affiche 0
            if v==0:
                print(cpef)

                context={
                    'cpef':cpef,'cpeg':cpeg,'cpeh':cpeh,'cpei':cpei,'bool':bool,'e4':e4,'e10':e10,'e2':e2
                    ,'de':de,'b':b,'ve':v,'cpej':cpej
                }
            else:
                context={
                    'cpef':cpef,'cpeg':cpeg,'cpeh':cpeh,'cpei':cpei,'bool':bool,'e4':e4,'e10':e10,'e2':e2
                    ,'de':de,'b':b,'ve':v
                }

            return render(request,'vent.html',context)
            
            

     

     
   
     return render(request,'vent.html')
    

def parois(request):
      if request.method == 'POST':
        de = request.POST.get('d')
        b = request.POST.get('b')
        h=request.POST.get('h')
        s=request.POST.get('s')
        if h and b and de and s :
            b=float(b)
            de=float(de)
            h=float(h)
            s=float(s)
            e=min(b,2*h)
            if de>e:
                bool=1
            elif de<=e:
                bool=2
            elif de<=e/5:
                bool=3
            d_e=de-e
            de5 = "{:.2f}".format(de-e/5)
            e45 = "{:.2f}".format((4*e)/5)
            e5 = "{:.2f}".format(e/5)
            if s<=1:
                    cpea=donnees_parois['A']['cpe1']
                    cpeb=donnees_parois['B']['cpe1']
                    cpec=donnees_parois['C']['cpe1']
            elif 1 < s < 10:
                cpea=donnees_parois['A']['cpe1'] -(donnees_parois['A']['cpe1']-donnees_parois['A']['cpe10'])*math.log(s, 10)    
                cpea = "{:.2f}".format(cpea)
                cpeb=donnees_parois['B']['cpe1'] -(donnees_parois['B']['cpe1']-donnees_parois['B']['cpe10'])*math.log(s, 10)    
                cpeb = "{:.2f}".format(cpeb)
                cpec=donnees_parois['C']['cpe1'] -(donnees_parois['C']['cpe1']-donnees_parois['C']['cpe10'])*math.log(s, 10)    
                cpec = "{:.2f}".format(cpec)
            elif s >= 10:
                    cpea=donnees_parois['A']['cpe10']
                    cpeb=donnees_parois['B']['cpe10']
                    cpec=donnees_parois['C']['cpe10']
                   
            context={'bool':bool,'h':h,'e':e,'d_e':d_e,'de5':de5,
                    'e45':e45,'e5':e5,'cpea':cpea,'cpeb':cpeb,'cpec':cpec}
            return render(request,'parois.html',context)    
      else:
          return render(request,'parois.html')   

            


     

