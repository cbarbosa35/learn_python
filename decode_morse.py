import os
import sys
import pandas as pd
import datetime
from config import file_path, dict_morse

def decode_morse(msg, morse_dict):
    '''
    Decifra uma mensagem em código Morse onde as letras são separadas por espaços e palavras são separadas por dois espaços.
    
    input : mensagem em código morse e dicionário Morse
    output : mensagem em texto claro
    '''
    words = msg.split("  ")
    decoded_words = []
    for word in words:
        letters = word.split(" ")
        decoded_letters = [morse_dict.get(letter, '') for letter in letters]
        decoded_words.append("".join(decoded_letters))
    return " ".join(decoded_words)

def save_clear_msg_csv(decoded_msg, file_path):
    '''
    Salva a mensagem decifrada em um arquivo CSV com cabeçalho e data/hora.
    
    input : mensagem decifrada e caminho do arquivo CSV
    '''
    now = datetime.datetime.now()
    df = pd.DataFrame([[decoded_msg, now]], columns=["mensagem", "datetime"])
    file_exists = os.path.isfile(file_path)
    df.to_csv(file_path, mode="a", index=False, header=not file_exists)
    print(f"Arquivo CSV '{file_path}' atualizado com sucesso.")

if __name__ == "__main__":    
    # Recebe a mensagem em código Morse do argumento de linha de comando
    morse_msg = sys.argv[1]
    
    # Decifra a mensagem e salva no arquivo CSV
    decoded_msg = decode_morse(morse_msg, dict_morse)
    save_clear_msg_csv(decoded_msg, file_path)
    print(f"Mensagem decifrada: {decoded_msg}")


