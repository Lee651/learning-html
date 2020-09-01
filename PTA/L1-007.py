N = input("")

n = int(N)
t = []
dic = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu'}
a = ""
count = 0
if n >= 0:
    for i in range(1, len(N)+1):
        t_i = int(n / (10 ** (len(N) - i)) % 10)
        t.append(t_i)

    for z in t:
        count += 1
        for x, y in dic.items():
            if int(x) == z:
                if count < len(t):
                    a += (y + " ")
                else:
                    a += y
            else:
                pass
    print(a)
            
else:
    for i in range(1, len(N)):
        t_i = int(-n / (10 ** (len(N) -1 - i)) % 10)
        t.append(t_i)

    for z in t:
        count += 1
        for x, y in dic.items():
            if int(x) == z:
                if count < len(t):
                    a += (y + " ")
                else:
                    a += y
            else:
                pass
    print("fu" + " " + a)