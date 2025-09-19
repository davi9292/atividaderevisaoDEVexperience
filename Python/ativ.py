# Davi de Assis, Vinicius Queiroz e Thomas Gabriel
# Sistema de Cadastro e Busca de Alunos

class Aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Curso: {self.curso}"
    
class SistemaCadastro:
    def __init__(self):
        self.alunos = []

    def cadastrar_aluno(self, nome, idade, curso):
        aluno = Aluno(nome, idade, curso)
        self.alunos.append(aluno)
        print(f"Aluno {nome} cadastrado com sucesso!")

    def buscar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
                return aluno
        return None

    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in self.alunos:
                print(aluno)
                

print("Bem-vindo ao Sistema de Cadastro e Busca de Alunos")
print("Desenvolvido por Davi de Assis, Vinicius Queiroz e Thomas Gabriel")
cadastro = input("gostaria de entrar em nosso sistema? (s/n)")
if cadastro.lower() == 's':
    sistema = SistemaCadastro()
    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Buscar Aluno")
        print("3. Listar Alunos")
        print("4. Sair")    
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Nome do aluno: ")
            idade = input("Idade do aluno: ")
            curso = input("Curso do aluno: ")
            sistema.cadastrar_aluno(nome, idade, curso)
        elif escolha == '2':
            nome = input("Nome do aluno a buscar: ")
            aluno = sistema.buscar_aluno(nome)
            if aluno:
                print(aluno)
            else:
                print("Aluno não encontrado.")
        elif escolha == '3':
            sistema.listar_alunos()
        elif escolha == '4':
            print("Saindo do sistema. Adeus!")
            break
        else:
            print("Opção inválida, coloque um dos numeros acima e tente novamente.")
else:
    print("Saindo do sistema. Adeus!")