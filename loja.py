# loja.py - Sistema de E-commerce com Produtos Físicos e Digitais
from abc import ABC, abstractmethod

class Produto(ABC):
    """Classe abstrata base para todos os produtos"""
    
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base
    
    @abstractmethod
    def calcular_preco_final(self):
        """Método abstrato - deve ser implementado pelas subclasses"""
        pass


class ProdutoFisico(Produto):
    """Classe para produtos físicos (com frete)"""
    
    def __init__(self, nome, preco_base, custo_frete):
        super().__init__(nome, preco_base)
        self.custo_frete = custo_frete
    
    def calcular_preco_final(self):
        """Calcula preço final incluindo custo do frete"""
        return self.preco_base + self.custo_frete


class ProdutoDigital(Produto):
    """Classe para produtos digitais (com taxa de serviço)"""
    
    def __init__(self, nome, preco_base, taxa_servico):
        super().__init__(nome, preco_base)
        self.taxa_servico = taxa_servico
    
    def calcular_preco_final(self):
        """Calcula preço final incluindo taxa de serviço"""
        return self.preco_base + self.taxa_servico


# ÁREA DE TESTES - Simulando carrinho de compras
if __name__ == "__main__":
    print("=" * 50)
    print("           LOJA VIRTUAL - CARRINHO")
    print("=" * 50)
    
    # Criando produtos para o carrinho
    carrinho = [
        ProdutoFisico("Livro Python Avançado", 89.90, 15.50),
        ProdutoFisico("Caneca Programador", 25.00, 8.00),
        ProdutoDigital("E-book Django", 45.00, 2.50),
        ProdutoDigital("Curso Online Flask", 120.00, 5.00),
        ProdutoFisico("Mouse Gamer", 150.00, 12.00),
        ProdutoDigital("Assinatura Premium", 29.90, 1.50)
    ]
    
    # Calculando totais
    total_compra = 0
    
    print("\n ITENS NO CARRINHO:")
    print("-" * 40)
    
    # Usando polimorfismo - mesmo método para tipos diferentes
    for i, produto in enumerate(carrinho, 1):
        preco_final = produto.calcular_preco_final()
        total_compra += preco_final
        
        # Identificando tipo do produto
        tipo = "Físico" if isinstance(produto, ProdutoFisico) else "Digital"
        
        print(f"{i}. {produto.nome}")
        print(f"   Tipo: {tipo}")
        print(f"   Preço base: R$ {produto.preco_base:.2f}")
        
        if isinstance(produto, ProdutoFisico):
            print(f"   Frete: R$ {produto.custo_frete:.2f}")
        else:
            print(f"   Taxa: R$ {produto.taxa_servico:.2f}")
            
        print(f"   Preço final: R$ {preco_final:.2f}")
        print()
    
    print("-" * 40)
    print(f" TOTAL DA COMPRA: R$ {total_compra:.2f}")
    print("=" * 50)