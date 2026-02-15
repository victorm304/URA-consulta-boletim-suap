import uuid
from time import sleep
from pathlib import Path


SOUNDS_DIR = Path(__file__).resolve().parent / "../../sounds"

class UraController:
    def __init__(self, agi):
        self.agi = agi
        self.sounds_dir = SOUNDS_DIR

    # Audio
    def play_sound(self, subdir, file_name, escape_digit=None):
        path = self.sounds_dir / subdir / file_name
        if escape_digit:
            digit = self.agi.stream_file(path, escape_digit)
            return digit
        
        self.agi.stream_file(path)

    def play_prompts(self, subdir: str, prompts, valid_digits: list, escape_digit=None):
        for sound, pause in prompts:
            if escape_digit:
                digit = self.play_sound(subdir, sound, escape_digit=escape_digit)
                if digit: return digit
            else:
                self.play_sound(subdir, sound)
                sleep(pause)

        if valid_digits:
            choice = ""
            while choice not in valid_digits:
                choice = self.agi.wait_for_digit(timeout=10 * 60 * 1000)

            return choice
    
    def get_digits(self, timeout_ms: int, max_digits: int, beep: str = "beep") -> str:
        return self.agi.get_data(beep, timeout=timeout_ms, max_digits=max_digits) or ""

    # Gravação
    def record_wav(self):
        path = f"/tmp/rec_{uuid.uuid4()}"
        self.agi.record_file(
            path, "wav", 
            timeout=6000, 
            escape_digits="#"
        )

        return path + ".wav"

    def home_menu(self):
        return self.play_prompts(
            subdir="inicio",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                #("3", 0)
            ],        
            valid_digits=None
        )

    def get_access_code_method(self):
        return self.play_prompts(
            subdir="codigo_responsavel",
            prompts=[
                ("1", 0.25),
                ("2", 0.25),
                ("3", 0)
            ],
            valid_digits=["1", "2"],
            escape_digit="12"
        )


    def obtain_access_code_by_digit(self):
        self.play_prompts(
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

        raw = self.get_digits(timeout_ms=10 * 60 * 1000, max_digits=40)
        return self._decode_access_code_from_dtmf(raw)

    def try_again_choice(self):
        return self.play_prompts(
            subdir="erros/falha_token",
            prompts=[
                ("1", 0.25),
                ("2", 0.25)
            ],
            valid_digits=["1", "2"],
            escape_digit="12"
        )

    def play_boletim_audio(self, path: str):
        digit = ""
        while digit != "2":
            self.agi.stream_file(path)
            sleep(0.5)
            digit = self.play_prompts(
                subdir="boletim",
                prompts=[
                    ("opcoes", 0)
                ],
                valid_digits=["1", "2"],
                escape_digit="12"
            )

    def ask_matricula(self):
        self.play_sound("matricula", "3")
        return self.get_digits(timeout_ms=10 * 60 * 1000, max_digits=14)


    def obtain_access_code_by_audio(self) -> str:
        self.play_sound("codigo_responsavel/voz/", "stts")
        f = self.record_wav()
        self.play_sound("codigo_responsavel/voz/", "audio_recebido")
        return f
    
    # T9
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

    def _decode_access_code_from_dtmf(self, raw: str, sep: str = "*"):
        # exemplo: "2*22*7777" => "2AR"
        parts = raw.split(sep) if raw else []
        out = []
        for p in parts:
            if len(p) > 1:
                out.append(self._decode_t9(p))
            else:
                out.append(p)
        
        return "".join(out).lower()
