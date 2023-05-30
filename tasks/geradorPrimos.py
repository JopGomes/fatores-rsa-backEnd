
class Primos:
    def __init__(self, n):
        self.listaPrimos = []
        listaCompleta = []

        for i in range(0,n+1):
            listaCompleta.append(True)
        
        for i in range(2,n+1):
            if listaCompleta[i] == True:
                self.listaPrimos.append(i)
            for j in range(i+1,n+1):
                if j%i == 0:
                    listaCompleta[j] = False
                
    def getPrimos(self):
        return self.listaPrimos