'''
Projeto - Jogo Das Perguntas
Desenvolvedor - Nickolas Kinceski Martins
2025.06.30
'''

from modules import limpaTela, mostraCabecalho, mostraMenu, playAgain, getValue, validaValue # Importa funçõs o arquivo modules.py

# VARIÁVEIS
escolha = '' # Variavel das escolhar
acertos = 0 # Define a variavel acertos como 0

# LISTAS
msgCab = ['Jogo das Perguntas', 'Desenvolvedor: Nickolas Kinceski Martins', '2025.06.30'] # Mostra a msg do Cabeçalho
msgMenu = ['Enter - Jogar', "Caso queira sair do jogo clique na tecla '0'",
            "para sair a qualuqer momento"] # Mostra a msg do Menu

# PERGUNTAS E RESPOSTAS
perguntas = [
    {
        "pergunta": "Qual é a capital da França?", # Pergunta feita
        "opcoes": ["1 - Paris", "2 - Londres"], # Opções de resposta
        "correta": 1,
        "resposta_correta": "Paris" # Reposta correta
    },
    {
        "pergunta": "Qual o lugar mais profundo dos oceanos?", # Pergunta feita
        "opcoes": ["1 - Fossa de Java", "2 - Fossa das Marianas"], # Opções de resposta
        "correta": 2,
        "resposta_correta": "Fossa das Marianas" # Reposta correta
    },
    {
        "pergunta": "Quais as cores primárias?", # Pergunta feita
        "opcoes": ["1 - Vermelho, Azul, Verde", "2 - Vermelho, Amarelo, Azul"], # Opções de resposta
        "correta": 2,
        "resposta_correta": "Vermelho, Amarelo, Azul" # Reposta correta
    },
    {
        "pergunta": "Qual o país mais novo do mundo?", # Pergunta feita
        "opcoes": ["1 - Sudão do Sul", "2 - Alemanha"], # Opções de resposta
        "correta": 1,
        "resposta_correta": "Sudão do Sul" # Reposta correta
    },
    {
        "pergunta": "Quem foi a primeira mulher a viajar para o espaço?", # Pergunta feita
        "opcoes": ["1 - Sally Ride", "2 - Valentina Tereshkova"], # Opções de resposta
        "correta": 2,
        "resposta_correta": "Valentina Tereshkova" # Reposta correta
    }
]

def jogar(): # Bloco que define o jogo
    global acertos # Zera os acertos
    acertos = 0
    limpaTela() # Limpa a tela para mostrar o Cabeçalho
    mostraCabecalho(msgCab) # Mostra o Cabeçalho
    mostraMenu(msgMenu) # Mostra o Menu do jogo
    input("Pressione Enter para começar o jogo...") # Para iniciar o jogo o jogador deve precionar a tecla "Enter"

    for q in perguntas: # Inicia as 5 peguntas, mostra cada pergunta e suas opçoes
        print("\n" + q["pergunta"]) # Mostra as perguntas
        for opcao in q["opcoes"]: # Mostra as opções de resposta
            print(opcao)
        while True:
            try:
                resp = int(input("Digite o número da resposta: ")) # Pede a reposta do jogador
                if resp == 0: 
                    print("Você escolheu sair do jogo") # Se a tecla 0 for clicada, o jogador sai do jogo
                    return # Sai da função jogar()
                if resp in [1, 2]:
                    break
                else:
                    print("Digite 0 para sair do jogo a qualquer momento.")
            except ValueError:
                print("Digite um número válido (1 ou 2).")
        if resp == q["correta"]: # Verifica se a resposta está correta
            acertos += 1 # Soma um acerto
            print("Resposta correta!") # Confirma o acerto do jagador
        else:
            print(f"Resposta incorreta! A resposta correta é {q['resposta_correta']}.") # Se o jagor errou, mostra a resposta correta

    print(f"\nVocê acertou {acertos} perguntas!") # Mostra quantos acerto o jogador fez
    print('Obrigado por jogar!') # Agradecimento por jogar
    print('Deseja jogar novamente?') # Pergunta se o jogador deseja jogar novamente
    playAgain()
if __name__ == "__main__":
    jogar()