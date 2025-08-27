# inventario.py
# Controle de Inventário Básico

def main():
    inventario = []  # Lista de dicionários
    
    while True:
        print("\n" + "="*40)
        print("      CONTROLE DE INVENTÁRIO")
        print("="*40)
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Listar inventário")
        print("4. Sair")
        print("="*40)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            adicionar_item(inventario)
        elif opcao == "2":
            remover_item(inventario)
        elif opcao == "3":
            listar_inventario(inventario)
        elif opcao == "4":
            print("Saindo do sistema... Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

def adicionar_item(inventario):
    print("\n--- ADICIONAR ITEM ---")
    nome = input("Nome do item: ").strip()
    
    # Verifica se o item já existe
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            print("⚠️ Item já existe! Use a opção de edição ou remova primeiro.")
            return
    
    try:
        quantidade = int(input("Quantidade: "))
        if quantidade < 0:
            print(" Quantidade não pode ser negativa!")
            return
    except ValueError:
        print("Digite um número válido!")
        return
    
    inventario.append({"nome": nome, "quantidade": quantidade})
    print(f"✅ Item '{nome}' adicionado com sucesso!")

def remover_item(inventario):
    print("\n--- REMOVER ITEM ---")
    if not inventario:
        print("Inventário vazio! Nada para remover.")
        return
    
    nome = input("Nome do item a remover: ").strip()
    
    for item in inventario:
        if item["nome"].lower() == nome.lower():
            inventario.remove(item)
            print(f"✅ Item '{nome}' removido com sucesso!")
            return
    
    print("❌ Item não encontrado no inventário!")

def listar_inventario(inventario):
    print("\n--- INVENTÁRIO ATUAL ---")
    
    if not inventario:
        print("📦 Inventário vazio!")
        return
    
    print(f"{'Nº':<4} {'ITEM':<20} {'QUANTIDADE':<10}")
    print("-" * 35)
    
    for i, item in enumerate(inventario, 1):
        print(f"{i:<4} {item['nome']:<20} {item['quantidade']:<10}")

if __name__ == "__main__":
    main()