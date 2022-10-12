key = [1,2,3,5,7,11,13,17,19,23,29,31,37,41,47,53,59,61,67,71,73,79,83,97,101,103,107,109,113,127,131,137,149,151,157,163,167,173,179,181,191,197,199,211,223,227,229,233,239,241,257,263,269,271,277,281,283,293,307,313,317,331,337,347,349,353,359,367,379,383,389,397,401,409,419,421,431,439,443,449,457,461,463,467,479,487,499,503,509,521,523,541,547,557,563,571,577,587,593,599,45989,61861,58109,40459,53101,45817,36973,49207,41959,57901,47501,50867,49559,47381,42467,48017,54841,60899,35149,51361,53653,58679,34763,64109]
alf =list('абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

p = 0
g = 0
c1 = 0
d1 = 0
c2 = 0

p_true = False
g_true = False
c1_true = False
c2_true = False

def Code():

    while True:
        p = int(input('Введите простое число P: '))
        g = int(input('Введите  простое число G (1 < G < P-1) : '))
        c1 = int(input('Введите секретный ключ C1 (1 < C1 < P-1) : '))
        c2 = int(input('Введите секретный ключ C2 (1 < C1 < P-1) : '))


        for i in key:
             if(p == i):
                p_true = True
        for j in key:
            if(g<p-1 and g==j):
                g_true = True
        if(c1 < p-1 and c1 != g):
            c1_true = True
        if(c2 < p-1 and c2 != c1):
            c2_true = True
        if(p_true == True and g_true == True and c1_true == True and c2_true == True):
            break
    d1 = g**c2 % p
    print('Открытый ключ: ',d1)

    sum = 0
    message = input('Введите сообщение: ')
    for sym in message:
        for i in alf:
            if (sym == i):
                sum=sum+alf.index(i)
                sum = sum+1
    print('Сумма символов равна: ',sum)
    e = sum*(d1**c1) % p
    print('Результат кодирования значения цифровой подписи равен: ',e)

def Decode():

    while True:
        p = int(input('Введите простое число P: '))
        c2 = int(input('Введите секретный ключ C1 (1 < C1 < P-1) : '))
        d1 = int(input('Введите открытый ключ D1 : '))
        e = int(input('Введите электронный цифровой ключ: '))


        for i in key:
             if(p == i):
                p_true = True
             if(c2<p-1 and c2!=d1):
                c2_true = True
       
        if(p_true == True and c2_true == True):
            break
      
    message = e*d1**(p-1-c2) % p
    print('Результат декодирования значения цифровой подписи равен: ',message)


change = input('Кодирование / Декодирование :')
if (change == 'K'or change =='k'or change =='К' or change =='к'):
    Code()
    
if (change == 'D'or change =='d'or change =='Д'or change =='д'):
    Decode()
   