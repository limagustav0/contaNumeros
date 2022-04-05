

def contaNumeros(numero,tamanho):
    cont = 0
    for x in range(tamanho+1):
        x = str(x)
        for i in range (len(x)):
            if x[i] == str(numero):
                cont +=1
    print(cont)

if __name__ == "__main__":
    contaNumeros(3,100)



