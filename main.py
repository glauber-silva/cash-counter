from operator import itemgetter

cash = []
num_cash = []

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

def count(value):
    """
    This function will calcule the amount of cash and print 
    """
    
    print("output: Notas necessarias para compor o valor de {0}:".format(value))

    for i in cash:
        if value >= i:
            num_cash.append(int(value/i))
            value %= i
        else:
            num_cash.append(0)
    
    for i in range(len(cash) - 1 ):
        if num_cash[i] != 0:
            print("{0} notas de {1}".format(num_cash[i], cash[i]))
       
    num_cash.clear()

def get_value():
    """
    Function to pick the total cash
    """
    typed = 0
    while typed != -1:
        typed = int(input("input: "))
        if typed != -1 and typed > 0:
            count(typed)

def main():
    """
    Main function
    """
    get_cash()
    get_value()

if __name__ == '__main__':
    main()
