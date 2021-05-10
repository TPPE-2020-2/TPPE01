from models.sequence_diagram_element import SequenceDiagramElement
class Fragment(SequenceDiagramElement):
    def __init__(self, name='', represented_by=None):
        super().__init__(name)
        self.represented_by = represented_by

    def __eq__(self, fragment): # pragma: no cover
        return self.name == fragment.name and \
                self.represented_by == fragment.represented_by
    
    def __str__(self): # pragma: no cover
        return 'Name: {}\nRepresented by: {}\n'.format(self.name, self.represented_by)

    def set_represented_by(self, represented_by):
        self.represented_by = represented_by
    
    def get_represented_by(self):
        return self.represented_by