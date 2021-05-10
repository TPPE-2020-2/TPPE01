from models.sequence_diagram_element import SequenceDiagramElement

class Lifeline(SequenceDiagramElement):
    def __init__(self, id=-1, name=''):
        super().__init__(name)
        self.id = id

    def __eq__(self, life_line): # pragma: no cover
        return self.name == life_line.name and \
                self.id == life_line.id
    
    def __str__(self): # pragma: no cover
        return 'ID: {}\nName: {}\n'.format(self.id, self.name)

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id
