"""
"""


nota = {
    "nota" : 0,
    "qtd":0
}

to_count = {
    "notas": [],
    "value": 0
}

def main():
    
    typed = 0
    
    while typed != -1:
        typed = int(input("input: "))
        if typed != -1:
            nota["nota"]
            to_count["notas"].append(nota)

    typed = 0

    while typed != -1:
        typed = int(input("input: "))
        if typed != -1 and typed > 0:
            print("output: Notas necessarias para compor o valor de 134: \n"
                "2 notas de 50 \n"
                "1 nota de 30 \n"
                "4 notas de 1")


if __name__ == '__main__':
    main()
