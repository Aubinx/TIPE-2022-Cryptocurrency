import ccxt
from matplotlib.pyplot import *
from math import *

text_btc = r'Time Series\btc.txt'
text_valeurs = r'Time Series\valeurs.txt'
text_valeurs_comparaison = r'Time Series\valeurs_comparaison.txt'
text_correlation = r'Time Series\correlation.txt'
text_correlation_n = r'Time Series\correlation_n.txt'
text_correlation_n2 = r'Time Series\correlation_n2.txt'

text_ada_usdt = r'Time Series\ada-usdt.txt'
text_btc_usdt = r'Time Series\btc-usdt.txt'
text_doge_usdt = r'Time Series\doge-usdt.txt'
text_dot_usdt = r'Time Series\dot-usdt.txt'
text_eth_usdt = r'Time Series\eth-usdt.txt'
text_xrp_usdt = r'Time Series\xrp-usdt.txt'
text_comparaison = r'Time Series\comparaison.txt'

text_liste_heures_ada = r'Time Series\liste-heures-ada.txt'
text_liste_heures_btc_1 = r'Time Series\liste-heures-btc-1.txt'
text_liste_heures_btc_2 = r'Time Series\liste-heures-btc-2.txt'
text_liste_heures_doge = r'Time Series\liste-heures-doge.txt'
text_liste_heures_dot = r'Time Series\liste-heures-dot.txt'
text_liste_heures_eth = r'Time Series\liste-heures-eth.txt'
text_liste_heures_xrp = r'Time Series\liste-heures-xrp.txt'
text_liste_heures_comparaison = r'Time Series\liste-heures-comparaison.txt'

text_liste_hamming = r'Time Series\liste-hamming.txt'
text_liste_hamming_btc = r'Time Series\liste-hamming-btc.txt'
text_liste_hamming_comparaison = r'Time Series\liste-hamming-comparaison.txt'

text_liste_octet_ada = r'Time Series\liste-octet-ada.txt'
text_liste_octet_btc_1 = r'Time Series\liste-octet-btc-1.txt'
text_liste_octet_btc_2 = r'Time Series\liste-octet-btc-2.txt'
text_liste_octet_doge = r'Time Series\liste-octet-doge.txt'
text_liste_octet_dot = r'Time Series\liste-octet-dot.txt'
text_liste_octet_eth_1 = r'Time Series\liste-octet-eth-1.txt'
text_liste_octet_eth_2 = r'Time Series\liste-octet-eth-2.txt'
text_liste_octet_xrp = r'Time Series\liste-octet-xrp.txt'
text_liste_octet_comparaison = r'Time Series\liste-octet-comparaison.txt'

text_liste_octet_1 = r'Time Series\liste-octet-1.txt'
text_liste_octet_2 = r'Time Series\liste-octet-2.txt'
text_liste_octet_3 = r'Time Series\liste-octet-3.txt'
text_liste_octet_4 = r'Time Series\liste-octet-4.txt'

text_liste_octet2_1 = r'Time Series\liste-octet2-1.txt'
text_liste_octet2_2 = r'Time Series\liste-octet2-2.txt'
text_liste_octet2_3 = r'Time Series\liste-octet2-3.txt'
text_liste_octet2_4 = r'Time Series\liste-octet2-4.txt'

text_performance_hamming = r'Time Series\performance-hamming.txt'
text_performance_octet = r'Time Series\performance-octet.txt'
text_performance_octet2 = r'Time Series\performance-octet2.txt'
text_performance_extremum = r'Time Series\performance-extremum.txt'
text_performance_extremum_rentabilite = r'Time Series\performance-extremum-rentabilite.txt'

liste_fichiers = [text_ada_usdt,text_btc_usdt,text_doge_usdt,text_dot_usdt,text_eth_usdt,text_xrp_usdt]

couples_lignes = [(0,1973400),(1973400,4296721),(4296721,5630139),(5630139,6372604),(6372604,8695951),(8695951,10644388)]

liste_fichiers_heures=[text_liste_heures_ada,text_liste_heures_btc_1,text_liste_heures_btc_2,text_liste_heures_doge,text_liste_heures_dot,text_liste_heures_eth,text_liste_heures_xrp]

liste_fichiers_octet=[text_liste_octet_ada,text_liste_octet_btc_1,text_liste_octet_btc_2,text_liste_octet_doge,text_liste_octet_dot,text_liste_octet_eth_1,text_liste_octet_eth_2,text_liste_octet_xrp]

exchange = ccxt.binance()

def plot_unix(unix):
    y=[]
    l = exchange.fetch_ohlcv('ETH/USDT', since=unix, limit=1000)
    for m in l:
        y.append(m[1])
    x=list(range(len(y)))
    figure()
    plot(x,y)
    show()

def plot_unix_2(m):
    unix=premiere_occurrence(m)
    y=[]
    while unix <= 1642341469000:
        print(unix)
        l = exchange.fetch_ohlcv(m, since=unix, limit=1000)
        for n in l:
            y.append(n[1])
        unix+=60000000
    x=list(range(len(y)))
    figure()
    plot(x,y)
    show()

