
validas2=["R$ 1,00", "R$ 2,00","R$ 5,00","R$ 10,00","R$ 20,00","R$ 50,00"]

validas=[1,2,5,10,20,50,100]

quantidade_notas=[100,50,40,30,10,5]

def checar_nota(nota,validas):
        if nota in validas:
            return nota
    
def troco_valido(qtd,qtd_dispo):
    x=len(qtd)
    for i in range (6):
        if (qtd_dispo[i]-qtd[i]) < 0:
            return False        
    return True
    


def calcular_notas(troco):
    a=[0,0,0,0,0,0]
    a[5]=troco//50
    a[4]=(troco-50*a[5])//20
    a[3]=(troco-50*a[5]-20*a[4])//10
    a[2]=(troco-50*a[5]-20*a[4]-10*a[3])//5
    a[1]=(troco-50*a[5]-20*a[4]-10*a[3]-5*a[2])//2
    a[0]=(troco-50*a[5]-20*a[4]-10*a[3]-5*a[2]-2*a[1])
    return a
    
    



  
