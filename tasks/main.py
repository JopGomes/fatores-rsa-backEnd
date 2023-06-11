from geradorPrimos import Primos
from database.db import BancoDados

primo = Primos(100)
listaPrimos = primo.getPrimos()

banco = BancoDados()

banco.apagarTuplas()

for i in range(0,len(listaPrimos)):
    for j in range(i+1,len(listaPrimos)):
        banco.inserirNumero(listaPrimos[i],listaPrimos[j])
