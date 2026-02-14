import requests
import time

def speech_to_text(url: str, path: str) -> dict:
    try:
        with open(path, mode="rb") as f:
            for _ in range(7):
                r = requests.post(url, params={"language": "pt"}, files={"file": f}, timeout=600)
                r.raise_for_status()
                job_id = r.json().get("job_id")
                status = ""
                
                while status != "finished":
                    r = requests.get(url + "/" + job_id).json()
                    status = r.get("status")
       
                    if r.get("error"):
                        break
                    
                    time.sleep(2)

                if status == "finished":
                    break
                
            return r

    except requests.exceptions.Timeout:
        raise RuntimeError("Timeout ao conectar ao serviço STT")

    except requests.exceptions.ConnectionError:
        raise RuntimeError("Erro de conexão com o serviço STT")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"Erro HTTP {e.response.status_code}: {e.response.text}"
        )
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Erro inesperado no requests: {e}")
