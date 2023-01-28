distancia = float (input('qual a é a distancia da sua viagem?'))
print ('voce esta prestes a começar uma viagem de {}'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print ('e o preço da sua passagem será de R${:.2f}'.format(distancia))