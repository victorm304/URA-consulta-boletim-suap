#!/var/lib/asterisk/agi-bin/Voip-pesquisa-telefonia/.venv/bin/python3

from asterisk.agi import *
from suap.client import SuapClient
from utils.utils import *
from agi.handler import AgiHandler
from tts.client import text_to_speech
from config import load_config_ini
from sts.client import speech_to_text
import os

config = load_config_ini()

TTS_URL = config.tts_url
STS_URL = config.sts_url

TTS_VOICE = config.tts_voice

SUAP_USER_AGENT = config.suap_user_agent

def main():
   try:
     agi = AGI()
     agi_handler = AgiHandler(agi)
     
     agi.verbose("Inicio.")
     agi.answer()
     
     agi_handler.home_menu()
     matricula = agi_handler.ask_matricula()
     choice = agi_handler.access_code_menu()
     if choice == "1":
          access_code = agi_handler.obtain_access_code_by_digit()
     elif choice == "2":
         audio_path = agi_handler.obtain_access_code_by_audio()
         agi.verbose(f"audio salvo em: {audio_path}")
         res = speech_to_text(url=STS_URL, path=audio_path)
         access_code = res.get("text").lower()
         agi.verbose(f"json: {res}")
         agi.verbose(f"Código recebido: {access_code}")

         try:
          os.remove(audio_path)
         except Exception as e:
             agi.verbose(f"Erro: {e}")
         
     suap = SuapClient(enrolment=matricula, responsible_code= access_code)
     
     req = suap.get_periodos()['results'][0]
     year, period = req.get("ano_letivo"), req.get("periodo_letivo")

     boletim = suap.get_boletim(
          year=year, 
          period=period
     )
     
     text_boletim = format_boletim(boletim)
     
     audio_wav = text_to_speech(
          url=TTS_URL,
          text=text_boletim,
          voice_type=TTS_VOICE,
     )

     audio_gsm = wav_to_gsm_8k(audio_wav)
     os.remove(audio_wav)

     agi.stream_file(audio_gsm.split(".gsm")[0])

     agi.hangup()
     
    
   except Exception as e:
        agi.verbose(f"Erro: {e}")

if __name__ == "__main__":
    main()
