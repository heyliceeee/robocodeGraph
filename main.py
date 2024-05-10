import matplotlib.pyplot as plt

# Lista para armazenar os dados do arquivo
dados = []

# Abrindo o arquivo e lendo os dados
with open('D:/githubProjects/robocodeIA/bin/sampleRobots/SirKazzio.data/movimentacaoGraph.txt', 'r') as file:
    for linha in file:
        # Removendo quebras de linha e convertendo para inteiro
        dados.append(int(linha.strip()))

# Criando o gráfico de barras
plt.bar(range(1, len(dados) + 1), dados)

# Adicionando rótulos ao gráfico
plt.xlabel('Rondas')
plt.ylabel('Fitness Function')
plt.title('Gráfico de Dados')

# Adicionando os valores exatos como anotações
for i, valor in enumerate(dados):
    plt.text(i + 1, valor, str(valor), ha='center', va='bottom')

# Definindo os rótulos do eixo x
plt.xticks(range(1, len(dados) + 1), [str(i) for i in range(1, len(dados) + 1)])
# Exibindo o gráfico
plt.show()
