from time import sleep
from .io import AgiIO

class UraController:
    def __init__(self, io: AgiIO):
        self.io = io
    
    def home_menu(self):
        return self.io.play_prompts(
            subdir="inicio",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                #("3", 0)
            ],        
            valid_digits=None
        )

    def get_access_code_method(self):
        return self.io.play_prompts(
            subdir="codigo_responsavel",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                ("3", 0)
            ],
            valid_digits=["1", "2"]  
        )


    def obtain_access_code_by_digit(self):
        self.io.play_prompts(
            subdir="codigo_responsavel/manual",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                ("3", 0.25),
                ("4", 0.25),
                ("5", 0.25)
            ],
            valid_digits=None
        )

        raw = self.io.get_digits(timeout_ms=20000, max_digits=40)
        return self.io.decode_access_code_from_dtmf(raw)

    def try_again_choice(self):
        return self.io.play_prompts(
            subdir="erros/falha_token",
            prompts=[
                ("1", 0.25),
                ("2", 0.25)
            ],
            valid_digits=["1", "2"]
        )

    def ask_matricula(self):
        self.io.play_sound("matricula", "3")
        sleep(0.25)
        return self.io.get_digits(timeout_ms=20000, max_digits=14)


    def obtain_access_code_by_audio(self) -> str:
        return self.io.record_wav()
    
    def play_suap_is_off_audio(self):
        self.io.play_sound("inicio", "1")