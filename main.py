from models.response import Response

def main():
    while(True):
        print('----- Main Menu -----')
        print('Select the diagram you want to generate:\n'
            '1 - Sequence Diagram\n'
            '2 - Exit')
        user_in = input('Insert your option: ')
        
        Response(user_in)



if __name__ == '__main__':
    main()