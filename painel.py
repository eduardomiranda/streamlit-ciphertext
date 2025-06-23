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

	st.title("🔐 Ciphertext")

	chave_default = st.checkbox("Utilizar valor chave default?", value=True)

	if not chave_default:
		col11, col12, col3 = st.columns(3)
		with col11:
			n = st.number_input('Insira o valor da chave (n)', value=123, step=1)


	options = ["Criptografar", "Descriptografar"]
	default = options[1]
	operacao = st.pills("", options=options, selection_mode="single", default=default)


	textos = st.text_area('Strings')

	if st.button('Processar'):

		data = {'Original': [], 'Processado': []}

		for texto in textos.split('\n'):

			processado = None

			if operacao == options[0]:
				processado = encrypt( texto )
			elif operacao == options[1]:
				processado = decrypt( texto )

			data['Original'].append(texto)
			data['Processado'].append(processado)

		st.table( pd.DataFrame.from_dict(data) )


