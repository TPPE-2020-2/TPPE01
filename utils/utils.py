class Util():
    def __init__(self):
        self.MESSAGE='Message'
        self.FRAGMENT='Fragment'
 
    def clear(self):
        for i in range(1, 20):
            print()
        return 0
    
    def generate_diagrama_sequencia(self, sequence_diagram):
        xml = sequence_diagram.to_xml()
        f = open(f"docs/{sequence_diagram.nome}.xml", "w+")
        f.write(xml)
        f.close()


    def get_tab(self, size):
        return '\t'.expandtabs(size)