from math import pow

def funMath(maxLoop):
    for i in range(0,maxLoop,1):
        pers1=(str(1)+str(6) *i)
        pers2=(str(5)+str(0)*i)
        pers3= (str(3)*(i+1))
        result= int(pow(int(pers1),3))+int(pow(int(pers2),3))+ int(pow(int(pers3),3))
        print(f'{i+1}. {pers1}+{pers2}+{pers3}={result}')
