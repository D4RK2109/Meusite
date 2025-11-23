// Função para validar email
function validarEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

// Função para escapar caracteres especiais (prevenir XSS)
function escapeHtml(text) {
  const map = {
    '&': '&amp;',
    '<': '&lt;',
    '>': '&gt;',
    '"': '&quot;',
    "'": '&#039;'
  };
  return text.replace(/[&<>"']/g, function(m) { return map[m]; });
}

// Pegando o form
const form = document.getElementById('meuForm');
const output = document.getElementById('saida');

form.addEventListener('submit', function(e) {
  e.preventDefault(); // impede envio automático

  const email = document.getElementById('email').value;
  const mensagem = document.getElementById('mensagem').value;

  // Validação de email
  if (!validarEmail(email)) {
    alert('Email inválido!');
    return;
  }

  // Escapa mensagem antes de mostrar
  output.textContent = escapeHtml(mensagem);

  alert('Dados validados e seguros!');
});
