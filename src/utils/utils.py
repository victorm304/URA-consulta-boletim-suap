import subprocess
import os

def format_boletim(boletim: dict):
    text = []
    for i in boletim['results']:
        disciplina = i.get('disciplina').split("TEC")[1]
        text.append(f"Disciplina: {disciplina},")
        text.append(f"Media Final: {i.get('media_final_disciplina')},")
        text.append(f"Situação: {i.get('situacao')},")
    
    return ''.join(text)

def run_cmd(command):
    subprocess.run(command, check=True)

def wav_to_gsm_8k(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo: {path} não existe.")
    try:
        fname = os.path.splitext(os.path.basename(path))[0]
        out_dir = os.path.dirname(os.path.abspath(path))
        
        output_path = os.path.join(out_dir, fname + ".gsm")    
        cmd = [ 
            "sox", 
            path, 
            "-r", "8000", 
            "-c", "1",
            #"-t", "gsm", 
            output_path
        ]
        
        run_cmd(cmd)

        return output_path

    except subprocess.CalledProcessError as e:
        raise Exception(f"Sox falhou: {e}")