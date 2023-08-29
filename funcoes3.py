import sprint3

# CRIANDO FUNÇÕES DA ESCOLHA NÚMERO 2
# Criando a primeira função (primeira opção do menu)
def linha1(onibus_linha1):
    if onibus_linha1 == 309:
        return sprint3.dicionario_linha1['309']
    elif onibus_linha1 == 105:
        return sprint3.dicionario_linha1['105']
    elif onibus_linha1 == 56:
        return sprint3.dicionario_linha1['056']
    else:
        return "Ônibus não encontrado, por favor tente novamente"


# CRIANDO FUNÇÕES DA ESCOLHA NÚMERO 3
# Fazendo a primeira pergunta do quiz com uso de função
def quiz1():
    questao1 = input("Quantos '%' da população brasileira possui algum tipo de deficiência? \na)35% \nb)20% \nc)24% \nd)25% \nResposta: ")
    return questao1


# Criando a segunda pergunta com uso de função
def quiz2():
    questao2 = input("Quantos '%' das pessoas com deficiência no Brasil passam por dificuldades ao pegar um transporte público? \na) 50% \nb) 55% \nc) 65% \nd) 63% \nResposta: ")
    return questao2


# Fazendo a terceira pergunta com uso de função
def quiz3():
    questao3 = input(
        "Quantos '%' dos ônibus urbanos você acha que atendem plenamente as necessidades dos deficientes? \na) 1% \nb) 0.9% \nc) 1.5% \nd) 1.3% \nResposta: ")
    return questao3


# Fazendo a quarta pergunta com uso de função
def quiz4():
    questao4 = input(
        "Quantos '%' dos deficientes dizem que os ônibus tem uma acessibilidade boa ou muito boa? \na) 20% \nb) 25% \nc) 22% \nd) 18% \nResposta: ")
    return questao4

    