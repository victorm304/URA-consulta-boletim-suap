# 🧠 URA-consulta-boletim-suap

O **URA-consulta-boletim-suap** é um sistema de Resposta Audível Interativa (URA/IVR) que permite a pais e responsáveis consultarem informações acadêmicas de alunos por meio de chamadas telefônicas.

O sistema integra **Asterisk/Issabel**, a API do **SUAP (IFRN)** e recursos de **síntese e reconhecimento de voz**, permitindo atendimento automatizado sem necessidade de interação humana.

O objetivo do projeto é demonstrar a aplicação de VoIP e automação em serviços educacionais, aumentando a acessibilidade e disponibilidade de informações acadêmicas.

---

## 🚀 Funcionalidades

- Atendimento telefônico automatizado via URA  
- Navegação por menus de voz  
- Consulta de dados acadêmicos via API do SUAP  
- Entrada de dados por DTMF e voz  
- Síntese de voz (TTS) para respostas dinâmicas  
- Tratamento de erros e validação de entradas  
- Sistema de configuração via arquivo `.conf` 

---

## 🛠️ Tecnologias Utilizadas

- **Telefonia:** Asterisk / Issabel PBX  
- **Backend:** Python 3.x  
- **Integração:** API SUAP  
- **Recursos de Voz (IA):**
  - Text-to-Speech (TTS) - Kokoro-82M
  - Speech-to-Text (STT) - Whisper Large V3

<p align="left">
  <img src="https://github.com/user-attachments/assets/bc7a500a-715f-41ec-a9f8-1e2667480368" width="600"/>
</p>

---

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
3. Informe matrícula ou código via teclado ou voz  
4. O sistema consulta o SUAP e retorna por áudio 

---

## 📂 Estrutura do Projeto

```plaintext
.
├── app.conf
├── main.py
├── README.md
├── sounds
│   ├── boletim
│   │   ├── opcoes.gsm
│   │   └── realizando_consulta.gsm
│   ├── codigo_responsavel
│   │   ├── 1.gsm
│   │   ├── 2.gsm
│   │   ├── 3.gsm
│   │   ├── manual
│   │   │   ├── 1.gsm
│   │   │   ├── 2.gsm
│   │   │   ├── 3.gsm
│   │   │   ├── 4.gsm
│   │   │   └── 5.gsm
│   │   └── voz
│   │       ├── 1.gsm
│   │       ├── 1.wav
│   │       ├── 2.gsm
│   │       ├── 2.wav
│   │       ├── 3.gsm
│   │       └── 3.wav
│   ├── erro_interno
│   │   └── erro_interno.gsm
│   ├── erros
│   │   ├── falha_suap
│   │   │   └── 1.gsm
│   │   └── falha_token
│   │       ├── 1.gsm
│   │       └── 2.gsm
│   ├── inicio
│   │   ├── 1.gsm
│   │   ├── 2.gsm
│   │   └── 3.gsm
│   └── matricula
│       ├── 1.gsm
│       └── 3.gsm
└── src
    ├── config.py
    ├── init.py
    ├── ivr
    │   ├── controller.py
    │   ├── init.py
    │   └── io.py
    ├── sts
    │   ├── client.py
    │   └── init.py
    ├── suap
    │   ├── client.py
    │   └── init.py
    ├── tts
    │   ├── client.py
    │   └── init.py
    └── utils
        ├── errors.py
        ├── init.py
        └── utils.py
```

---

## 📌 Observações

Este projeto foi desenvolvido no **Projeto Integrador do curso de Redes de Computadores do IFRN**, com foco em:

- Aplicação de VoIP na educação  
- Automação de atendimento  
- Integração de sistemas  
- Acessibilidade a dados acadêmicos  

---

## 👥 Autores

- Jéssica Caroline da Silva  
- Matheus da Silva Mendes  
- Victor Matheus Machado Silva  
- William Santanna de Araújo  

## 📽️ Vídeo de apresentação

Clique na imagem para assistir:

[![Demo URA SUAP](https://img.youtube.com/vi/AXxk6qbx1ow/0.jpg)](https://youtu.be/AXxk6qbx1ow)


---

## 📜 Licença

Este projeto é open-source e pode ser utilizado para fins acadêmicos e educacionais.