def fichier(m):
    btc=open(text_btc, 'w')
    unix=1642374000000
    i=0
    y=[]
    while unix<1653827000000:
        print(unix)
        l = exchange.fetch_ohlcv(m, since=unix, limit=1000)
        for n in l:
            btc.write(str(n[0])+' '+str(n[1])+' '+str(n[2])+' '+str(n[3])+' '+str(n[4])+' '+str(n[5])+'\n')
        unix+=60000000
        y.append(n[1])
    btc.close()
    x=list(range(len(y)))
    figure()
    plot(x,y)
    show()

def premiere_occurrence(m):
    l = exchange.fetch_ohlcv('ETH/USDT', since=0, limit=1000)
    return l[0][0]

def fichier_compilation_valeurs():
    valeurs=open(text_valeurs,'w')
    for fichier in liste_fichiers:
        print(0)
        f=open(fichier,'r')
        c=f.readlines()
        for ligne in c:
            l=ligne.split(' ')
            valeurs.write(l[1]+"\n")
        f.close()
    valeurs.close()

def fichier_compilation_valeurs_2():
    valeurs=open(text_valeurs_comparaison,'w')
    f=open(text_comparaison,'r')
    c=f.readlines()
    for ligne in c:
        l=ligne.split(' ')
        valeurs.write(l[1]+"\n")
    f.close()
    valeurs.close()

def etablissement_liste_heures():
    lh=open(text_liste_heures_comparaison,'w')
    valeurs=open(text_valeurs_comparaison,'r')
    v=valeurs.read().splitlines()
    c=len(v)
    for i in range(c-59):
        if i%10000==0: print(i)
        a=''
        for j in range(60):
            a+=v[i+j]
            a+=' '
        lh.write(a+'\n')
    valeurs.close()
    lh.close()

def etablissement_liste_hamming():
    lham=open(text_liste_hamming,'w')
    for fichier in liste_fichiers_heures:
        print(0)
        f=open(fichier,'r')
        c=f.readlines()
        for ligne in c:
            s=''
            l=ligne.split(' ')
            for i in range(59):
                a,b=l[i],l[i+1]
                if a<b: s+='2'
                elif a>b: s+='0'
                else: s+='1'
            lham.write(s+'\n')
        f.close()
    lham.close()

def etablissement_liste_hamming_2():
    lham=open(text_liste_hamming_comparaison,'w')
    f=open(text_liste_heures_comparaison,'r')
    c=f.readlines()
    for ligne in c:
        s=''
        l=ligne.split(' ')
        for i in range(59):
            a,b=l[i],l[i+1]
            if a<b: s+='2'
            elif a>b: s+='0'
            else: s+='1'
        lham.write(s+'\n')
    f.close()
    lham.close()

def hamming_1(a,b):
    d=0
    for i in range(len(a)):
        d+=abs(int(a[i])-int(b[i]))
    return d

def octet(n):
    a=bin(n)[2:]
    b='0'*(8-len(a))
    return b+a+' '

def etablissement_liste_octet():
    lo=open(text_liste_octet_2,'w')
    f=open(text_liste_heures_comparaison,'r')
    c=f.readlines()
    for i in range(len(c)):
        ligne=c[i]
        if i%10000==0: print(i)
        l=ligne.split(' ')[:-1]
        m,s=[],''
        for x in l: m.append(float(x))
        a,b=min(m),max(m)
        for fl in m:
            if a==b: d=0
            else: d=int(255*(fl-a)/(b-a))
            s+=str(d)+' '
        lo.write(s+'\n')
    f.close()
    lo.close()

def etablissement_liste_correlation():
    valeurs=open(text_valeurs,'r')
    tc=open(text_correlation,'w')
    v=valeurs.read().splitlines()
    ada=1231000
    btc=1581000+1973400
    doge=4296721+591000
    dot=5630139
    eth=6372604+1580967
    xrp=8695951+1206000
    for i in range(742321):
        tc.write(v[ada]+' '+v[btc]+' '+v[doge]+' '+v[dot]+' '+v[eth]+' '+v[xrp]+'\n')
        ada+=1
        btc+=1
        doge+=1
        dot+=1
        eth+=1
        xrp+=1
    valeurs.close()
    tc.close()

def etablissement_liste_correlation_n():
    tc=open(text_correlation,'r')
    cn=open(text_correlation_n,'w')
    c=tc.read().splitlines()
    m=[[],[],[],[],[],[]]
    p=[]
    for ligne in c:
        l=ligne.split(' ')
        for i in range(6):
            m[i].append(float(l[i]))
    for n in m:
        q=[]
        a,b=min(n),max(n)
        for fl in n:
            q.append(str(int(255*(fl-a)/(b-a))))
        p.append(q)
    for i in range(len(p[0])):
        cn.write(p[0][i]+' '+p[1][i]+' '+p[2][i]+' '+p[3][i]+' '+p[4][i]+' '+p[5][i]+'\n')
    tc.close()
    cn.close()

def moyenne(L):
    s=0
    for i in L: s+=i
    return s/len(L)

