linha = '--------------------------------------------------'
# EXERCÍCIOS PRÁTICOS
# 1, lista de convidados
# cria uma lista com nomes de convidadados para uma festa.
# exiba uma mensagem personalizada para cada convidado.
convidados = ['Ana', 'Bruno', 'Carlos', 'Diana']

for convidado in convidados:
    print(f'Olá, {convidado}! Você está convidado para a festa.')
    print(linha)

# saída:
    # Olá, Ana! Você está convidado para a festa.
    # Olá, Bruno! Você está convidado para a festa.
    # Olá, Carlos! Você está convidado para a festa.
    # Olá, Diana! Você está convidado para a festa.

# 2, estatísticas de números
# peça ao usuário para inserir uma lista de números (separados por espaço) e calcule:
# a) o maior número, b) o menor número, c) a soma dos números, d) a média dos números
entrada = input('digite números separados por espaço: ')
numeros = [float(num) for num in entrada.split()]

maior_numero = max(numeros)
menor_numero = min(numeros)
soma_numeros = sum(numeros)
media_numeros = soma_numeros / len(numeros)

print("maior número:", maior_numero)
print("menor número:", menor_numero)
print("soma dos números:", soma_numeros)
print("média dos números:", media_numeros)
print(linha)

# 3, contagem de caracteres em uma string
# peça ao usuário para inserir uma frase e conte quantas vezes cada letra aparece
frase = input("digite uma frase: ").lower()
letras = {}

for caractere in frase:
    if caractere.isalpha():
        if caractere in letras:
            letras[caractere] += 1
        else:
            letras[caractere] = 1
            
for letra, contagem in letras.items():
    print(f"a letra '{letra}' aparece {contagem} vez(es).")
    print(linha)
    
# saída: o programa vai separar separar as letras da frase e mostrar quantas vezes elas aparecem

# 4, ordenando uma lista
# peça ao usuário para inserir uma lista de números,
# (separados por espaço) e exiba a lista em ordem crescente e decrescente.
entrada = input("digite números separados por espaço: ")
numeros = [float(num) for num in entrada.split()]

# ordem crescente
numeros_crescente = sorted(numeros)
print("números em ordem crescente:", numeros_crescente)

# ordem decrescente
numeros_decrescente = sorted(numeros, reverse = True)
print("números em ordem decrescente:", numeros_decrescente)
print(linha)

# 5, trabalhando com tuplas
# crie uma tupla com nomes de meses do ano. 
# peça ao usuário um número entre 1 e 12 e exiba o nome do mês correspondente.
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

numero_mes = int(input("Digite um número entre 1 e 12: "))

if 1 <= numero_mes <= 12:
    print(f"o mês correspondente é {meses[numero_mes - 1]}.")
else:
    print("número inválido. Por favor, digite um número entre 1 e 12.")
    print(linha)

# DESAFIOS EXTRAS
# 1, lista de tarefas
# crie um programa que gerencia uma lista de tarefas. o usuário deve ser capaz de:
# a) adicionar uma tarefa, b) remover uma tarefa, c) listar todas as tarefas
tarefas = []

while True:
    print('\n MENU DE TAREFAS')
    print('1. Adicionar Tarefa')
    print('2. Remover Tarefa')
    print('3. Listar Tarefas')
    print('4. Sair')
    
    opcao = input('escolha uma opção: ')
    
    if opcao == "1":
        tarefa = input("digite a tarefa a ser adicionada: ")
        tarefas.append(tarefa)
        print("tarefa adicionada com sucesso.")
        
    elif opcao == "2":
        tarefa = input("digite a tarefa a ser removida: ")
        if tarefa in tarefas:
            tarefas.remove(tarefa)
            print("tarefa removida com sucesso.")
        else:
            print("tarefa não encontrada.")
    elif opcao == "3":
        print("\n LISTA DE TAREFAS:")
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f"{idx}. {tarefa}")
    elif opcao == "4":
        print("saindo do programa...")
        break
    else:
        print("opção inválida. tente novamente.")
        print(linha)
        
# 2, analisador de notas
# Ccie um programa que recebe as notas dos alunos em uma lista e:
# exibe a maior e a menor nota.
# calcula a média da turma.
# exibe as notas acima da média.
notas = []


while True:
    entrada = input("digite uma nota (ou 'sair' para finalizar): ")
    if entrada.lower() == 'sair':
        break
    else:
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("nota inválida. digite um valor entre 0 e 10.")
        except ValueError:
            print("entrada inválida. Ppr favor, digite um número.")
if notas:
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / len(notas)
    notas_acima_media = [nota for nota in notas if nota > media]
    
    print("\n RESULTADOS:")
    print("maior nota:", maior_nota)
    print("menor nota:", menor_nota)
    print("média da turma:", media)
    print("notas acima da média:", notas_acima_media)
else:
    print("nenhuma nota foi inserida.")
    print(linha)
    
# 3, contando palavras de um texto
# peça ao usuário para inserir um texto e conte quantas vezes cada palavra aparece.
texto = input("digite um texto: ").lower()
palavras = texto.split()
contagem_palavras = {}

for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
        
print("\n contagem de palavras:")
for palavra, contagem in contagem_palavras.items():
    print(f"a palavra '{palavra}' aparece {contagem} vez(es).")


