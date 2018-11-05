#cash-counter

***

Desenvolver o teste abaixo utilizando Python.

Definição: Criar um projeto em python que exiba quais notas são necessárias para compor um valor 'x' e qual a quantidade de cada uma. As notas disponíveis são informadas pelo usuário e as mesmas serão infinitas, podendo utilizar quantas forem necessárias para compor o valor. Desconsidere os centavos.


 ##### Inputs (Terminal):

  * a) Usuário devera entrar com todas as notas disponíveis 'y', onde 'y' é inteiro e 1 <= y <= 1000. Não sera necessário exibir a quantidade de cada nota, pois, como dito na definição do problema as notas que forem adicionadas são infinitas, isso é, se a nota de valor 5 esta disponível a mesma poderá ser utilizada quantas vezes for necessário para compor um certo valor 'x'. Para finalizar o usuario devera digitar "-1".


  * b) Usuario devera entrar com todos os testes 'x', onde 'x' é inteiro e 0 <= z <= 10000. Para finalizar o usuario devera digitar "-1".

##### Saída: 

Apos processar cada teste, o resultado devera ser printado na tela informando quais notas são necessárias e qual a quantidade de cada uma sera necessária para compor o valor 'x' digitado pelo usuário, lembrando que só poderá utilizar as notas disponíveis na lista de notas validas.

***
Exemplo de uso:
```
input:  50   // representa que tem a nota de valor igual a 50 disponivel no caixa
input:  30   // representa que tem a nota de valor igual a 30 disponivel no caixa
input:  1    // representa que tem a nota de valor igual a 1 disponivel no caixa
input:  -1   // fim
input:  134  // representa que vão ser processado
output: Notas necessarias para compor o valor de 134:
  2 notas de 50
  1 nota de 30
  4 notas de 1
input:  10  // representa que vão ser processado
output: Notas necessarias para compor o valor de 10:
  10 nota de 1
input: -1    // fim
```

***

Para executar este programa
Caso não tenha o git, siga esse doc: https://git-scm.com/book/pt-br/v1/Primeiros-passos-Instalando-Git

Caso  não tenha o python instalado, siga um dos docs abaixo:
* Windows: https://python.org.br/instalacao-windows/
* Linux: https://python.org.br/instalacao-linux/


Siga os passado abaixo:
```
$ git clone https://github.com/glauber-silva/cash-counter.git
$ cd cash-counter
$ python3 main.py
```

Para rodar os testes:
```
$python3 -m unittest
```



