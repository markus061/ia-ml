#Exercício 1 • Olá, Mundo! (exercício-modelo)


#Objetivo: Compreender a estrutura mínima de um programa em Python e o uso de comentários.
#Atividades:
#• Digite e execute o código acima em seu ambiente Python.
#• Altere a mensagem para exibir o seu próprio nome, por exemplo: Olá, meu nome é ....
#• Adicione um comentário acima do print explicando o que aquela linha faz


#Botar hashtags (#) é como se colocam comentarios, eles não afetam o código, e é bom para ou deixar notas para outros progamadores, ou pro você do futuro que não se lembra o que era pra fazer

#A função do print serve para IMPRIMIR, você poderia imprimir números, mas também é util pra STRINGS que geralmente são frases ou palavras

#O que são STRINGS? basicamente é o que nos colocamos dentro das aspas (""), enquanto print() é uma FUNÇÃO (existem outras funções, como INPUT(), que vamos ver depois)
#E também tem VARIAVEIS, que vamos ver na questão 3, mas se lembre de FUNÇÕES, VARIAVEIS E STRINGS

#A função print exibe uma mensagem no terminal
print("Olá meu nome é Marcus")


#Exercício 2 • Sequência de números
#Objetivo: Praticar a ideia de estrutura sequencial: uma lista de instruções executadas uma após a outra, na ordem em que aparecem

#Tem jeito de fazer isso de maneira mais automatica, mas não vamos aprender isso agora
print(1) 
print(2) 
print(3) 
print(4) 
print(5) 
print(6) 
print(7) 
print(8) 
print(9) 
print(10) 
 

#Exercício 3 • Trabalhando com variáveis
# Objetivo: Entender o que é uma variável e como armazenar e exibir valores
# Neste caso, (Ex: Nome, idade e etc...) são as variaveis, e o que estão dentro das variaveis são DATA (Ex: Guilherme)

#O que são variaveis? Basicamente é Data/informação/Valor que nos queremos manter armazenada na memoria do codigo, para que nos possamos re-chamar elas a qualquer momento,
# mas só dá para usar DEPOIS da linha que foi escrita, não daria pra usar o Nome ou Idade antes dessas linhas
#Como o pdf fala "Uma variavel funciona como uma caixa onde guardamos um valor para usar depois"
Nome = "Marcus"
Curso = "IA e Machine Learning" 
Cidade = "Vicente Pires"
print(Nome)
print(Cidade)
print(Curso)
#Exercício 4 • Soma de dois números
#Objetivo: Aplicar o algoritmo visto em aula 
# Leia dois números → Some os dois números → Mostre o resultado em código Python.
  
#O que é input()?
#input() é uma FUNÇÃO como print(), ela serve para a pedir para a pessoa do outro lado botar alguma informação (Pense como pedem para dar Login, é o input do usuario e senha)

#O que é esse INT? são tipos de Data de números, Int (integer) é para números inteiros(1,2,3,4,5), enquanto Float é para números quebrados (0.5,  3.4,  5.4 etc) 
#Se eu não botasse esse int, o número seria salvo como uma STRING, e em vez de 2 + 2 ser igual a 4, seria igual a 22 (porque juntou os dois numeros)

#Nas Variaveis de antes, elas salvaram uma STRING, mas nessa como você pode ver, por causa do Int, eu salvei como Números em vez de palavras
Numero1 = int(input("Insira o primeiro numero"))
Numero2 = int(input("Insira o segundo número"))


#Você quer manter suas linhas o mais curtas possiveis, por isso em vez de eu fazer print(Numero1 + Numero2), eu criei uma OUTRA linha para fazer a variavel soma, e depois chamar essa
#variavel pro print, é meio confuso de inicio mas basicamente, mantenha suas linhas curtas e faceis de ler
somaQ4 = Numero1 + Numero2 
print(somaQ4)

#Exercicio 5
#honestamente não tem muito o que explicar nessa, só que / e * servem para divisão e multiplicação, ah e em codigo (fora de string e comentarios) evite usar caracteres diferentes como acentos e ç
#Python foi pensando em inglês, então ter acentos em variaveis e etc pode dar erros

num1 = 8 
num2 = 4
soma = num1 + num2
subtracao = num1 - num2 
divisao = num1 / num2
multiplicacao = num1 * num2
#Ah e se quiser botar pra chamar uma FUNÇÃO depois de uma STRING, bote uma virgula e dê um espaço (o espaço não é necessario mas é bom para ficar facil de ler)
print("A soma dos numeros é igual a ", soma)
print("A subtração dos numeros é igual a ", subtracao)
print("A divisao dos números é igual a ", divisao)
print("A multiplicação dos números é igual a ", multiplicacao)