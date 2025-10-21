class Livro:
    def __init__(self, titulo, autor, isbn, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = disponivel

class Usuario:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.historico = Pilha()

class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        return None

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        return None

class Fila:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def enfileirar(self, item):
        self.items.insert(0, item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop()
        return None

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinariaBusca:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor.titulo < no.valor.titulo:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir(no.direita, valor)

    def buscar(self, titulo):
        return self._buscar(self.raiz, titulo)

    def _buscar(self, no, titulo):
        if no is None or no.valor.titulo == titulo:
            return no
        if titulo < no.valor.titulo:
            return self._buscar(no.esquerda, titulo)
        return self._buscar(no.direita, titulo)

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, usuario):
        if self.cabeca is None:
            self.cabeca = usuario
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = usuario

    def buscar(self, matricula):
        atual = self.cabeca
        while atual is not None and atual.matricula != matricula:
            atual = atual.proximo
        return atual

class TabelaHash:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def _hash(self, chave):
        return hash(chave) % self.tamanho

    def adicionar_livro(self, livro):
        indice = self._hash(livro.isbn)
        self.tabela[indice].append(livro)

    def buscar_livro(self, isbn):
        indice = self._hash(isbn)
        for livro in self.tabela[indice]:
            if livro.isbn == isbn:
                return livro
        return None

class SistemaBiblioteca:
    def __init__(self):
        self.livros = TabelaHash(100)
        self.usuarios = ListaEncadeada()
        self.arvore_livros = ArvoreBinariaBusca()
        self.fila_espera = Fila()

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        isbn = input("Digite o ISBN do livro: ")
        livro = Livro(titulo, autor, isbn)
        self.livros.adicionar_livro(livro)
        self.arvore_livros.inserir(livro)
        print(f"Livro '{titulo}' cadastrado com sucesso.")

    def cadastrar_usuario(self):
        nome = input("Digite o nome do usuário: ")
        matricula = input("Digite a matrícula do usuário: ")
        usuario = Usuario(nome, matricula)
        self.usuarios.adicionar(usuario)
        print(f"Usuário '{nome}' cadastrado com sucesso.")

    def emprestar_livro(self):
        matricula = input("Digite a matrícula do usuário: ")
        isbn = input("Digite o ISBN do livro: ")
        usuario = self.usuarios.buscar(matricula)
        livro = self.livros.buscar_livro(isbn)
        if usuario and livro:
            if livro.disponivel:
                livro.disponivel = False
                usuario.historico.empilhar(livro)
                print(f"Livro '{livro.titulo}' emprestado para '{usuario.nome}'.")
            else:
                self.fila_espera.enfileirar((matricula, isbn))
                print(f"Livro '{livro.titulo}' indisponível. Adicionado à lista de espera.")
        else:
            print("Usuário ou livro não encontrado.")

    def devolver_livro(self):
        matricula = input("Digite a matrícula do usuário: ")
        isbn = input("Digite o ISBN do livro: ")
        usuario = self.usuarios.buscar(matricula)
        livro = self.livros.buscar_livro(isbn)
        if usuario and livro:
            if not livro.disponivel:
                livro.disponivel = True
                print(f"Livro '{livro.titulo}' devolvido por '{usuario.nome}'.")
                if not self.fila_espera.esta_vazia():
                    prox_usuario, prox_isbn = self.fila_espera.desenfileirar()
                    self.emprestar_livro(prox_usuario, prox_isbn)
            else:
                print("Este livro já está disponível.")
        else:
            print("Usuário ou livro não encontrado.")

    def consultar_livros_disponiveis(self):
        print("Livros Disponíveis:")
        self._consultar_livros_disponiveis(self.arvore_livros.raiz)

    def _consultar_livros_disponiveis(self, no):
        if no:
            self._consultar_livros_disponiveis(no.esquerda)
            if no.valor.disponivel:
                print(f"- {no.valor.titulo} por {no.valor.autor}")
            self._consultar_livros_disponiveis(no.direita)

    def consultar_historico_emprestimos(self):
        matricula = input("Digite a matrícula do usuário: ")
        usuario = self.usuarios.buscar(matricula)
        if usuario:
            if not usuario.historico.esta_vazia():
                print(f"Histórico de empréstimos de {usuario.nome}:")
                while not usuario.historico.esta_vazia():
                    livro = usuario.historico.desempilhar()
                    print(f"- {livro.titulo} por {livro.autor}")
            else:
                print("Este usuário não tem histórico de empréstimos.")
        else:
            print("Usuário não encontrado.")

# Exemplo de uso do sistema de biblioteca
sistema = SistemaBiblioteca()

while True:
    print("\nSistema de Biblioteca")
    print("1. Cadastrar Livro")
    print("2. Cadastrar Usuário")
    print("3. Empréstimo de Livro")
    print("4. Devolução de Livro")
    print("5. Consultar Livros Disponíveis")
    print("6. Consultar Histórico de Empréstimos")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        sistema.cadastrar_livro()
    elif opcao == "2":
        sistema.cadastrar_usuario()
    elif opcao == "3":
        sistema.emprestar_livro()
    elif opcao == "4":
        sistema.devolver_livro()
    elif opcao == "5":
        sistema.consultar_livros_disponiveis()
    elif opcao == "6":
        sistema.consultar_historico_emprestimos()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
