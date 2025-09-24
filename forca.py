import random

def get_word():
    """Escolhe uma palavra aleatória de uma lista."""
    words = ['python', 'programacao', 'desenvolvimento', 'github', 'computador', 'terminal']
    return random.choice(words).upper()

def play_game(word):
    """Lógica principal do jogo."""
    word_completion = ["_" for _ in word]  # Cria a representação da palavra com underlines
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6  # Número de chances para o jogador

    print("--- Bem-vindo ao Jogo da Forca! ---")
    print(display_hangman(tries))
    print(" ".join(word_completion))

    while not guessed and tries > 0:
        guess = input("\nPor favor, adivinhe uma letra ou a palavra: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Você já adivinhou essa letra!")
            elif guess not in word:
                print(f"'{guess}' não está na palavra.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Bom trabalho, '{guess}' está na palavra!")
                guessed_letters.append(guess)
                # Atualiza a palavra para mostrar a letra acertada
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion[i] = guess
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Você já adivinhou essa palavra.")
            elif guess != word:
                print(f"'{guess}' não é a palavra.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = list(word)

        else:
            print("Entrada inválida. Tente uma letra ou a palavra completa.")

        print(display_hangman(tries))
        print(" ".join(word_completion))

    if guessed:
        print("\nParabéns! Você adivinhou a palavra. Você venceu!")
    else:
        print(f"\nVocê perdeu. A palavra era: {word}")

def display_hangman(tries):
    """Desenha a forca de acordo com o número de tentativas."""
    stages = [  # Forca em 7 estágios
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def main():
    """Função principal que inicia e reinicia o jogo."""
    word = get_word()
    play_game(word)
    while input("\nQuer jogar novamente? (S/N) ").upper() == "S":
        word = get_word()
        play_game(word)

if __name__ == "__main__":
    main()