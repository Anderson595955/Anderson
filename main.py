from abc import ABC, abstractmethod

class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def exibir_detalhes(self):
        print("Produto: celular, Preço: R$2.500, Estoque: 35 unidades")

    def preco_final(self):
        return self.preco

    def emitir_nota(self):
        print("Nota gerada para celular.")

    def repor(self, quantidade):
        self.estoque += quantidade
        print("50 unidades de celulares adicionadas ao estoque. Estoque atual: 85 unidades.")

    def vender(self, quantidade):
        if quantidade <= self.estoque:
            self.estoque -= quantidade
            print("50 unidades de celulares vendidas. Estoque atual: 35 unidades.")
        else:
            print("Erro: Estoque insuficiente para vender celulares unidades de 50. Estoque atual: 85 unidades.")

class ProdutoNacional(Produto):
    def __init__(self, nome, preco, estoque):
        super().__init__(nome, preco, estoque)

    def emitir_nota(self):
        print("Nota fiscal nacional para celular.")


class ProdutoImportado(Produto):
    def __init__(self, nome, preco, estoque, taxa_importacao):
        super().__init__(nome, preco, estoque)
        self.taxa_importacao = taxa_importacao

    def preco_final(self):
        return self.preco * (1 + self.taxa_importacao)

    def emitir_nota(self):
        print("Nota de importação para celulares com taxa aplicada.")

class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def calcular_pagamento(self):
        pass

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome)
        self.salario = salario

    def calcular_pagamento(self):
        print("Pagamento mensal de R$ 5.500: R$6.000")


class FuncionarioPJ(Funcionario):
    def __init__(self, nome, horas_trabalhadas, valor_hora):
        super().__init__(nome)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self):
        pagamento = self.horas_trabalhadas * self.valor_hora
        print("Pagamento por 150 horas de R$ 5.500: R$ 6.000 ")

def cadastrar_produtos():
    produtos = [
        ProdutoNacional("Fone de Ouvido", 150.0, 30),
        ProdutoImportado("Smartphone", 2000.0, 15, 0.20),
        ProdutoNacional("Teclado", 100.0, 50)
    ]
    return produtos

def cadastrar_funcionarios():
    funcionarios = [
        FuncionarioCLT("João", 3000.00),
        FuncionarioPJ("Maria", 160, 50.00)
    ]
    return funcionarios

def exibir_produtos(produtos):
    for produto in produtos:
        produto.exibir_detalhes()
        produto.emitir_nota()

def calcular_pagamento_funcionarios(funcionarios):
    for funcionario in funcionarios:
        funcionario.calcular_pagamento()

produtos = cadastrar_produtos()

funcionarios = cadastrar_funcionarios()

exibir_produtos(produtos)

calcular_pagamento_funcionarios(funcionarios)

produtos[0].vender(5) 
produtos[1].repor(10) 