# 🧠 URA-consulta-boletim-suap

O sistema de **Resposta Audível Interativa (URA/IVR)** é uma aplicação desenvolvida para fornecer uma plataforma de telefonia automatizada que permite aos usuários interagir com serviços acadêmicos por telefone.

O sistema utiliza o **Asterisk**, um framework open-source amplamente usado em telefonia, para gerenciar chamadas e oferecer uma interface de navegação por menus de voz.

As principais funcionalidades incluem captura de entrada do usuário, reprodução de áudios e integração com APIs externas para consulta de dados.

---

## 🚀 Funcionalidades

- Gerenciamento de chamadas recebidas com navegação por menus  
- Reprodução de arquivos de áudio para instruções e respostas  
- Integração com APIs externas para consulta e processamento de dados  
- Tratamento e validação de entradas do usuário  
- Sistema de gerenciamento de configurações da aplicação  
- Funções utilitárias para formatação de dados e operações no sistema  
- Tratamento personalizado de exceções relacionadas a tokens  

---

## 🛠️ Tecnologias Utilizadas

- **Frontend:** Não possui (aplicação via telefonia)  
- **Backend:** Python 3.x  
- **Banco de Dados:** Não possui (usa APIs externas)  
- **IA:** Integração com SUAP (dados acadêmicos)  

### Bibliotecas e Frameworks

- `asterisk.agi` – Integração com Asterisk  
- `configparser` – Gerenciamento de configurações  
- `pathlib` – Operações de sistema de arquivos  
- `subprocess` – Execução de comandos externos  
- `os` – Interação com sistema operacional  
- `SuapClient` – Integração com API do SUAP  

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/victorm304/URA-consulta-boletim-suap.git
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o arquivo:

```
app.conf
```

4. Execute a aplicação:

```bash
python main.py
```

---

## 💻 Uso

1. Ligue para o número associado ao servidor Asterisk  
2. Siga as instruções de voz do sistema  
3. Insira as informações solicitadas via teclado do telefone  
4. O sistema consultará os dados e responderá por áudio  

---

## 📂 Estrutura do Projeto

```plaintext
.
├── main.py
├── src
│   ├── config.py
│   ├── ivr
│   │   ├── controller.py
│   │   └── io.py
│   └── utils
│       ├── errors.py
│       └── utils.py
├── app.conf
└── requirements.txt
```

---

## 📌 Observações

Este projeto foi desenvolvido como parte de um **Projeto Integrador do curso de Redes de Computadores do IFRN**, com foco em acessibilidade e automação de atendimento acadêmico.

---

## 👥 Autores

- Jéssica Caroline da Silva  
- Matheus da Silva Mendes  
- Victor Matheus Machado Silva  
- William Santanna de Araújo  

---

## 📜 Licença

Este projeto é open-source e pode ser utilizado para fins acadêmicos e educacionais.
