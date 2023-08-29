import funcoes3
 

# Solicitando nome, email
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")


# Validando nome e email
validaNome = input(f"Seu nome ({nome}) e email ({email}) estão corretos? \nResponda com 'Sim' ou 'Não': ")
while validaNome.lower() != "sim":
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    validaNome = input(f"Seu nome ({nome}) e email ({email}) estão corretos?  \nResponda com 'Sim' ou 'Não': ")

 

# Solicitando uma senha de  no minímo oito digítos
senha = input("Digite sua senha (minímo de oito dígitos): ")


# Validando senha com no mínimo 8 dígitos
while len(senha) < 8:
    senha = input("Digite sua senha (minímo de oito dígitos): ")


# Perguntando se a senha está correta
validaSenha = input(f"Sua senha ({senha}) está correta? \nResponda com 'Sim' ou 'Não': ")

while validaSenha.lower() != "sim":
    senha = input("Digite sua senha (minímo de oito dígitos): ")
    validaSenha = input(f"Sua senha: {senha} está correta? \nResponda com 'Sim' ou 'Não': ")

 

# Iniciando o loop
while True:

    # Criando um menu de opções para o usuário
    menu = '''
    [1]- Como você imagina que é para um cadeirante ao pegar um ônibus \n
    [2]- Cheque sua rota do ônibus \n
    [3]- Quiz sobre acessibilidade em transportes públicos \n
    [4]- Encerrar programa
    '''
    print(menu)
    escolha = int(input("Escolha uma das opções acima (de 1 - 4): "))
 

    # Repetindo a pergunta caso o numero não esteja entre 1 e 4
    while escolha > 4 or escolha < 1:
        escolha = int(input("Escolha uma das opções acima (de 1 - 4): "))


# Encerrando o programa caso o usuário deseje
    if escolha == 4:
        print("Programa encerrado")
        break

 

# Criando situação 1

# Criando a variável respostas[], para armazenar todas as respostas do usuário
    respostas1 = []


# Iniciando as perguntas
    if escolha == 1:
        for a in range(5):
            opcao1 = input("Digite uma situação em que você imagina que um cadeirante tem dificuldade para pegar um ônibus: ")
            respostas1.append(opcao1)

        
# Perguntando se o usuário quer receber suas respostas de volta
        respostas2 = input(f"{nome}, você gostaria de receber suas respostas de volta? \nResponda com 'Sim' ou 'Não': ")
        if respostas2.lower() == "sim":
            print(f"Suas respostas foram: {respostas1} \nMuito obrigado, {nome}!")

 

# Criando situação 2
    if escolha == 2:
# Printando menu de opções de linhas dos ônibus
        print('''[1] - Linha 1 (Metrô Tucuruvi - Terminal Bandeira) \n[2] - Linha 2 (Terminal Pirituba - Terminal Princesa Isabel) \n[3] - Linha 3 (Terminal Campo Limpo - Metrô São Judas) \n[4] - Linha 4 (Metrô Tucuruvi - Pinheiros)''')
        escolha2 = int(input("Escolha uma das linhas: "))
        

# Criando condição caso escolha a linha errada, para escolher novamente
        while escolha2 != 1 and escolha2 != 2 and escolha2 != 3 and escolha2 != 4:
            print('''[1] - Linha 1 (Metrô Tucuruvi - Terminal Bandeira) \n[2] - Linha 2 (Terminal Pirituba - Terminal Princesa Isabel) \n[3] - Linha 3 (Terminal Campo Limpo - Metrô São Judas) \n[4] - Linha 4 (Metrô Tucuruvi - Pinheiros)''')
            escolha2 = int(input("Escolha uma das linhas: "))
            
