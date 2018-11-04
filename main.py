from operator import itemgetter

cash = []
num_cash = []
value = 0

def get_cash():
    """
    Function to get the cash that will be available
    """
    typed = 0
    while typed != -1:
        typed = int(input("input: "))
        cash.append(typed)
       
    cash.sort()
    cash.reverse()

def get_value():
    """
    Function to pick the total cash
    """
    typed = 0
    while typed != -1:
        typed = int(input("input: "))
        if typed != -1 and typed > 0:
            value = typed
            print("output: Notas necessarias para compor o valor de {0}: \n"
            "2 notas de 50 \n"
            "1 nota de 30 \n"
            "4 notas de 1".format(value))

def main():
    """
    Main function
    """
    get_cash()
    get_value()


if __name__ == '__main__':
    main()
