class MembroUEPA:

    
    def __init__(self, nome, matricula, email):
        self.nome = nome
        self.matricula = matricula
        self.email = email
    
    def apresentar(self):
        
        return f"Olá, sou {self.nome}, membro da UEPA."


class Aluno(MembroUEPA):
    
    
    def __init__(self, nome, matricula, email, curso):
        # Usando super() para herdar atributos da classe pai
        super().__init__(nome, matricula, email)
        self.curso = curso
    
    def verificar_notas(self):
       
        return f"{self.nome} está verificando suas notas no sistema."
    
    def apresentar(self):
    
        return f"Olá, sou {self.nome}, aluno do curso de {self.curso} na UEPA. Matrícula: {self.matricula}"


class Professor(MembroUEPA):

    
    def __init__(self, nome, matricula, email, departamento):
        # Usando super() para herdar atributos da classe pai
        super().__init__(nome, matricula, email)
        self.departamento = departamento
    
    def lancar_frequencia(self):
        """Método específico para professores lançarem frequência"""
        return f"Professor {self.nome} está lançando a frequência dos alunos."
    
    def apresentar(self):
        """Sobrescrevendo o método apresentar() para Professor"""
        return f"Olá, sou {self.nome}, professor do departamento de {self.departamento} na UEPA. Email: {self.email}"


# ÁREA DE TESTES - Demonstrando o funcionamento das classes
if __name__ == "__main__":
    print("=" * 50)
    print("      SISTEMA UEPA DIGITAL - DEMONSTRAÇÃO")
    print("=" * 50)
    
    # Criando instância de Aluno
    aluno1 = Aluno(
        nome="Maria Alice",
        matricula="2025A001",
        email="maria.alive@uepa.br",
        curso="Bacharel em Tecnologia da Informação"
    )
    
    # Criando instância de Professor
    professor1 = Professor(
        nome="Dr. Breno Cavalcante",
        matricula="PROF2025001",
        email="breno.cavalcante@uepa.br",
        departamento="Ciência da Computação"
    )
    
    # Testando os métodos
    print("\n🎓 ALUNO:")
    print(aluno1.apresentar())
    print(aluno1.verificar_notas())
    
    print("\n👨‍🏫 PROFESSOR:")
    print(professor1.apresentar())
    print(professor1.lancar_frequencia())
    
    print("\n" + "=" * 50)
    print("Demonstração concluída com sucesso! ✅")
    print("=" * 50)