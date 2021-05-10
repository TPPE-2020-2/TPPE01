from utils.sequence_diagram_helper import SequenceDiagramHelper
from models.sequence_diagram import SequenceDiagram

sequence_diagram_helper = SequenceDiagramHelper()

class Response():
    def __init__(self, option=''):
        if(option == '1'):
            print('----- Sequence Diagram -----')
            name = input('Insert the Sequence Diagram name: ')
            print('Insert the guard condition:',
                                    '\n 1 - True',
                                    '\n 2 - False')
            guard_condition = input()
            guard_condition = True if guard_condition == 1 else False
            sequence_diagram = SequenceDiagram(name=name, guard_condition=guard_condition)
            sequence_diagram_helper.sequence_diagram_menu(sequence_diagram)
            util.clear()
        elif(option == '2'):
            print('Leaving the program!')
            return 0
        else:
            util.clear()
            print('Invalid input. Please select again\n')