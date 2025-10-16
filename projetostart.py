usuarios = [ ]
produtos= [ ]
escolha = '167'

while escolha != '0':
    print ('Bem-Vindo ao Fazenda Agro!')
    print ('.......MENU PRINCIPAL.......')
    print('1-Cadastrar familia\n2-Fazer login\n3-Vizualizar produtos de todas as famílias\n4-Vizualizar lista de usuários cadastrados\n0-Sair  ')
    escolha = input('Digite a opção escolhida: ')

    if escolha == '1':
        nome =input ('Digite seu nome: ')
        cpf = input ('Digit seu CPF: ')
        senha = input ('Crie uma senha: ').lower()
        confirm_senha = input ('Confirme sua senha:') .lower()

        while confirm_senha != senha :
            confirm_senha = input('As senhas estão diferentes. Digite novamente: ').lower()
        usuarios.append([nome,cpf, senha])
        print ('Cadastro concluído com sucesso!')

    elif escolha == '4':
        print(usuarios)

    elif escolha == '2':
        cpf = input('Digite seu CPF: ')
        senha = input('Digite sua senha: ').lower()
        log_ok= False
        for usu in usuarios:
            if cpf== usu [1] and senha == usu [2]:
                log_ok= True
                break
            else:
                print('Acesso negado - OK. Cadastre-se em nosso sistema ou insira seus dados corretamente.')


        op= None
        while op != '0':
            print('.......MENU INTERNO.........')
            print('1-Inserir produto\n2-Remover produto\n3-Mostrar lista de produtos cadastrados\n0-sair')
            op = input('Digite a opção escolhida: ')

            if op =='1':
                prod= input('Digite o nome do produto: ')
                quant = input('Digite a quantidade disponível do produto: ')
                valor = input('Digite o valor do produto: ')
                produtos.append ([prod, quant, valor, usuarios[0][1]])

            elif op== '3':
                print (produtos)

            elif op=='2':
                for itens in range (len (produtos)):
                    print (itens, 'Nome do produto:', produtos [itens][0])
                indice= int (input ('Digite o índice do produto escolhido: '))
                produtos.pop (indice)














