import requests

def speech_to_text(url: str, path: str) -> dict:
    try:
        with open(path, mode="rb") as f:
            r = requests.post(url=url, params={"language": "pt"}, files={"file": f}, timeout=600)
            r.raise_for_status()

        content_type = r.headers.get("content-type")
        if "json" not in content_type:
            raise ValueError(f"Erro no STS, resposta não é aúdio: {content_type}")
        return r.json()

    except requests.exceptions.Timeout:
        raise RuntimeError("Timeout ao conectar ao serviço STS")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Erro de conexão com o serviço STS")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"Erro HTTP {e.response.status_code}: {e.response.text}"
        )
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro inesperado no requests: {e}")
