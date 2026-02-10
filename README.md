# 🧠 URA-consulta-boletim-suap

Sistema de **Resposta Audível Interativa (URA/IVR)** desenvolvido para permitir que usuários consultem informações acadêmicas por telefone. A aplicação é executada como um script AGI no **Asterisk**, conduzindo o fluxo de chamadas por menus de voz, capturando entradas via DTMF e integrando-se a APIs externas para obtenção e síntese de dados.

---

## 🚀 Funcionalidades

* Navegação por menus de voz no Asterisk
* Reprodução de áudios em formato compatível com Asterisk (GSM/WAV)
* Captura e validação de entradas DTMF
* Integração com APIs externas para:

  * Texto-para-fala (TTS)
  * Fala-para-texto (STS)
  * Consulta de dados acadêmicos (SUAP)
* Gerenciamento de configurações via arquivo `app.conf`
* Tratamento de exceções específicas (ex.: falhas de token/SUAP)

---

## 🛠️ Tecnologias

* **Telefonia:** Asterisk (AGI)
* **Backend:** Python
* **Integrações:**

  * SUAP (dados acadêmicos)
  * Kokoro-FastAPI (TTS)
  * whisper-transcription-api (STS)

---

## 📦 Instalação

1. Clone o repositório:

```bash
git clone https://github.com/victorm304/URA-consulta-boletim-suap.git
cd URA-consulta-boletim-suap
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure o arquivo `app.conf` (URLs das APIs, voz TTS, etc.).

4. Copie o script AGI para o diretório do Asterisk e ajuste permissões (exemplo):

```bash
cp main.py /var/lib/asterisk/agi-bin/URA-consulta-boletim-suap/
chmod +x /var/lib/asterisk/agi-bin/URA-consulta-boletim-suap/main.py
```

5. Configure o plano de discagem do Asterisk para chamar o AGI.

---

## 💻 Uso

1. Ligue para a extensão associada ao serviço no Asterisk.
2. Siga as instruções de voz.
3. Digite as informações solicitadas no teclado do telefone.
4. O sistema consulta as APIs e responde por áudio.

---

## 📂 Estrutura do Projeto

```plaintext
.
├── app.conf
├── main.py
├── README.md
├── sounds/
└── src/
    ├── config.py
    ├── ivr/
    ├── sts/
    ├── suap/
    ├── tts/
    └── utils/
```

*(Estrutura completa disponível no repositório.)*

---

## 🔧 Dependências (requisitos mínimos)

* **Python 3.6+**
* `requests`
* `pyst2`
* Asterisk com suporte a AGI

### APIs obrigatórias

Para funcionamento completo do projeto, é necessário executar previamente:

* **Kokoro-FastAPI (TTS):**
  [https://github.com/remsky/Kokoro-FastAPI](https://github.com/remsky/Kokoro-FastAPI)

* **whisper-transcription-api (STS):**
  [https://github.com/victorm304/whisper-transcription-api](https://github.com/victorm304/whisper-transcription-api)

As URLs dessas APIs devem ser configuradas em `app.conf`.

---

## 📌 Observações

Projeto desenvolvido como parte do **Projeto Integrador do curso de Redes de Computadores do IFRN**, com foco em acessibilidade e automação de atendimento acadêmico.

---

## 👥 Autores

* Jéssica Caroline da Silva
* Matheus da Silva Mendes
* Victor Matheus Machado Silva
* William Santanna de Araújo

---

## 📜 Licença

Este projeto é **open-source** e pode ser utilizado para fins **acadêmicos e educacionais**.
