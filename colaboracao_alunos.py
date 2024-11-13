while True:    
    pesquisa = input("\nPara Pesquisar o nome e RA do aluno:\nEscolha [sim] para realizar a pesquisa \nou\nEscolha [não] para encerrar o programa: \nDigite aqui sua decisão: ").strip().lower()
    
    if pesquisa == 'sim':
        try:
            n = int(input("\nDigite seu número da lista de chamada: "))

            match n:
                case 1:
                    print("\n\n\n\nNão Participou da Atividade")
                case 2:
                    print("\n\n\n\nNome: Ana Beatriz Gomes Vieira,RA:00001104119778SP")
                case 3:
                    print("\n\n\n\nNão Participou da Atividade")
                case 4:
                    print("\n\n\n\nNão Participou da Atividade")
                case 5:
                    print("\n\n\n\nNão Participou da Atividade")
                case 6:
                    print("\n\n\n\nNome: Eryck Nascimento dos Santos, RA: 001104052234")
                case 7:
                    print("\n\n\n\nNome:Fabricio de Oliveira Mello -RA:00001139909817SP")
                case 8:
                    print("\n\n\n\nNão Participou da Atividade")
                case 10:
                    print("\n\n\n\nNão Participou da Atividade")
                case 11:
                    print("\n\n\n\nNOME: Gabriella Gomes, RA: 1132687007")
                case 12:
                    print("\n\n\n\nNão Participou da Atividade")
                case 13:
                    print("\n\n\n\nNão Participou da Atividade")
                case 14:
                    print("\n\n\n\nNão Participou da Atividade")
                case 15:
                    print("\n\n\n\nNão Participou da Atividade")
                case 16:
                    print("\n\n\n\n NOME: Hesther Maria, RA: 1093739186SP")
                case 17:
                    print("\n\n\n\nNão Participou da Atividade")
                case 18:
                    print("\n\n\n\nNão Participou da Atividade")
                case 19:
                    print("\n\n\n\nNão Participou da Atividade")
                case 21:
                    print("\n\n\n\nNão Participou da Atividade")
                case 23:
                    print("\n\n\n\nNOME: Kelly Cristine Souza da Cruz, RA: 000112249761")
                case 25:
                    print("\n\n\n\nNão Participou da Atividade")
                case 26:
                    print("\n\n\n\nNão Participou da Atividade")
                case 27:
                    print("\n\n\n\nNão Participou da Atividade")
                case 28:
                    print("\n\n\n\nNão Participou da Atividade")
                case 29:
                     print("\n\n\n\nNome: Luan Ferreira, RA: 0001111616565")
                case 30:
                    print("\n\n\n\nNão Participou da Atividade")
                case 31:
                    print("\n\n\n\nNome:Lucas Celestino Santos   RA: 00001103831641SP")
                case 32:
                    print("\n\n\n\nNão Participou da Atividade")
                case 33:
                    print("\n\n\n\nNOME:Luiz Felipe da Silva Nolasco, RA: 00001103572969")
                case 34:
                    print("\n\n\n\nNão Participou da Atividade")
                    print("\n\n\n\nNOME: Maria Eduarda de Souza, RA:0001166754455")
                case 35:
                    print("\n\n\n\nNão Participou da Atividade")
                case 36:
                    print("\n\n\n\nNão Participou da Atividade")
                case 37:
                    print("\n\n\n\nNão Participou da Atividade")
                case 42:
                    print("\n\n\n\nNome: Sabrina Lombizani Mendes Carvalho, RA: 00001104023969")
                case 43:
                    print("\n\n\n\nNão Participou da Atividade")
                case 44:
                    print("\n\n\n\nNão Participou da Atividade")
                case 45:
                    print("\n\n\n\nNão Participou da Atividade")

                case _:
                    print("\n\nNúmero de chamada não encontrado.\n\n")

        except ValueError:
            print("\n\nErro: Por favor, insira um número inteiro válido.\n\n")

    elif pesquisa == 'não' or pesquisa == 'nao':
            print("\n\nObrigado pela preferência e volte sempre ;)\n\n")
            break
    else:
        print("\n\nOpção inválida, por favor, digite 'sim' ou 'não'.\n\n")
