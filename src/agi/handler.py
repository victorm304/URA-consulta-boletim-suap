import os
import uuid
from time import sleep
from pathlib import Path

SOUNDS_DIR = Path(__file__).resolve().parent / "../../sounds"

class AgiHandler:
    def __init__(self, agi: object):
        self.agi = agi
    
    def _menu(self, subdir: str, prompts: dict, valid_digits: list):
        for sound, pause in prompts:
            self._play_sound(subdir, sound)
            sleep(pause)

        if valid_digits:
            choice = ""
            while choice not in valid_digits:
                choice = self.agi.wait_for_digit()

            return choice
    
    def home_menu(self):
        return self._menu(
            subdir="inicio",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                ("3", 0)
            ],        
            valid_digits=["1", "2"]
        )

    def access_code_menu(self):
        return self._menu(
            subdir="codigo_responsavel",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                ("3", 0)
            ],
            valid_digits=["1", "2"]  
        )

    def ask_matricula(self):
        subdir = "matricula"
        self._play_sound(subdir, "1")
        sleep(0.25)

        matricula = self.agi.get_data("beep", timeout=20000, max_digits=14)
        self.agi.verbose(matricula)
        return matricula


    def obtain_access_code_by_digit(self):
        self._menu(
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

        digits = self.agi.get_data("beep", timeout=20000, max_digits=40)
        access_code = ""
        for i in digits.split("*"):
            if len(i) > 1:
                access_code += self._decode_t9(i)
            else:
                access_code += i
        
        return access_code.lower()

    def obtain_access_code_by_audio(self):
        path = f"/tmp/rec_{uuid.uuid4()}"
        self.agi.record_file(path, "wav", 10000)
        return path + ".wav"


    def _play_sound(self, subdir, file_name):
        self.agi.stream_file(os.path.join(SOUNDS_DIR, subdir, file_name))


    def _decode_t9(self, seq):
        mapping = {
            "22": "A",  "222": "B",  "2222": "C",
            "33": "D",  "333": "E",  "3333": "F",
            "44": "G",  "444": "H",  "4444": "I",
            "55": "J",  "555": "K",  "5555": "L",
            "66": "M",  "666": "N",  "6666": "O",
            "77": "P",  "777": "Q",  "7777": "R",  "77777": "S",
            "88": "T",  "888": "U",  "8888": "V",
            "99": "W",  "999": "X",  "9999": "Y",  "99999": "Z",
        }

        return mapping.get(seq, "?")
