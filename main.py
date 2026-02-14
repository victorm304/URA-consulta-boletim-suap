#!/var/lib/asterisk/agi-bin/URA-consulta-boletim-suap/.venv/bin/python3

from asterisk.agi import *
from src.utils.utils import *
from src.utils.errors import *
from src.ivr.controller import UraController
from src.tts.client import text_to_speech
from src.config import load_config_ini
from src.stt.client import speech_to_text

config = load_config_ini()

TTS_URL = config.tts_url
STS_URL = config.sts_url

TTS_VOICE = config.tts_voice

SUAP_USER_AGENT = config.suap_user_agent


def main():
     agi = None
     controller = None
     try:
          agi = AGI()
          controller = UraController(agi)
 
          agi.answer()
          controller.home_menu()

          while True:
               matricula = controller.ask_matricula()
               access_code_method = controller.get_access_code_method()
               try:
                    if access_code_method == "1":
                         access_code = controller.obtain_access_code_by_digit()
                    
                    elif access_code_method == "2":
                         audio = controller.obtain_access_code_by_audio()
                         res = speech_to_text(url=STS_URL, path=audio)
                         
                         text = (res["result"]["text"].split(".")[0] or "").strip().lower()
                         if not text:
                              raise FalhaAoObterToken("Falha na transcrição")

                         access_code = text

                    
                    controller.play_sound("boletim", "realizando_consulta")
                    year, period, boletim = suap_get_boletim(matricula=matricula, access_code=access_code) 
                    break
                    
               except FalhaAoObterToken as e:
                    agi.verbose(f"Ocorreu um erro: {e}")
                    
                    continuar = controller.try_again_choice()              
                    if continuar == "1": continue
                    else:
                         agi.hangup() 
                         break

               except ConnectionError as e:
                    agi.verbose(f"Ocorreu um erro: {e}")
                    controller.play_sound("erros/falha_suap", "1")
                    agi.hangup()
                    break
          
            
          text_boletim = format_boletim(year, period, boletim)
          boletim_audio_wav = text_to_speech(
               url=TTS_URL,
               text=text_boletim,
               voice_type=TTS_VOICE
          )

          boletim_audio_gsm = wav_to_gsm_8k(boletim_audio_wav)
          remove_audio(boletim_audio_wav)

          controller.play_boletim_audio(boletim_audio_gsm.split(".gsm")[0])
          remove_audio(boletim_audio_gsm)


     except Exception as e:
          agi.verbose(f"Erro: {e}")
          controller.play_sound("erro_interno", "erro_interno")
     finally:
          agi.hangup()


if __name__ == "__main__":
    main()
