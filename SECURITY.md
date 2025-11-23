# Security Policy

## 1. Supported Versions
Estas são as versões do projeto que recebem atualizações de segurança:

| Versão | Suportada |
|--------|-----------|
| 1.x    | ✔️ |
| 0.x    | ❌ |

## 2. Reportando Vulnerabilidades
Se você encontrar uma vulnerabilidade, siga este processo:

1. **Não abra um issue público.**
2. Envie um e‑mail diretamente para: **SEU_EMAIL_AQUI**
3. Inclua:
   - Descrição da falha
   - Como reproduzir
   - Possível impacto
   - Log ou prints se possível

Eu respondo normalmente em **ATUALIZE_AQUI (ex: 72h)**.

## 3. Diretrizes de Divulgação
Para proteger usuários:

- Aguarde um patch ser liberado antes de divulgar publicamente.
- Caso a falha seja crítica, o patch será lançado o mais rápido possível.
- Colaboradores que reportarem falhas podem receber **crédito no changelog**, caso desejem.

## 4. Escopo do Programa de Segurança
Ações válidas:

- Testes no ambiente público disponível
- Análise de código aberto (repo)
- Testes de autenticação **somente na sua própria conta**

Proibido:

- Ataques DDoS
- Engenharia social
- Ataques contra terceiros ou infraestrutura externa

## 5. Tipos de Falhas Bem-Vindas
- XSS
- CSRF
- Injeções (SQL/Command/LDAP)
- Autenticação quebrada
- Falhas de autorização
- Exposição de dados sensíveis

## 6. Tipos de Falhas Não Aceitas
- Cookies inseguros sem impacto real
- Bugs do navegador
- Divulgações de stack trace com baixo impacto

