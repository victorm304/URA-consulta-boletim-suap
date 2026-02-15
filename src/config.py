import configparser
from pathlib import Path


class AppConfig(object):
    def __init__(
        self,
        tts_url,
        tts_voice,
        stt_url,
        suap_user_agent
    ):
        self.tts_url = tts_url
        self.tts_voice = tts_voice
        self.stt_url = stt_url
        self.suap_user_agent = suap_user_agent


def load_config_ini(path=None):
    default_path = Path(__file__).resolve().parent / "../app.conf"
    p = Path(path) if path else default_path

    cp = configparser.ConfigParser()

    if p.exists():
        cp.read(str(p), encoding="utf-8")

    return AppConfig(
        tts_url=cp.get("tts", "url", fallback=""),
        tts_voice=cp.get("tts", "voice", fallback=""),
        stt_url=cp.get("stt", "url", fallback=""),
        suap_user_agent=cp.get("suap", "user_agent", fallback="")
    )
