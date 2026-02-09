import requests
from ..utils.errors import FalhaAoObterToken

class SuapClient:
    def __init__(self, enrolment, responsible_code):
        self.url = 'https://suap.ifrn.edu.br/'
        self.credentials = {
            'matricula': enrolment,
            'chave': responsible_code   
        }
       
    def get_student_token(self):
        endpoint = '/api/ensino/autenticacao/acesso-responsaveis/'
        url = self.url + endpoint  
        try:
            res = requests.post(
                url= url,
                headers={'accept': 'application/json'},
                params=self.credentials,
                timeout=60 
            )
            res.raise_for_status()
            data = res.json()
            token = data.get('token')
            if not token:
                raise FalhaAoObterToken(f'Resposta sem token: {data}')
            return token 

        except Exception as e:
            raise FalhaAoObterToken('Falha ao obter token:', e)
        
            
    
    def _get_auth(self, endpoint, params=None):
        if not self._check_con():
            raise ConnectionError('Não foi possível estabelecer conexão com a api do suap.')
        
        token = self.get_student_token()
        url = self.url + endpoint

        try:
            res = requests.get(
                url=url,
                headers={'Authorization': f'Bearer {token}'},
                params=params,
                timeout=15
            )
            content_type = res.headers.get('content-type')
            if 'json' not in content_type:
                raise ConnectionError(f'Erro na comunicaçao com api do SUAP, o conteúdo da resposta não é JSON: {content_type}')
            
            res.raise_for_status()
            return res.json()
        
        except requests.RequestException as e:
            raise ConnectionError(f"Falha no GET {endpoint}: {e}")
    
    def get_boletim(self, year, period):
        endpoint = f'/api/ensino/meu-boletim/{year}/{period}/'
        return self._get_auth(endpoint)
    
    def get_periodos(self):
        endpoint = '/api/ensino/meus-periodos-letivos/'
        return self._get_auth(endpoint)

    def _check_con(self):
        try:
            res = requests.get(self.url, timeout=10, stream=True)
            res.raise_for_status()
            return True
        

        except requests.RequestException: 
            return False

