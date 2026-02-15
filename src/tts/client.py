import requests
import tempfile
import os

def text_to_speech(url: str, text: str, voice_type) -> str:
    try:
        headers = {
            "content-type": "application/json",
            "User-Agent": "URA/Consulta de Boletim",
        }

        payload = {
            "input": text,
            "voice": voice_type,
            "response_format": "wav",
            "download_format": "wav",
            "stream": False,
            "speed":1,
            "return_download_link": False,
            "lang_code": "p",
        }

        req = requests.post(
            url=url, 
            headers=headers, 
            json=payload,
            timeout=500
        )

        req.raise_for_status()
        
        content_type = req.headers.get("content-type")
        if "audio" not in content_type:
            raise ValueError(f"Erro no TTS, resposta não é aúdio: {content_type}")

        f = tempfile.NamedTemporaryFile(mode="wb", suffix=".wav", delete=False)
        os.chmod(f.name, 0o600)
        f.write(req.content)
        f.close()

        if os.path.exists(f.name):
            os.chmod(f.name, 0o600)     

        return f.name
        
    except requests.exceptions.Timeout:
        raise RuntimeError("Timeout ao conectar ao serviço TTS")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Erro de conexão com o serviço TTS")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"Erro HTTP {e.response.status_code}: {e.response.text}"
        )
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro inesperado no requests: {e}")
