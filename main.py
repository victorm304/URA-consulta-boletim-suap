#!/usr/bin/env python3
from asterisk.agi import *
from src.utils.utils import *
from src.utils.errors import *
from src.ivr.controller import UraController
from src.tts.client import text_to_speech
from src.config import load_config_ini
from src.stt.client import speech_to_text

config = load_config_ini()

TTS_URL = config.tts_url
STT_URL = config.stt_url

STT_API_KEY = config.stt_api_key

TTS_VOICE = config.tts_voice

MAX_TENT = 3

def main():
     agi = None
     controller = None
     try:
          agi = AGI()
          controller = UraController(agi)
 
          agi.answer()
          controller.home_menu()

          tent = 0
          while tent < MAX_TENT:
               tent += 1

               matricula = controller.ask_matricula()
               access_code_method = controller.get_access_code_method()
               try:
                    if access_code_method == "1":
                         access_code = controller.obtain_access_code_by_digit()
                    
                    elif access_code_method == "2":
                         audio = controller.obtain_access_code_by_audio()
                         res = speech_to_text(
                              url=STT_URL, 
                              api_key=STT_API_KEY, 
                              path=audio
                         )
                         remove_file(audio)

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
                    if continuar != "1":
                         return     
                    continue
                    

               except ConnectionError as e:
                    agi.verbose(f"Ocorreu um erro: {e}")
                    controller.play_sound("erros/falha_suap", "1")
                    return
          
          else:
               controller.play_sound("erros", "excedido_lim_tentativas")
               return
     
          def tts(t):
               wav =  text_to_speech(
                    url=TTS_URL,
                    text=t,
                    voice_type=TTS_VOICE
               )
               gsm = wav_to_gsm_8k(wav)
               remove_file(wav)
               return os.path.splitext(gsm)[0]

          tnotas, tfaltas = format_boletim(year, period, boletim)
          audio_notas = tts(tnotas)
          audio_faltas = tts(tfaltas)

          controller.show_boletim(audio_notas, audio_faltas)


     except Exception as e:
          agi.verbose(f"Erro: {e}")
          controller.play_sound("erros", "erro_interno")
     finally:
          agi.hangup()


if __name__ == "__main__":
    main()

