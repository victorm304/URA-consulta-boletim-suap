# 🧠 URA-consulta-boletim-suap

O **URA-consulta-boletim-suap** é um sistema de Resposta Audível Interativa (URA/IVR) que permite a consulta informações acadêmicas de alunos por meio de chamadas telefônicas.

O sistema integra **Asterisk/Issabel**, a API do **SUAP (IFRN)** e recursos de **síntese e reconhecimento de voz**, permitindo atendimento automatizado sem necessidade de interação humana.

O objetivo do projeto é demonstrar a aplicação de VoIP e automação em serviços educacionais, aumentando a acessibilidade e disponibilidade de informações acadêmicas.

---

## 🚀 Funcionalidades

* Atendimento telefônico automatizado via URA
* Navegação por menus de voz
* Consulta de dados acadêmicos via API do SUAP
* Entrada de dados por DTMF e voz
* Síntese de voz (TTS) para respostas dinâmicas
* Tratamento de erros e validação de entradas
* Sistema de configuração via arquivo `.conf`

---

## 🛠️ Tecnologias Utilizadas

* **Telefonia:** Asterisk / Issabel PBX
* **Integração:** API SUAP
* **Recursos de Voz (IA):**

  * **Text-to-Speech (TTS):** Kokoro-82M
  * **Speech-to-Text (STT):** Whisper Large V3

<p align="left">
  <img src="https://github.com/user-attachments/assets/bc7a500a-715f-41ec-a9f8-1e2667480368" width="600"/>
</p>

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

4. Copie **todo o diretório do projeto** para o diretório de scripts AGI do Asterisk e ajuste permissões (exemplo):

```bash
cp -r URA-consulta-boletim-suap /var/lib/asterisk/agi-bin/
chown -R asterisk:asterisk /var/lib/asterisk/agi-bin/URA-consulta-boletim-suap
chmod -R 755 /var/lib/asterisk/agi-bin/URA-consulta-boletim-suap
```

5. Configure o plano de discagem do Asterisk para chamar o AGI (exemplos abaixo).

---

## 💻 Uso

1. Ligue para o número associado ao servidor Asterisk
2. Siga as instruções de voz do sistema
3. Informe matrícula ou código via teclado ou voz
4. O sistema consulta o SUAP e retorna por áudio

---

## 📞 Configuração no Asterisk (Dialplan)

### Exemplo (modelo)

Em **extensions_custom.conf** (ou no contexto adequado ao seu ambiente):

```ini
[teste]
exten => xxxx,1,NoOp(inicio)
 same => n,AGI(/var/lib/asterisk/agi-bin/URA-consulta-boletim-suap/main.py)
```

> Substitua `xxxx` pelo número da extensão que você deseja utilizar no seu plano de discagem.

---

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

* **whisper-transcription-api (STT):**
  [https://github.com/victorm304/whisper-transcription-api](https://github.com/victorm304/whisper-transcription-api)

As URLs dessas APIs devem ser configuradas em `app.conf`.

---

## 📌 Observações

Este projeto foi desenvolvido no **Projeto Integrador do curso de Redes de Computadores do IFRN**, com foco em:

* Aplicação de VoIP na educação
* Automação de atendimento
* Integração de sistemas
* Acessibilidade a dados acadêmicos

---

## 👥 Autores

* Jéssica Caroline da Silva
* Matheus da Silva Mendes
* Victor Matheus Machado Silva
* William Santanna de Araújo

## 📽️ Vídeo de apresentação

Clique na imagem para assistir:

[![Demo URA SUAP](https://img.youtube.com/vi/AXxk6qbx1ow/0.jpg)](https://youtu.be/AXxk6qbx1ow)

---

## 📜 Licença

Este projeto é **open-source** e pode ser utilizado para fins **acadêmicos e educacionais**.
