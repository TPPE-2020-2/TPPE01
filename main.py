from models.sequence_diagram import SequenceDiagram
from models.fragment import Fragment
from models.lifeline import Lifeline
from models.message import Message
from utils.utils import Util
from time import sleep

util = Util()


def main():
    while(True):
        print('----- Main Menu -----')
        print('Select the diagram you want to generate:\n'
            '1 - Sequence Diagram\n'
            '2 - Exit')
        user_in = input('Insert your option: ')
        
        if(user_in == '1'):
            print('----- Sequence Diagram -----')
            name = input('Insert the Sequence Diagram name: ')
            print('Insert the guard condition:',
                                    '\n 1 - True',
                                    '\n 2 - False')
            guard_condition = input()
            guard_condition = True if guard_condition == 1 else False
            sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
            sequence_diagram_menu(sequence_diagram)
            util.clear()
        elif(user_in == '2'):
            print('Leaving the program!')
            return 0
        else:
            util.clear()
            print('Invalid input. Please select again\n')


def sequence_diagram_menu(sequence_diagram):
    util.clear()
    lifelines = get_lifelines()
    sequence_diagram.set_life_lines(lifelines)
    while True:
        print('----- Sequence Diagram Menu -----')
        print('Select the element you want to generate:\n'
              f'1 - {util.MESSAGE}\n'
              f'2 - {util.FRAGMENT}\n'
              '3 - Return to Main Menu')
        user_in = input('Insert your option: ')
        if user_in == '1':
            sequence_diagram.set_messages(add_message(lifelines))
        elif user_in == '2':
            sequence_diagram.set_fragments(add_fragment())
        elif user_in == '3':
            return sequence_diagram
        else:
            util.clear()
            print('Invalid input. Please select again\n')


def get_lifelines():
    lifelines = {}
    lifelines_amount = input('Insert the number of lifelines:')
    for index, lifeline in enumerate(range(int(lifelines_amount))):
        print(f'Insert the {index + 1} Lifeline name: ')
        lifeline_name = input()
        lifeline = Lifeline(id=index, name=lifeline_name)
        lifelines[index] = lifeline
        print()
    return lifelines


def add_fragment():
    fragment_name = input('Insert the Fragment name: ')
    diagram_name = input('Insert the Sequence Diagram name: ')
    fragment = Fragment(name=fragment_name, represented_by=diagram_name)
    return fragment


def add_message(lifelines):
    message_type_dict = {
        1: 'Synchronous',
        2: 'Assynchronous',
        3: 'Reply'
    }

    message_name = input('Insert the Message name: ')
    while(len(message_name)==0):
        print('MessageFormatException - You must define a message name')

    print('Select the source Lifeline: ')
    print_lifelines(lifelines)
    try:

        source_lifeline = lifelines[int(input('Which is the initial Lifeline?'))]
    except:
        print('MessageFormatException - Please select a valid Lifeline')
        source_lifeline = lifelines[int(input('Which is the initial Lifeline?'))]

    try:
        target_lifeline = lifelines[int(input('Which is the final Lifeline?'))]
    except:
        print('MessageFormatException - Please select a valid Lifeline')
        target_lifeline = lifelines[int(input('Which is the initial Lifeline?'))]

    prob = input('How much is the message probability?')
    print_message_type()
    message_type = message_type_dict[int(input())]

    message = Message(name=message_name, source=source_lifeline,
                      target=target_lifeline, prob=prob,
                      message_type=message_type)
    return message

def print_lifelines(lifelines):
    print('Your Lifelines: ')
    for index, lifeline in lifelines.items():
        print('Lifeline', str(index) + ':', lifeline.name)

def print_message_type():
    print('These are your message type options, please select one: ',
          '\n 1 - Synchronous',
          '\n 2 - Aynchronous',
          '\n 3 - Reply')

def create_sequence_diagram():
    print('----- Sequence Diagram -----')
    name = input('Insert the Sequence Diagram name: ')
    print('Insert the guard condition:',
                            '\n 1 - True',
                            '\n 2 - False')
    guard_condition = input()
    guard_condition = True if guard_condition == 1 else False
    sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
    return sequence_diagram

if __name__ == '__main__':
    main()