import uuid
from time import sleep
from pathlib import Path

SOUNDS_DIR = Path(__file__).resolve().parent / "../../sounds"

class AgiIO:
    def __init__(self, agi: object, sounds_dir: str = SOUNDS_DIR):
        self.agi = agi
        self.sounds_dir = sounds_dir
    
    # Audio
    def play_sound(self, subdir, file_name):
        path = self.sounds_dir / subdir / file_name
        self.agi.stream_file(str(path))

    def play_prompts(self, subdir: str, prompts, valid_digits: list):
        for sound, pause in prompts:
            self.play_sound(subdir, sound)
            sleep(pause)

        if valid_digits:
            choice = ""
            while choice not in valid_digits:
                choice = self.agi.wait_for_digit()

            return choice
    
    def get_digits(self, timeout_ms: int, max_digits: int, beep: str = "beep") -> str:
        return self.agi.get_data(beep, timeout=timeout_ms, max_digits=max_digits) or ""

    # Gravação
    def record_wav(self):
        path = f"/tmp/rec_{uuid.uuid4()}"
        self.agi.record_file(path, "wav", 10000)
        return path + ".wav"
    
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

    def play_boletim_audio(self, path: str):
        while True:
            self.agi.stream_file(path)
            
            audio = SOUNDS_DIR / "boletim" / "opcoes"
            digit = self.agi.stream_file(audio, "12")

            if not digit:
                digit = self.agi.wait_for_digit(180000)

            if digit == "2":
                return

            elif digit == "1":
                continue

            else:
                return

    def decode_access_code_from_dtmf(self, raw: str, sep: str = "*"):
        # exemplo: "2*22*7777" => "2AR"
        parts = raw.split(sep) if raw else []
        out = []
        for p in parts:
            if len(p) > 1:
                out.append(self._decode_t9(p))
            else:
                out.append(p)
        
        return "".join(out).lower()