# Estruturas de condicionamento para cada escolha de linha
        # Linha 1
        if escolha2 == 1:
         
           print("Os ônibus disponiveis na linha 1 no momento são: \n309 \n105 \n056")
           dicionario_linha1 = {
               '309': 'Rampa de Acesso',
               '105': 'Elevador',
                '056': 'Nenhum tipo de acessibilidade'
           }
           onibus_linha1 = int(input("Escolha um desses ônibus e confira os níveis de acessibilidade dele: "))

           funcoes3.linha1(onibus_linha1)

        # Linha 2
        if escolha2 ==2:
            
            print("Os ônibus disponiveis na linha 2 no momento são: \n057 \n7662 \n1200-T")
            dicionario_linha2 = {
               '057': 'Rampa de Acesso',
               '7662': 'Elevador',
                '1200-T': 'Nenhum tipo de acessibilidade'
           }
            
            onibus_linha2 = int(input("Escolha um desses ônibus e confira os níveis de acessibilidade dele"))

        # Linha 3    
        if escolha2 == 3:

            print("Os ônibus disponiveis na linha 3 no momento são: \n898 \n62 \n1432")
            dicionario_linha3 = {
               '898': 'Rampa de Acesso',
               '62': 'Elevador',
                '1432': 'Nenhum tipo de acessibilidade'
           }
            onibus_linha3 = int(input("Escolha um desses ônibus e confira os níveis de acessibilidade dele"))

        # Linha 4
        if escolha2 == 4:
            print("Os ônibus disponiveis na linha 4 no momento são: \n128 \n44 \n2870")
            dicionario_linha4 = {
               '2870': 'Rampa de Acesso',
               '44': 'Elevador',
                '128': 'Nenhum tipo de acessibilidade'
           }
            onibus_linha4 = int(input("Escolha um desses ônibus e confira os níveis de acessibilidade dele"))

 

# Criando a situação 3
    if escolha == 3:

    # Criando uma variável contadora para contar quantas questões o usuário acertou
        cont = 0

    # Chamando a função da primeira pergunta do quiz
        populacao = funcoes3.quiz1()
 

    # Conferindo se a resposta está correta e contando
        if populacao.lower() == "a":
            cont += 1


    # Chamando a função da segunda pergunta do quiz
        dificuldade = funcoes3.quiz2()
 

    # Conferindo se a resposta está correta e contando
        if dificuldade.lower() == "d":
            cont += 1

    
    # Chamando a função da terceira pergunta do quiz
        onibus = funcoes3.quiz3()


    # Conferindo se a resposta está correta e contando
        if onibus.lower() == "b":
            cont += 1

       
    # Chamando a função da quarta pergunta do quiz
        acessibilidade = funcoes3.quiz4()


    # Conferindo se a resposta está correta e contando
        if acessibilidade.lower() == "c":
            cont += 1


    # Transformando as questões em variáveis
        a2 = ("Quantos '%' da população brasileira possui algum tipo de deficiência? \na)35% \nb)20% \c)24% \nd)25%")
        b2 = ("Quantos '%' das pessoas com deficiência no Brasil passam por dificuldades ao pegar um transporte público? \na) 50% \nb) 55% \nc) 65% \nd) 63%")
        c2 = ("Quantos '%' dos ônibus urbanos você acha que atendem plenamente as necessidades dos deficientes? \na) 1% \nb)0.9% \nc) 1.5% \nd)1.3%")
        d2 = ("Quantos '%' dos deficientes dizem que os ônibus tem uma acessibilidade boa ou muito boa? \na) 20% \nb) 25% \nc) 22% \nd) 18%")

 

    # Perguntando para o usuário se ele quer receber suas respostas de volta e seu resultado final
        pergunta = input( "Você gostaria de receber suas respostas de volta? Além disso seu resultado final? \nResponda com 'Sim' ou 'Não': ")

   

    # Criando um loop para resposta ser "sim" ou "não"
        while pergunta.lower() != "sim" and pergunta.lower() != "não" and pergunta.lower() != "nao":
            pergunta = input("Você gostaria de receber suas respostas de volta? Além disso seu resultado final? \nResponda com 'Sim' ou 'Não': ")

 

    # Devolvendo as respostas e resultado caso solicitado
        if pergunta.lower() == "sim":
            print(f'1- {a2} \nResposta: {populacao} \n\n{b2} \nResposta: {dificuldade} \n\n')
            print(f'2- {c2} \nResposta: {onibus} \n\n{d2} \nResposta: {acessibilidade} \n\n')
            print(f"Seu resultado foi de {cont}/4")
            print(f'\nObrigado, {nome}! \nQuiz finalizado.\n\n\n')
        else:
            print(f'\nObrigado, {nome}! \nQuiz finalizado.\n\n\n')


    # Fazendo resumo das operações realizadas