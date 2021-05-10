from models.sequence_diagram import SequenceDiagram

sequence_diagram = SequenceDiagram()

class MakeXML:
  def get_tab(self, size):
      return '\t'.expandtabs(size)

  def define_lifeline(sequence_diagram):
    xml += self.get_tab(4) + '<Lifelines>\n'
    for lifeline in sequence_diagram.life_lines.values():
        xml += self.get_tab(8) + f'<Lifeline name="{lifeline.name}">' + '\n'
    xml += self.get_tab(4) + '</Lifelines>\n'
  
  def define_fragments(sequence_diagram):
    xml += self.get_tab(4) + '<Fragments>\n'
    for fragment in sequence_diagram.fragments:
        xml += self.get_tab(8) + f'<Optional name="{fragment.name}" representedBy="{fragment.represented_by}">\n'
    xml += self.get_tab(4) + '</Fragments>\n'
  
  def define_messages(sequence_diagram):
    xml += self.get_tab(4) + f'<SequenceDiagram name="{self.name}">\n'
    for message in sequence_diagram.messages.values():
        xml += self.get_tab(8) + f'<Message name="{message.name}" prob="{message.prob}" source="{message.source.name}" target="{message.target.name}">\n'

  def to_xml(self):
    print(sequence_diagram.messages)
    print(type(sequence_diagram.messages))
    xml = '<SequenceDiagrams>\n'
    self.define_lifeline()
    self.define_fragments()
    self.define_messages()
    xml += self.get_tab(8) + f'<Fragment name="{sequence_diagram.fragment.name}">\n'
    xml += self.get_tab(4) + '</SequenceDiagram>\n'
    xml += '</SequenceDiagrams>\n'

    print(xml)
    return xml