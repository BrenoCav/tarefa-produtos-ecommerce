def calcular_custo_viagem():
    print("\n🌟 PLANEJADOR DE VIAGEM 🌟")
    print("----------------------------")
    
    # Dados da viagem
    destino = input("Local de destino: ").strip().title()
    distancia = float(input("Distância (Km): "))
    consumo = float(input("Consumo do carro (Km/l): "))
    preco_combustivel = float(input("Preço do combustível (R$/litro): "))
    
    # Cálculos
    litros_necessarios = distancia / consumo
    custo_total = litros_necessarios * preco_combustivel
    
    # Exibe relatório completo
    print("\n📊 RESUMO DA VIAGEM")
    print("----------------------------")
    print(f"Destino: {destino}")
    print(f"Distância: {distancia} Km")
    print(f"Consumo: {consumo} Km/l")
    print(f"Preço do combustível: R$ {preco_combustivel:.2f}")
    print("----------------------------")
    print(f"💵 CUSTO TOTAL: R$ {custo_total:.2f}")
    print("----------------------------")
    
    # Salva em arquivo (opcional)
    with open(f"viagem_{destino.replace(' ', '_')}.txt", "w") as file:
        file.write(f"Destino: {destino}\nCusto: R$ {custo_total:.2f}")

if __name__ == "__main__":
    calcular_custo_viagem()