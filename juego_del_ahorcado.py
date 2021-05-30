import os
os.system('clear')

def open_data():
    with open('data.txt', mode = 'r', encoding= 'UTF-8') as a:
        words = [l.replace('\n', '') for l in a]
    return words

def create_word(words):
    from random import randint
    random_word = open_data()[randint(0, len(open_data()))]
    
    words_with_accents = {'á': 'a','é': 'e','í': 'i','ó': 'o','ú': 'u'}
    
    for letter in random_word:
        if letter in words_with_accents:
            new_letter = words_with_accents[letter]
            random_word = random_word.replace(letter, new_letter)

    return random_word

def main():
    #Leo el dataset de palabras
    data = open_data()
    #Genero una palabra aleatoria
    secret_word = create_word(data)
    #Genero un diccionario de letras a partir de la palabra
    dict_word = {}
    discovery_word = {}
    for i in range(len(secret_word)):
        dict_word[i]= secret_word[i]
        discovery_word[i] = '_ '

    print("JUEGO DEL AHORCADO")
    print('La palabra a elegir tiene: '+str(len(secret_word))+ ' letras.')
    while dict_word != discovery_word:
        final_word =''    
        letter = str(input('Por favor ingrese una letra: '))
        if letter not in final_word:
            if not letter.isnumeric():
                print('pasa')
                for w in range(len(dict_word)):
                    if letter == dict_word[w] :
                        print(final_word)
                        discovery_word[w] = letter
                
                for s in range(len(discovery_word)):
                    final_word = final_word+ discovery_word[s]
                os.system('clear')
                print("JUEGO DEL AHORCADO")
                print(final_word)

            else:
                os.system('clear')
                print("No ingrese numeros. Solo letras")
                try:
                    print(final_word)
                except:
                    pass
                print("JUEGO DEL AHORCADO")
                pass
        else:
            os.system('clear')
            print("Letra previamente ingresada")
            try:
                print(final_word)
            except:
                pass
            print("JUEGO DEL AHORCADO")
            pass
    else:
        print("Felicitaciones! Has ganado\nLa palabra es: "+ secret_word)

if __name__ == "__main__":
    main()