def graphe_correlation():
    cn=open(text_correlation_n,'r')
    c=cn.readlines()
    cn.close()
    x=list(range(len(c)//100))
    y0,y1,y2,y3,y4,y5=[],[],[],[],[],[]
    for i in range(len(c)//100):
        l0,l1,l2,l3,l4,l5=[],[],[],[],[],[]
        for j in range(100):
            ligne=c[100*i+j]
            l=ligne.split(' ')
            l0.append(int(l[0]))
            l1.append(int(l[1]))
            l2.append(int(l[2]))
            l3.append(int(l[3]))
            l4.append(int(l[4]))
            l5.append(int(l[5]))
        y0.append(moyenne(l0))
        y1.append(moyenne(l1))
        y2.append(moyenne(l2))
        y3.append(moyenne(l3))
        y4.append(moyenne(l4))
        y5.append(moyenne(l5))
    figure()
    # plot(x,y0)
    plot(x,y1)
    plot(x,y2)
    # plot(x,y3)
    # plot(x,y4)
    # plot(x,y5)
    show()

def ecart_type(L):
    a=moyenne(L)**2
    M=[]
    for i in L: M.append(i**2)
    b=moyenne(M)
    return (b-a)**(1/2)


def etablissement_liste_correlation_n2():
    tc=open(text_correlation,'r')
    cn=open(text_correlation_n2,'w')
    c=tc.read().splitlines()
    m=[[],[],[],[],[],[]]
    p=[]
    for ligne in c:
        l=ligne.split(' ')
        for i in range(6):
            m[i].append(float(l[i]))
    for n in m:
        q=[]
        a,b=moyenne(n),ecart_type(n)
        for fl in n:
            q.append(str((fl-a)/b))
        p.append(q)
    for i in range(len(p[0])):
        cn.write(p[0][i]+' '+p[1][i]+' '+p[2][i]+' '+p[3][i]+' '+p[4][i]+' '+p[5][i]+'\n')
    tc.close()
    cn.close()

def graphe_correlation_2(n):
    cn=open(text_correlation_n2,'r')
    c=cn.readlines()
    cn.close()
    x=list(range(len(c)//n))
    y0,y1,y2,y3,y4,y5=[],[],[],[],[],[]
    for i in range(len(c)//n):
        l0,l1,l2,l3,l4,l5=[],[],[],[],[],[]
        for j in range(n):
            ligne=c[n*i+j]
            l=ligne.split(' ')
            l0.append(float(l[0]))
            l1.append(float(l[1]))
            l2.append(float(l[2]))
            l3.append(float(l[3]))
            l4.append(float(l[4]))
            l5.append(float(l[5]))
        y0.append(moyenne(l0))
        y1.append(moyenne(l1))
        y2.append(moyenne(l2))
        y3.append(moyenne(l3))
        y4.append(moyenne(l4))
        y5.append(moyenne(l5))
    figure()
    #plot(x,y0)
    plot(x,y1,color='blue',label='Bitcoin')
    # plot(x,y2)
    plot(x,y3,color='red',label='Polkadot')
    #plot(x,y4)
    #plot(x,y5)
    xlabel('Jours')
    legend()
    show()

def coefficient_de_correlation(L1,L2):
    e1,e2=ecart_type(L1),ecart_type(L2)
    b=moyenne(L1)*moyenne(L2)
    M=[]
    for i in range(len(L1)):
        M.append(L1[i]*L2[i])
    return (moyenne(M)-b)/(e1*e2)

def liste_coefficients_de_correlation():
    tc=open(text_correlation,'r')
    c=tc.read().splitlines()
    m=[[],[],[],[],[],[]]
    p=[]
    for ligne in c:
        l=ligne.split(' ')
        for i in range(6):
            m[i].append(float(l[i]))
    a=[]
    for i in range(6):
        for j in range(6):
            a.append(coefficient_de_correlation(m[i],m[j]))
    return a

def couleurs():
    figure()
    for i in range(0,6):
        plot([0,1],[i,i])
    show()

def ordre(L): return L[1]

def comparaison_hamming(s): #Retourne la liste des distances de hamming avec la base de données
    lh=open(text_liste_hamming_btc,'r')
    L=[]
    c=lh.read().splitlines()
    for i in range(len(c)-60):
        if i%100000==0:print(i//100000)
        l=c[i]
        L.append((l,hamming_1(s,l),i))
    M=sorted(L,key=ordre)
    N=[]
    for i in range(10):
        N.append(M[i][2])
    return N

def etablissement_liste_hamming_btc():
    lham=open(text_liste_hamming_btc,'w')
    f=open(text_liste_heures_btc_2,'r')
    c=f.readlines()
    for ligne in c:
        s=''
        l=ligne.split(' ')
        for i in range(59):
            a,b=l[i],l[i+1]
            if a<b: s+='2'
            elif a>b: s+='0'
            else: s+='1'
        lham.write(s+'\n')
    f.close()
    lham.close()

def graphe_cours(A,L):
    figure()
    X=list(range(len(L[0])))
    plot(X,A)
    for Y in L:
        plot(X,Y)
    show()

def graphe_hamming(n):
    tch=open(text_liste_hamming_comparaison,'r')
    ch=tch.read().splitlines()
    tc=open(text_liste_octet_2,'r')
    c=tc.read().splitlines()
    th=open(text_liste_octet_1,'r')
    h=th.read().splitlines()
    L=comparaison_hamming(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(60): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        H1=[]
        for i in range(60): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours(A,M)

def etablissement_liste_octet_2():
    lo=open(text_liste_octet_4,'w')
    f=open(text_liste_heures_comparaison,'r')
    c=f.readlines()
    for i in range(len(c)-60):
        ligne=c[i]
        ligne2=c[i+60]
        if i%10000==0: print(i)
        l=ligne.split(' ')[:-1]
        l2=ligne2.split(' ')[:-1]
        m,s=[],''
        for x in l: m.append(float(x))
        a,b=min(m),max(m)
        for x in l2: m.append(float(x))
        for fl in m:
            if a==b: d=0
            else: d=int(255*(fl-a)/(b-a))
            s+=str(d)+' '
        lo.write(s+'\n')
    f.close()
    lo.close()

def graphe_cours_2(A,L):
    figure()
    X1=list(range(60))
    X2=list(range(59,120))
    A1,A2=[],[A[59]]
    for i in range(60):
        A1.append(A[i])
        A2.append(A[i+60])
    plot(X1,A1,color='blue',label='Cours évalué')
    plot(X2,A2,color='red',label='Évolution réelle')
    B=len(X2)*[A[59]]
    if len(L)!=0:
        Y=L[0]
        Y1,Y2=[],[Y[59]]
        for i in range(60):
            Y1.append(Y[i])
            Y2.append(Y[60+i])
        plot(X1,Y1,color='0.4',label='Prédiction')
        plot(X2,Y2,color='0.4')
    #     for i in range(1,len(L)):
    #         Y=L[i]
    #         Y1,Y2=[],[Y[59]]
    #         for i in range(60):
    #             Y1.append(Y[i])
    #             Y2.append(Y[60+i])
    #         plot(X1,Y1,color='0.7')
    #         plot(X2,Y2,color='0.7')
    plot(X1,A1,color='blue')
    plot(X2,A2,color='red')
    plot(X2,B,linestyle='dashed',color='black')
    legend()
    show()

def graphe_hamming_2(n):
    tch=open(text_liste_hamming_comparaison,'r')
    ch=tch.read().splitlines()
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    L=comparaison_hamming(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(120): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        H1=[]
        for i in range(120): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours_2(A,M)

def performance_hamming(n):
    tch=open(text_liste_hamming_comparaison,'r')
    ch=tch.read().splitlines()
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    L=comparaison_hamming(ch[n])
    p=0
    CN=c[n].split(' ')
    a=int(CN[59])<int(CN[119])
    print(int(CN[59]),int(CN[119]))
    for i in L:
        H=h[i].split(' ')
        b=int(H[59])<int(H[119])
        print(int(H[59]),int(H[119]))
        if a==b: p+=1
    return p

def performance_hamming_complet():
    tch=open(text_liste_hamming_comparaison,'r')
    ch=tch.read().splitlines()
    tc=open(text_liste_octet_4,'r')
    co=tc.read().splitlines()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    lh=open(text_liste_hamming_btc,'r')
    c=lh.read().splitlines()
    for n in range(192,len(ch)):
        ph=open(text_performance_hamming,'r')
        PH=ph.read()
        ph.close()
        L=[]
        for i in range(len(c)-60):
            l=c[i]
            L.append((l,hamming_1(ch[n],l),i))
        M=sorted(L,key=ordre)
        N=[]
        for i in range(10):
            N.append(M[i][2])
        p=0
        CN=co[n].split(' ')
        a=int(CN[59])<int(CN[119])
        if a:
            te='H'
        else:
            te='B'
        for i in N:
            H=h[i].split(' ')
            b=int(H[59])<int(H[119])
            if a==b: p+=1
        print(n,te,p)
        ph=open(text_performance_hamming,'w')
        ph.write(PH+te+' '+str(p)+'\n')
        ph.close()

def comparaison_octet(s):
    lh=open(text_liste_octet_1,'r')
    L=[]
    c=lh.read().splitlines()
    for i in range(len(c)-60):
        if i%100000==0:print(i//100000)
        l=c[i]
        L.append((l,distance_octet(s,l),i))
    M=sorted(L,key=ordre)
    N=[]
    for i in range(10):
        N.append(M[i][2])
    return N

def distance_octet(l,m):
    L=l.split(' ')[:-1]
    M=m.split(' ')[:-1]
    d=0
    for i in range(len(L)):
        d+=abs(int(L[i])-int(M[i]))
    return d

def graphe_octet(n):
    tch=open(text_liste_octet_2,'r')
    ch=tch.read().splitlines()
    tch.close
    tc=open(text_liste_octet_2,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet_1,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(60): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        H1=[]
        for i in range(60): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours(A,M)

def graphe_octet_2(n):
    tch=open(text_liste_octet_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(120): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        print(H)
        H1=[]
        for i in range(120): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours_2(A,M)

def performance_octet(n):
    tch=open(text_liste_octet_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet(ch[n])
    p=0
    CN=c[n].split(' ')
    a=int(CN[59])<int(CN[119])
    print(int(CN[59]),int(CN[119]))
    for i in L:
        H=h[i].split(' ')
        b=int(H[59])<int(H[119])
        print(int(H[59]),int(H[119]))
        if a==b: p+=1
    return p

def performance_octet_complet():
    tch=open(text_liste_octet_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet_4,'r')
    co=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet_3,'r')
    h=th.read().splitlines()
    th.close()
    lh=open(text_liste_octet_1,'r')
    c=lh.read().splitlines()
    lh.close()
    for n in range(149,len(ch)):
        ph=open(text_performance_octet,'r')
        PH=ph.read()
        ph.close()
        L=[]
        for i in range(len(c)-60):
            l=c[i]
            L.append((l,distance_octet(ch[n],l),i))
        M=sorted(L,key=ordre)
        N=[]
        for i in range(10):
            N.append(M[i][2])
        p=0
        CN=co[n].split(' ')
        a=int(CN[59])<int(CN[119])
        if a:
            te='H'
        else:
            te='B'
        for i in N:
            H=h[i].split(' ')
            b=int(H[59])<int(H[119])
            if a==b: p+=1
        print(n,te,p)
        ph=open(text_performance_octet,'w')
        ph.write(PH+te+' '+str(p)+'\n')
        ph.close()

def stats():
    tc=open(text_liste_octet_3,'r')
    c=tc.read().splitlines()
    tc.close()
    c1,c2=0,0
    for ligne in c:
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        if a1>a2:
            c1+=1
            if a2>a3:
                c2+=1
    return c1,c2

def stats_2():
    tc=open(text_liste_octet_3,'r')
    c=tc.read().splitlines()
    tc.close()
    c1,c2=0,0
    for ligne in c:
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        if a1<a2:
            c1+=1
            c2+=(a3-a2)/(a2-a1)
    return c1,c2

def stats_3():
    tc=open(text_liste_octet_3,'r')
    c=tc.read().splitlines()
    tc.close()
    C=[]
    for i in range(60):C.append([0,0])
    for ligne in c:
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        k=[]
        for i in range(60):
            k.append(int(l[i]))
        m=min(k)
        if a1>a2:
            pos=k.index(m)
            C[pos][0]+=1
            if a2<a3:
                C[pos][1]+=1
    return C

def graphe_stats_3():
    C=stats_3()
    X=list(range(5,60))
    Y=[]
    for i in range(5,60):
        Y.append(C[i][1]/C[i][0])
    figure()
    Z=55*[0.5]
    plot(X,Y,color='blue')
    plot(X,Z,color='black')
    show()

def etude_resultats_hamming():
    ph=open(text_performance_hamming)
    PH=ph.read().splitlines()
    ph.close()
    d,v,f=0,0,0
    L=[]
    for ligne in PH:
        l=ligne.split(' ')
        r=int(l[1])
        d+=r
        if r>5: v+=2
        elif r<5: f+=2
        else:
            v+=1
            f+=1
        L.append((l[0],r))
    return d,len(L),d/len(L),v,f

def etude_resultats_octet():
    ph=open(text_performance_octet)
    PH=ph.read().splitlines()
    ph.close()
    d,v,f=0,0,0
    L=[]
    for ligne in PH:
        l=ligne.split(' ')
        r=int(l[1])
        d+=r
        if r>5: v+=2
        elif r<5: f+=2
        else:
            v+=1
            f+=1
        L.append((l[0],r))
    return d,len(L),d/len(L),v,f

def etablissement_liste_octet_3():
    lo=open(text_liste_octet2_1,'w')
    f=open(text_liste_heures_btc_2,'r')
    c=f.readlines()
    for i in range(len(c)):
        ligne=c[i]
        if i%10000==0: print(i)
        l=ligne.split(' ')[:-1]
        m,s=[],''
        for x in l: m.append(float(x))
        a,b=min(m),max(m)
        for i in range(6):
            e=0
            if a==b: d=0
            else:
                for j in range(10):
                    fl=m[10*i+j]
                    e+=int(255*(fl-a)/(b-a))
                d=e//10
            s+=str(d)+' '
        lo.write(s+'\n')
    f.close()
    lo.close()

def etablissement_liste_octet_4():
    lo=open(text_liste_octet2_3,'w')
    f=open(text_liste_heures_btc_2,'r')
    c=f.readlines()
    for i in range(len(c)-60):
        ligne=c[i]
        ligne2=c[i+60]
        if i%10000==0: print(i)
        l=ligne.split(' ')[:-1]
        l2=ligne2.split(' ')[:-1]
        m,s=[],''
        for x in l: m.append(float(x))
        a,b=min(m),max(m)
        for x in l2: m.append(float(x))
        for i in range(12):
            e=0
            if a==b: d=0
            else:
                for j in range(10):
                    fl=m[10*i+j]
                    e+=int(255*(fl-a)/(b-a))
                d=e//10
            s+=str(d)+' '
        lo.write(s+'\n')
    f.close()
    lo.close()

def comparaison_octet2(s):
    lh=open(text_liste_octet2_1,'r')
    L=[]
    c=lh.read().splitlines()
    for i in range(len(c)-60):
        if i%100000==0:print(i//100000)
        l=c[i]
        L.append((l,distance_octet(s,l),i))
    M=sorted(L,key=ordre)
    N=[]
    for i in range(10):
        N.append(M[i][2])
    return N

def graphe_octet2(n):
    tch=open(text_liste_octet2_2,'r')
    ch=tch.read().splitlines()
    tch.close
    tc=open(text_liste_octet2_2,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet2_1,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet2(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(6): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        H1=[]
        for i in range(6): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours(A,M)

def graphe_octet2_2(n):
    tch=open(text_liste_octet2_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet2_4,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet2_3,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet2(ch[n])
    M=[]
    CN=c[n].split(' ')
    A=[]
    for i in range(12): A.append(int(CN[i]))
    for i in L:
        H=h[i].split(' ')
        H1=[]
        for i in range(12): H1.append(int(H[i]))
        M.append(H1)
    graphe_cours_2(A,M)

def performance_octet2(n):
    tch=open(text_liste_octet2_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet2_4,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet2_3,'r')
    h=th.read().splitlines()
    th.close()
    L=comparaison_octet2(ch[n])
    p=0
    CN=c[n].split(' ')
    a=int(CN[5])<int(CN[11])
    print(int(CN[5]),int(CN[11]))
    for i in L:
        H=h[i].split(' ')
        b=int(H[5])<int(H[11])
        print(int(H[5]),int(H[11]))
        if a==b: p+=1
    return p

def performance_octet2_complet():
    tch=open(text_liste_octet2_2,'r')
    ch=tch.read().splitlines()
    tch.close()
    tc=open(text_liste_octet2_4,'r')
    co=tc.read().splitlines()
    tc.close()
    th=open(text_liste_octet2_3,'r')
    h=th.read().splitlines()
    th.close()
    lh=open(text_liste_octet2_1,'r')
    c=lh.read().splitlines()
    lh.close()
    for n in range(1000):
        ph=open(text_performance_octet2,'r')
        PH=ph.read()
        ph.close()
        L=[]
        for i in range(len(c)-60):
            l=c[i]
            L.append((l,distance_octet(ch[n],l),i))
        M=sorted(L,key=ordre)
        N=[]
        for i in range(10):
            N.append(M[i][2])
        p=0
        CN=co[n].split(' ')
        a=int(CN[5])<int(CN[11])
        if a:
            te='H'
        else:
            te='B'
        for i in N:
            H=h[i].split(' ')
            b=int(H[5])<int(H[11])
            if a==b: p+=1
        print(n,te,p)
        ph=open(text_performance_octet2,'w')
        ph.write(PH+te+' '+str(p)+'\n')
        ph.close()

def etude_resultats_octet2():
    ph=open(text_performance_octet2)
    PH=ph.read().splitlines()
    ph.close()
    d,v,f=0,0,0
    L=[]
    for ligne in PH:
        l=ligne.split(' ')
        r=int(l[1])
        d+=r
        if r>5: v+=2
        elif r<5: f+=2
        else:
            v+=1
            f+=1
        L.append((l[0],r))
    return d,len(L),d/len(L),v,f

def stats_3_h():
    tc=open(text_liste_octet_3,'r')
    c=tc.read().splitlines()
    tc.close()
    C=[]
    for i in range(60):C.append([0,0])
    for ligne in c:
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        k=[]
        for i in range(60):
            k.append(int(l[i]))
        m=max(k)
        if a1<a2:
            pos=k.index(m)
            C[pos][0]+=1
            if a2<a3:
                C[pos][1]+=1
    return C

def stats_3_b():
    tc=open(text_liste_octet_3,'r')
    c=tc.read().splitlines()
    tc.close()
    C=[]
    for i in range(60):C.append([0,0])
    for ligne in c:
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        k=[]
        for i in range(60):
            k.append(int(l[i]))
        m=min(k)
        if a1>a2:
            pos=k.index(m)
            C[pos][0]+=1
            if a2<a3:
                C[pos][1]+=1
    return C

def comparaison_extremum():
    Ch=[[0, 0], [1294, 614], [1937, 947], [2451, 1187], [2913, 1434], [3323, 1671], [3712, 1854], [3913, 1931], [4148, 2082], [4374, 2174], [4520, 2201], [4875, 2385], [5035, 2459], [5241, 2556], [5364, 2642], [5556, 2765], [5759, 2824], [5947, 2949], [6166, 3090], [6377, 3190], [6563, 3288], [6784, 3394], [7027, 3504], [7188, 3571], [7429, 3617], [7548, 3686], [7805, 3842], [8007, 3955], [8139, 4027], [8298, 4103], [8448, 4183], [8642, 4312], [8794, 4403], [9032, 4519], [9183, 4596], [9449, 4753], [9765, 4861], [10009, 4984], [10296, 5146], [10547, 5261], [10945, 5487], [11323, 5606], [11709, 5819], [12071, 5959], [12527, 6079], [12981, 6305], [13479, 6530], [14023, 6821], [14619, 7049], [15360, 7485], [16134, 7832], [17082, 8183], [18042, 8615], [19255, 9142], [20662, 9768], [22496, 10537], [25165, 11667], [29317, 13401], [37708, 16965], [71612, 31543]]
    Cb=[[0, 0], [1210, 683], [1915, 1038], [2500, 1346], [2933, 1552], [3317, 1728], [3587, 1857], [3903, 2033], [4117, 2156], [4334, 2282], [4432, 2358], [4659, 2438], [4839, 2553], [5054, 2645], [5275, 2763], [5438, 2878], [5629, 2962], [5815, 3020], [6110, 3143], [6274, 3269], [6417, 3330], [6634, 3443], [6856, 3566], [6968, 3607], [7167, 3744], [7336, 3859], [7529, 3932], [7700, 3993], [7845, 4096], [8021, 4154], [8156, 4222], [8339, 4286], [8479, 4385], [8656, 4470], [8895, 4546], [9134, 4667], [9399, 4833], [9668, 5007], [9962, 5175], [10241, 5295], [10453, 5362], [10871, 5595], [11197, 5820], [11599, 6078], [11986, 6334], [12463, 6611], [13006, 6906], [13611, 7200], [14220, 7598], [14903, 7974], [15650, 8316], [16501, 8745], [17502, 9341], [18727, 9996], [20250, 10914], [22062, 12019], [24677, 13594], [28862, 15927], [36617, 20645], [65563, 37980]]
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    tc.close()
    d,v,f=0,0,0
    for ligne in c:
        d+=1
        l=ligne.split(' ')
        a1,a2,a3=int(l[0]),int(l[59]),int(l[119])
        if a1<=a2:
            k=[]
            for i in range(60):
                k.append(int(l[i]))
            m=max(k)
            pos=k.index(m)
            b1=Ch[pos][1]>0.5*Ch[pos][0]
            b2=a2<=a3
        else:
            k=[]
            for i in range(60):
                k.append(int(l[i]))
            m=min(k)
            pos=k.index(m)
            b1=Cb[pos][1]>0.5*Cb[pos][0]
            b2=a2<a3
        if b1==b2:
            v+=1
        else: f+=1
        if d%1000==0:
            print(d,v,f)
            # ph=open(text_performance_extremum,'r')
            # PH=ph.read()
            # ph.close()
            # ph=open(text_performance_extremum,'w')
            # ph.write(PH+str(d)+' '+str(v)+' '+str(f)+' '+'\n')
            # ph.close()
    print(d,v,f)
    # ph=open(text_performance_extremum,'r')
    # PH=ph.read()
    # ph.close()
    # ph=open(text_performance_extremum,'w')
    # ph.write(PH+str(d)+' '+str(v)+' '+str(f)+' '+'\n')
    # ph.close()

def comparaison_extremum_rentabilite():
    Ch=[[0, 0], [1294, 614], [1937, 947], [2451, 1187], [2913, 1434], [3323, 1671], [3712, 1854], [3913, 1931], [4148, 2082], [4374, 2174], [4520, 2201], [4875, 2385], [5035, 2459], [5241, 2556], [5364, 2642], [5556, 2765], [5759, 2824], [5947, 2949], [6166, 3090], [6377, 3190], [6563, 3288], [6784, 3394], [7027, 3504], [7188, 3571], [7429, 3617], [7548, 3686], [7805, 3842], [8007, 3955], [8139, 4027], [8298, 4103], [8448, 4183], [8642, 4312], [8794, 4403], [9032, 4519], [9183, 4596], [9449, 4753], [9765, 4861], [10009, 4984], [10296, 5146], [10547, 5261], [10945, 5487], [11323, 5606], [11709, 5819], [12071, 5959], [12527, 6079], [12981, 6305], [13479, 6530], [14023, 6821], [14619, 7049], [15360, 7485], [16134, 7832], [17082, 8183], [18042, 8615], [19255, 9142], [20662, 9768], [22496, 10537], [25165, 11667], [29317, 13401], [37708, 16965], [71612, 31543]]
    Cb=[[0, 0], [1210, 683], [1915, 1038], [2500, 1346], [2933, 1552], [3317, 1728], [3587, 1857], [3903, 2033], [4117, 2156], [4334, 2282], [4432, 2358], [4659, 2438], [4839, 2553], [5054, 2645], [5275, 2763], [5438, 2878], [5629, 2962], [5815, 3020], [6110, 3143], [6274, 3269], [6417, 3330], [6634, 3443], [6856, 3566], [6968, 3607], [7167, 3744], [7336, 3859], [7529, 3932], [7700, 3993], [7845, 4096], [8021, 4154], [8156, 4222], [8339, 4286], [8479, 4385], [8656, 4470], [8895, 4546], [9134, 4667], [9399, 4833], [9668, 5007], [9962, 5175], [10241, 5295], [10453, 5362], [10871, 5595], [11197, 5820], [11599, 6078], [11986, 6334], [12463, 6611], [13006, 6906], [13611, 7200], [14220, 7598], [14903, 7974], [15650, 8316], [16501, 8745], [17502, 9341], [18727, 9996], [20250, 10914], [22062, 12019], [24677, 13594], [28862, 15927], [36617, 20645], [65563, 37980]]
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    tc.close()
    th=open(text_liste_heures_comparaison,'r')
    h=th.read().splitlines()
    th.close()
    d,r,s=0,0,1
    for ligne in c:
        if d%60==0:
            lh1=h[d].split(' ')
            lh2=h[d+60].split(' ')
            l=ligne.split(' ')
            a1,a2,a3,a4,a5=int(l[0]),int(l[59]),int(l[119]),float(lh1[59]),float(lh2[59])
            if a1<=a2:
                k=[]
                for i in range(60):
                    k.append(int(l[i]))
                m=max(k)
                pos=k.index(m)
                b1=Ch[pos][1]>0.5*Ch[pos][0]
                if b1:
                    r+=(a5-a4)/a4
                    s*=a5/a4
                else:
                    r+=(a4-a5)/a4
                    s*=1+(a4-a5)/a4
            else:
                k=[]
                for i in range(60):
                    k.append(int(l[i]))
                m=min(k)
                pos=k.index(m)
                b1=Cb[pos][1]>0.5*Cb[pos][0]
                if b1:
                    r+=(a5-a4)/a4
                    s*=a5/a4
                else:
                    r+=(a4-a5)/a4
                    s*=1+(a4-a5)/a4
            print(d,r,s)
            ph=open(text_performance_extremum_rentabilite,'r')
            PH=ph.read()
            ph.close()
            ph=open(text_performance_extremum_rentabilite,'w')
            ph.write(PH+str(d)+' '+str(r)+' '+str(s)+' '+'\n')
            ph.close()
        d+=1

def graphe_rentabilite():
    tr=open(text_performance_extremum_rentabilite,'r')
    r=tr.read().splitlines()
    tr.close()
    tb=open(text_valeurs_comparaison,'r')
    b=tb.read().splitlines()
    tb.close()
    ini=float(b[0])
    X,Y,Z,W=[],[],[],[]
    for ligne in r:
        l=ligne.split(' ')
        X.append(int(l[0]))
        Y.append(float(l[2]))
        Z.append(1)
    for i in range(len(b)//60-1):
        W.append(float(b[60*i])/ini)
    figure()
    plot(X,W,color='red',linewidth=0.7,label='Cours du Bitcoin')
    plot(X,Y,color='blue',label='Valeur du capital investi',linewidth=0.7)
    plot(X,Z,color='black',linestyle='dotted', linewidth=2)
    ylabel("Valeur de l'actif")
    legend()
    show()

def graphe_bitcoin():
    tb=open(text_valeurs_comparaison,'r')
    b=tb.read().splitlines()
    tb.close()
    X,Y=[],[]
    for i in range(len(b)):
        X.append(i)
        Y.append(float(b[i]))
    figure()
    plot(X,Y)
    show()

def graphe_rentabilite_2():
    tr=open(text_performance_extremum_rentabilite,'r')
    r=tr.read().splitlines()
    tr.close()
    X,Y=[],[]
    for ligne in r:
        l=ligne.split(' ')
        y=int(l[0])
        if y==0:
            X.append(0)
            Y.append(0)
        else:
            X.append(int(l[0]))
            Y.append(exp(525600*log(float(l[2]))/y)-1)
    figure()
    plot(X[400:],Y[400:],color='black')
    show()

def calcul_rentabilite():
    tr=open(text_performance_extremum_rentabilite,'r')
    r=tr.read().splitlines()
    tr.close()
    X,Y,s=[],[],0
    for ligne in r:
        l=ligne.split(' ')
        y=int(l[0])
        s+=y
        if y==0:
            X.append(0)
            Y.append(0)
        else:
            X.append(int(l[0]))
            Y.append(y*(exp(525600*log(float(l[2]))/y)-1))
    return moyenne(Y)/190740

def graphe_liste_heure(n):
    tb=open(text_liste_heures_btc_2,'r')
    b=tb.read().splitlines()
    tb.close()
    X=list(range(60))
    Y=[]
    l=b[n].split(' ')
    for i in range(60):
        Y.append(float(l[i]))
    figure()
    plot(X,Y,label='Cours du Bitcoin (en $)')
    plot(X,Y,label='Liste échantillonnée',marker='o',color='red',linestyle='none')
    legend()
    show()

def performance_extremum():
    tp=open(text_performance_extremum,'r')
    p=tp.read().splitlines()
    tp.close
    for ligne in p:
        l=ligne.split(' ')
        a,b=int(l[0]),int(l[1])
        print(a,b/a)

def graphe_extremum(n):
    tc=open(text_liste_octet_4,'r')
    c=tc.read().splitlines()
    tc.close()
    l=c[n].split(' ')
    A=[]
    for i in range(120):
        A.append(int(l[i]))
    graphe_cours_2(A,[])