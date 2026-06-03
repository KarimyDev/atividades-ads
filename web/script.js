const botaoMenu = document.querySelector(".botao-menu");
const menu = document.querySelector(".links-menu");
const botaoTema = document.querySelector(".botao-tema");
const formulario = document.querySelector("#formulario-contato");
const confirmacao = document.querySelector("#confirmacao");

botaoMenu.addEventListener("click", () => {
  const menuAberto = menu.classList.toggle("aberto");
  botaoMenu.setAttribute("aria-expanded", String(menuAberto));
});

document.querySelectorAll(".links-menu a").forEach((link) => {
  link.addEventListener("click", () => {
    menu.classList.remove("aberto");
    botaoMenu.setAttribute("aria-expanded", "false");
  });
});

// Alterna o tema da página e mantém o texto do botão coerente com o estado atual.
botaoTema.addEventListener("click", () => {
  document.body.classList.toggle("tema-escuro");
  const temaEscuro = document.body.classList.contains("tema-escuro");
  botaoTema.textContent = temaEscuro ? "Tema claro" : "Tema escuro";
});

function mostrarErro(campo, mensagem) {
  document.querySelector(`#erro-${campo}`).textContent = mensagem;
}

function limparErros() {
  ["nome", "email", "mensagem"].forEach((campo) => mostrarErro(campo, ""));
  confirmacao.textContent = "";
}

function emailValido(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

// Valida os campos obrigatórios e simula o envio pedido na atividade.
formulario.addEventListener("submit", (evento) => {
  evento.preventDefault();
  limparErros();

  const nome = formulario.nome.value.trim();
  const email = formulario.email.value.trim();
  const mensagem = formulario.mensagem.value.trim();
  let formularioValido = true;

  if (!nome) {
    mostrarErro("nome", "Informe seu nome.");
    formularioValido = false;
  }

  if (!email) {
    mostrarErro("email", "Informe seu e-mail.");
    formularioValido = false;
  } else if (!emailValido(email)) {
    mostrarErro("email", "Digite um e-mail válido, como nome@dominio.com.");
    formularioValido = false;
  }

  if (!mensagem) {
    mostrarErro("mensagem", "Escreva uma mensagem antes de enviar.");
    formularioValido = false;
  }

  if (formularioValido) {
    formulario.reset();
    confirmacao.textContent = "Mensagem enviada com sucesso!";
  }
});
