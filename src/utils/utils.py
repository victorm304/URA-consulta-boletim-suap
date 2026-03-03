from ..suap.client import SuapClient
import subprocess
import os

def format_boletim(ano: str, periodo: str, boletim: dict):
    results = boletim.get("results") or []
    if not results:
        msg = "Ainda não foi publicado boletim para o período atual."
        return msg, msg

    def get_nota(d: dict, campo: str):
        bloco = d.get(campo)
        if isinstance(bloco, dict):
            return bloco.get("nota")
        return None

    def fmt_valor(v):
        return "Ainda não publicado" if v is None else str(v)

    cabecalho = f"Boletim de {ano} ponto {periodo}: \n\n"

    texto_notas = [cabecalho]
    texto_faltas = [cabecalho]

    for d in results:
        disciplina = d.get("disciplina") or "Sem nome"

        n1 = get_nota(d, "nota_etapa_1")
        n2 = get_nota(d, "nota_etapa_2")
        n3 = get_nota(d, "nota_etapa_3")
        n4 = get_nota(d, "nota_etapa_4")
        media_disciplina = d.get("media_final_disciplina")
        nota_av_final = get_nota(d, "nota_avaliacao_final")
        media_final = d.get("media_final") or d.get("media_final_disciplina")

        faltas = d.get("numero_faltas")
        freq = d.get("percentual_carga_horaria_frequentada")

        try:
            freq_int = int(float(freq)) if freq is not None else None
        except (ValueError, TypeError):
            freq_int = None

        situacao = d.get("situacao") or "—"

        texto_notas.append(f"Disciplina: {disciplina},\n")
        texto_notas.append(f"Nota da Primeira etapa: {fmt_valor(n1)},\n")
        texto_notas.append(f"Nota da Segunda etapa: {fmt_valor(n2)},\n")

        if n3 is not None:
            texto_notas.append(f"Nota da Terceira etapa: {n3},\n")

        if n4 is not None:
            texto_notas.append(f"Nota da Quarta etapa: {n4},\n")

        texto_notas.append(f"Média da disciplina: {fmt_valor(media_disciplina)},\n")
        
        if nota_av_final is not None:
            texto_notas.append(f"Avaliação final: {fmt_valor(nota_av_final)},\n")

        if media_final is not None:
            texto_notas.append(f"Média final: {media_final},\n")

        texto_notas.append("\n")

        texto_faltas.append(f"Disciplina: {disciplina}.\n")
        texto_faltas.append(f"Total de faltas: {fmt_valor(faltas)},\n")

        if freq_int is not None:
            texto_faltas.append(f"Percentual da carga horária frequentada: {freq_int} por cento,\n")

        texto_notas.append(f"Situação: {situacao},\n\n")

    return "".join(texto_notas), "".join(texto_faltas)

def suap_get_boletim(matricula, access_code):
    suap = SuapClient(enrolment=matricula, responsible_code=access_code)
    req = suap.get_periodos()['results'][0]
    year, period = req.get("ano_letivo"), req.get("periodo_letivo")
    boletim = suap.get_boletim(year, period)
    
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
