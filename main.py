from models.diagrama_sequencia import SequenceDiagram
from models.diagrama_sequencia import Fragment
from models.diagrama_sequencia import Lifeline
from models.diagrama_sequencia import Message

from utils.utils import Util

util = Util()

def main():
    while(True):
        resposta = menu()
        if(resposta == '1'):
            print('***** Diagrama de Sequencia *****')
            nome = input('Insira o nome do Diagrama de Sequencia: ')
            print('Insira a condição de guarda:')
            print('1 - True')                       
            print('2 - False')

            condicao_guarda = input()
            if(condicao_guarda == 1):
                condicao_guarda = True
            else:
                condicao_guarda = False

            diagrama_sequencia = SequenceDiagram(nome=nome, condicao_guarda=condicao_guarda)
            menu_diagrama_sequencia(diagrama_sequencia)
            util.clear()
        elif(resposta == '2'):
            return 0
        else:
            util.clear()
            print('Opcao invalida, tente novamente\n')

def menu():
    print('******** Bem Vindo ********')
    print('Escolha um diagrama para gerar:')
    print('1 - Diagrama de Sequencia')
    print('2 - Sair do Programa')
    resposta = input('Escolha sua opcao: ')
    return resposta

def menu_diagrama_sequencia(diagrama_sequencia):
    util.clear()
    lifelines = get_lifelines()
    diagrama_sequencia.set_life_lines(lifelines)
    while True:
        print('***** Diagrama de Sequencia Menu *****')
        print('Escolha o elemento qe você quer gerar: ')
        print(f'1 - {util.MESSAGE}\n')
        print(f'2 - {util.FRAGMENT}\n')
        print('3 - Generate Diagram\n')
        print('4 - Return to Main Menu')
        resposta = input('Insira a opcao: ')
        if resposta == '1':
            # diagrama_sequencia.messages.append(add_message(lifelines))
            diagrama_sequencia.set_messages(add_message(lifelines))
            
        elif resposta == '2':
            # diagrama_sequencia.fragments.append(add_fragment())
            diagrama_sequencia.set_fragments(add_fragment())
        elif resposta == '3':
            util.generate_diagrama_sequencia(diagrama_sequencia)
            return 0
        else:
            util.clear()
            print('Invalid input. Please select again\n')

def get_lifelines():
    lifelines = {}
    lifelines_amount = input('Insira o numero de lifelines:')
    for index, lifeline in enumerate(range(int(lifelines_amount))):
        print(f'Insira o {index + 1} nome Lifeline: ')
        lifeline_nome = input()
        lifeline = Lifeline(id=index, nome=lifeline_nome)
        lifelines[index] = lifeline
        print()
    return lifelines


def add_fragment():
    fragment_nome = input('Insira o nome do fragmento: ')
    diagram_nome = input('Insira o nome do diagrama de sequencia: ')
    fragment = Fragment(nome=fragment_nome, represented_by=diagram_nome)
    return fragment


def add_message(lifelines):
    message_type_dict = {
        1: 'Synchronous',
        2: 'Assynchronous',
        3: 'Reply'
    }

    message_nome = input('Insira o nome da mensagem: ')
    print(message_nome)
    while(len(message_nome)==0):
        print('MessageFormatException - You must define a message nome')

    print('Selecione a fonte lifeline: ')
    print_lifelines(lifelines)
    print(lifelines)
    try:

        source_lifeline = lifelines[int(input('Qual a Lifeline inicial?'))]
    except:
        print('MessageFormatException - Selecione uma Lifeline válida')
        source_lifeline = lifelines[int(input('Which is the initial Lifeline?'))]

    try:
        target_lifeline = lifelines[int(input('Qual a Lifeline final?'))]
    except:
        print('MessageFormatException - Selecione uma Lifeline valida')
        target_lifeline = lifelines[int(input('Qual a Lifeline inicial?'))]

    prob = input('Como é a probabilidade da mensagem?')
    print_message_type()
    message_type = message_type_dict[int(input())]

    message = Message(nome=message_nome, source=source_lifeline,
                      target=target_lifeline, prob=prob,
                      message_type=message_type)
    return message


def print_lifelines(lifelines):
    print('Your Lifelines: ')
    for index, lifeline in lifelines.items():
        print('Lifeline', str(index) + ':', lifeline.nome)


def print_message_type():
    print('These are your message type options, please select one: ',
          '\n 1 - Synchronous',
          '\n 2 - Aynchronous',
          '\n 3 - Reply')


if __name__ == '__main__':
    main()