from utils.utils import Util
util = Util()

class SequenceDiagramElement():
    def __init__(self, nome=''):
        self.nome = nome

    def __eq__(self, sequence_diagram_element): # pragma: no cover
        return self.nome == sequence_diagram_element.nome
    
    def __str__(self): # pragma: no cover
        return 'nome: {}\n'.format(self.nome)

    def set_nome(self, nome):
        self.nome = nome
    
    def get_nome(self):
        return self.nome

    def dispose(self):
        self.nome = ""


class Fragment(SequenceDiagramElement):
    def __init__(self, nome='', represented_by=None):
        super().__init__(nome)
        self.represented_by = represented_by

    def __eq__(self, fragment): # pragma: no cover
        return self.nome == fragment.nome and \
                self.represented_by == fragment.represented_by
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nRepresented by: {}\n'.format(self.nome, self.represented_by)

    def set_represented_by(self, represented_by):
        self.represented_by = represented_by
    
    def get_represented_by(self):
        return self.represented_by


class Lifeline(SequenceDiagramElement):
    def __init__(self, id=-1, nome=''):
        super().__init__(nome)
        self.id = id

    def __eq__(self, life_line): # pragma: no cover
        return self.nome == life_line.nome and \
                self.id == life_line.id
    
    def __str__(self): # pragma: no cover
        return 'ID: {}\nName: {}\n'.format(self.id, self.nome)

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

class Message(SequenceDiagramElement):
    def __init__(self, nome='', source=None, target=None, prob=0, message_type=''):
        super().__init__(nome)
        self.source = source
        self.target = target
        self.prob = prob
        self.message_type = message_type
    
    def __eq__(self, message): # pragma: no cover
        return self.nome == message.nome and \
                self.source == message.source and \
                self.target == message.target and \
                self.prob == message.prob and \
                self.message_type == message.message_type
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nSource: {}\nTarget: {}\nProb: {}\nMessage Type: {}\n'.format(self.nome, \
                                                                                        self.source, \
                                                                                        self.target, \
                                                                                        self.prob, \
                                                                                        self.message_type)

    def set_source(self, source):
        self.source = source
    
    def set_target(self, target):
        self.target = target
    
    def set_prob(self, prob):
        self.prob = prob

    def set_message_type(self, message_type):
        self.message_type = message_type

    def get_source(self):
        return self.source
    
    def get_target(self):
        return self.target
    
    def get_prob(self):
        return self.prob

    def get_message_type(self):
        return self.message_type

    def to_xml(self):
        return f'<name="{self.nome}" prob="{self.prob}" source="{self.source}" target="{self.target}"/>'

class SequenceDiagram():
    def __init__(self, nome='', condicao_guarda=''):
        self.nome = ''
        self.condicao_guarda = ''
        self.life_lines = []
        self.messages = []
        self.fragments = []

    def __eq__(self, sequence_diagram): # pragma: no cover
        return self.nome == sequence_diagram.nome and \
        self.condicao_guarda == sequence_diagram.condicao_guarda and \
        self.life_lines == sequence_diagram.life_lines and \
        self.messages == sequence_diagram.messages and \
        self.fragments == sequence_diagram.fragments
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nGuard Condition: {}\nLife Lines: {}\nElements: {}\n'.format(self.nome, \
                                                                                self.start_node, \
                                                                                self.life_lines, \
                                                                                self.messages, \
                                                                                self.fragments)

    def set_condicao_guarda(self, condicao_guarda):
        self.condicao_guarda = condicao_guarda

    def set_life_lines(self, life_line):
        self.life_lines = life_line

    def set_messages(self, messages):
        self.messages.append(messages)

    def set_fragments(self, fragments):
        self.fragments.append(fragments)
        
    def dispose(self):
        self.nome = ''
        self.condicao_guarda = ''
        self.life_lines = {}
        self.messages = []
        self.fragments = []

    def set_nome(self, nome):
        self.nome = nome

    def get_nome(self):
        return self.nome
    
    def get_condicao_guarda(self):
        return self.condicao_guarda

    def get_life_lines(self):
        return self.life_lines
    
    def get_messages(self):
        return self.messages

    def get_fragments(self):
        return self.fragments

    def to_xml(self):
        xml = '<SequenceDiagrams>\n'
        xml += util.get_tab(4) + '<Lifelines>\n'
        for lifeline in self.life_lines.values():
            xml += util.get_tab(8) + f'<Lifeline name="{lifeline.nome}">' + '\n'
        xml += util.get_tab(4) + '<\Lifelines>\n\n'
        xml += util.get_tab(4) + '<Fragments>\n'
        for fragment in self.fragments:
            xml += util.get_tab(8) + f'<Optional name="{fragment.nome} representedBy="{self.nome}">\n'
        xml += util.get_tab(4) + '</Fragments>\n'
        xml += util.get_tab(4) + f'<SequenceDiagram name="{self.nome}">\n'
        for message in self.messages:
            xml += util.get_tab(8) + f'{message.to_xml()}\n'
        xml += util.get_tab(8) + f'<Fragment name="{self.nome}">\n'
        xml += util.get_tab(4) + '</SequenceDiagram>\n\n'
        xml += '</SequenceDiagrams>\n'

        print(xml)
        return xml