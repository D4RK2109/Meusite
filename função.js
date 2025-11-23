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

  // Escapa mensagem antes de mostrar no front-end
  output.textContent = escapeHtml(mensagem);

  // Envia os dados para o back-end de forma segura
  fetch('/salvar-dados', {              // rota do back-end
    method: 'POST',                      // método HTTP
    headers: { 'Content-Type': 'application/json' }, // dados em JSON
    body: JSON.stringify({
      email: email,
      mensagem: mensagem
    })
  })
  .then(res => res.json())
  .then(data => {
    if (data.sucesso) {
      alert('Dados enviados e salvos com sucesso!');
    } else {
      alert('Erro ao salvar os dados: ' + (data.erro || 'desconhecido'));
    }
  })
  .catch(err => {
    console.error(err);
    alert('Erro na conexão com o servidor.');
  });
});
