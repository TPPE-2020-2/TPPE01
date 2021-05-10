from time import sleep
from services.make_xml import MakeXML 

make_xml = MakeXML()

class Util():
    def __init__(self):
        self.LIFELINE = 'LifeLine'
        self.MESSAGE = 'Message'
        self.FRAGMENT = 'Fragment'
    
    def clear(self):
        for i in range(1, 20):
            print()
        return 0

    def print_and_clear(self, message, clear=True):
        if(clear):
            self.clear()
        print('-'*64)
        print(message)
        print('-'*64)
        sleep(2)
   
    def generate_diagrama_sequencia(self, sequence_diagram):
        xml = make_xml.to_xml()
        f = open(f"docs/{sequence_diagram.nome}.xml", "w+")
        f.write(xml)
        f.close()
