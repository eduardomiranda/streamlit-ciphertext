const config = window.CIPHER_CONFIG || { key: "", n: 0 };
// Array.from separa por code point, como a iteração de strings em Python
const key = Array.from(config.key);

// Módulo com resultado sempre positivo, como o operador % do Python
const mod = (a, m) => ((a % m) + m) % m;

function shift(text, n) {
  let result = "";
  for (const l of text) {
    const idx = key.indexOf(l);
    result += idx === -1 ? l : key[mod(idx + n, key.length)];
  }
  return result;
}

const encrypt = (plaintext, n) => shift(plaintext, n);
const decrypt = (ciphertext, n) => shift(ciphertext, -n);

const $ = (id) => document.getElementById(id);
const chaveDefault = $("chave-default");
const nField = $("n-field");
const nInput = $("n");
const textos = $("textos");
const resultado = $("resultado");
const tbody = resultado.querySelector("tbody");

if (key.length === 0) $("aviso").hidden = false;

chaveDefault.addEventListener("change", () => {
  nField.hidden = chaveDefault.checked;
});

let operacao = "Descriptografar";
document.querySelectorAll(".pill").forEach((pill) => {
  pill.addEventListener("click", () => {
    document.querySelectorAll(".pill").forEach((p) => p.setAttribute("aria-pressed", "false"));
    pill.setAttribute("aria-pressed", "true");
    operacao = pill.dataset.op;
  });
});

$("processar").addEventListener("click", () => {
  const n = chaveDefault.checked ? Number(config.n) : parseInt(nInput.value, 10) || 0;
  const fn = operacao === "Criptografar" ? encrypt : decrypt;

  tbody.replaceChildren();
  textos.value.split("\n").forEach((texto, i) => {
    const tr = document.createElement("tr");
    for (const valor of [i, texto, fn(texto, n)]) {
      const td = document.createElement("td");
      td.textContent = valor;
      tr.appendChild(td);
    }
    tbody.appendChild(tr);
  });
  resultado.hidden = false;
});
