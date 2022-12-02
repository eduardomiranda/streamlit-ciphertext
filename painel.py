import streamlit as st
import pandas as pd


key = st.secrets["key"]
n = st.secrets["n"]



def encrypt(plaintext):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext:
        try:
            i = (key.index(l) + n) % len(key)
            result += key[i]
        except ValueError:
            result += l

    return result


def decrypt(ciphertext):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % len(key)
            result += key[i]
        except ValueError:
            result += l

    return result




if __name__ == "__main__":

	st.title("Ciphertext")

	operacoes = ("Criptografar", "Descriptografar")
	operacao = st.radio("Escolha a operação.", operacoes )

	textos = st.text_area('Strings')

	if st.button('Processar'):

		data = {'Original': [], 'Processado': []}

		for texto in textos.split('\n'):

			processado = None

			if operacao == operacoes[0]:
				processado = encrypt( texto )
			elif operacao == operacoes[1]:
				processado = decrypt( texto )

			data['Original'].append(texto)
			data['Processado'].append(processado)

		st.table( pd.DataFrame.from_dict(data) )


