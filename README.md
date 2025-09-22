# 🖥️ Gerenciamento de Clientes com Django

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-5.2.6-006400)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-brightgreen)

## 📌 Sobre o Projeto
Este projeto é um sistema simples de gerenciamento de clientes desenvolvido com Django. Permite que usuários se registrem, façam login e gerenciem seus próprios clientes com funcionalidades completas de CRUD (Criar, Ler, Atualizar e Deletar). O sistema garante que cada usuário veja e manipule apenas seus próprios dados, com controle de acesso e autenticação.

---

## 🚀 Funcionalidades
- **Cadastro e autenticação de usuários:** Registro, login e logout.
- **CRUD completo de clientes:** Criar, listar, editar e deletar clientes.
- **Controle de acesso:** Cada usuário gerencia apenas seus clientes.
- **Validação de dados:** Campos obrigatórios e unicidade de email por usuário.
- **Interface responsiva:** Utiliza Bootstrap para melhor experiência visual.

---

## 🛠 Tecnologias Utilizadas
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/) para estilização da interface

---

## ▶️ Como executar

1. Clone o repositório:
```bash
git clone https://github.com/Gabriel4002/crud-django.git
cd crud-django/crud_cliente
```

2. Crie e ative um ambiente virtual (recomendado):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r ../requirements.txt
```

4. Execute as migrações do banco de dados:
```bash
python manage.py migrate
```

5. Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

6. Acesse no navegador:
```bash
http://127.0.0.1:8000/
```

7. Registre um usuário, faça login e comece a gerenciar seus clientes.

---

## 📝 Observações

- O sistema utiliza banco SQLite por padrão para facilitar o desenvolvimento.
- As migrações estão versionadas para controle das alterações no banco.
- A interface é simples e pode ser facilmente customizada com Bootstrap.

---

## ✍️ Autor

Gabriel Lobato  
[LinkedIn](https://www.linkedin.com/in/gabriel-lobato-314096371)

---

> Este projeto foi desenvolvido como parte do aprendizado em Django, focando em autenticação, controle de acesso e operações CRUD.
