# streamlit-ciphertext



&nbsp;
## Criando o Python Virtual Environment
Necessário apenas um única vez.

```sh
python3  -m  venv  myvenv
```

\
&nbsp;
## Ativando o Virtual Environment
**Necessário toda vez** que for executar o código.

```sh
source  myvenv/bin/activate
```


# Execução do painel Streamlit
```sh
streamlit run painel.py 
```



# Versão estática (Cloudflare Pages)
A pasta `public/` contém a mesma aplicação em HTML + CSS + JavaScript puro, sem backend.

1. Preencha `key` e `n` em `public/config.js` (os mesmos valores do `secrets.toml`).
2. No Cloudflare Pages: *Framework preset* = None, *Build command* vazio, *Build output directory* = `public`.
   Ou via CLI: `npx wrangler pages deploy public`.

Para testar localmente: `python3 -m http.server -d public 8000`.

> Em um site estático, o `config.js` é baixado pelo navegador: a chave fica visível para qualquer visitante.
