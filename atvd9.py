# Um motorista deseja calcular o consumo médio de combustível do seu carro. Crie um programa que receba a quantidade de quilômetros percorridos e a quantidade de litros de combustível consumidos, e calcule o consumo médio (km por litro).
km = int(input("Quantos quilômetros foram percorridos? "))
litro = int(input("Quantos litros foram consumidos nesta viagem? "))
consumoMedio = km / litro

print (f"o consumo médio foram de {consumoMedio}km/L.")