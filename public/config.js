// Equivalente ao antigo secrets.toml do Streamlit.
// ATENÇÃO: em um site estático este arquivo é público — qualquer visitante pode lê-lo.
window.CIPHER_CONFIG = {
  key: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",  // alfabeto da cifra (mesmo valor de st.secrets["key"])
  n: 1012,  // deslocamento default (mesmo valor de st.secrets["n"])
};
