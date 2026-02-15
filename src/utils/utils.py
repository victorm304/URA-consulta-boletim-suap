from ..suap.client import SuapClient
import subprocess
import os

def format_boletim(ano: str, periodo: str, boletim: dict):
    text = []
    text.append(f"Boletim de {ano}ponto{periodo}\n\n")
    for d in boletim['results']:
        disciplina = d.get('disciplina')
        
        nota_etapa_1 = d.get('nota_etapa_1')['nota']
        nota_etapa_2 = d.get('nota_etapa_2')['nota']
        nota_etapa_3 = d.get('nota_etapa_3')['nota']
        nota_etapa_4 = d.get('nota_etapa_4')['nota']
        media_disciplina = d.get('media_final_disciplina')
        nota_avaliacao_final = d.get('nota_avaliacao_final')['nota']        
        media_final = d.get('media_final_disciplina')

        total_faltas = d.get('numero_faltas')
        porcentual_carga_horaria_frequentada = int(float(d.get('percentual_carga_horaria_frequentada')))
        situacao = d.get('situacao')

        text.append(f"Disciplina:\n{disciplina},\n")
        if nota_etapa_1:
            text.append(f"Nota da primeira etapa:\n{nota_etapa_1},\n")
        if nota_etapa_1 is None:
            text.append(f"Nota da primeira etapa:\nAinda não publicado,\n")
        if nota_etapa_2:
            text.append(f"Nota da segunda etapa:\n{nota_etapa_2},\n")
        if nota_etapa_2 is None:
            text.append(f"Nota da segunda etapa:\nAinda não publicado,\n")
        if nota_etapa_3:
            text.append(f"Nota da terceira etapa:\n{nota_etapa_3},\n")
        if nota_etapa_4:
            text.append(f"Nota da terceira etapa:\n{nota_etapa_3},\n")
        if media_disciplina:
            text.append(f"Média da Disciplina:\n{media_disciplina},\n")
        if media_disciplina is None:
            text.append(f"Média da Disciplina:\nainda não publicado,\n")
        if nota_avaliacao_final:
            text.append(f"Avaliação Final:\n{nota_avaliacao_final},\n")
        if media_final:
            text.append(f"Média Final:\n{media_final}\n")
        
        text.append(f"Total de Faltas:\n{total_faltas},\n")
        if porcentual_carga_horaria_frequentada is not None:
            text.append(f"Percentual da carga horária frequentada:\n{porcentual_carga_horaria_frequentada}%\n")
        text.append(f"Situação: {situacao},\n\n\n")
    
    return ''.join(text)

def suap_get_boletim(matricula, access_code):
    suap = SuapClient(enrolment=matricula, responsible_code=access_code)
    req = suap.get_periodos()['results'][0]
    year, period = req.get("ano_letivo"), req.get("periodo_letivo")
    boletim = suap.get_boletim(year=year, period=period)
    
    return year, period, boletim

def remove_file(path):
    try:
        os.remove(path)
    except Exception as e:
        print(f"Não foi possivel remover: {e}")

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
