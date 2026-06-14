import requests, json, configparser, json
from datetime import timedelta, datetime
from urllib.parse import urlencode
import http.client

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        pass # Logica de negocio removida por seguranca corporativa

    def __call__(self, r):
        pass # Logica de negocio removida por seguranca corporativa



class IBMApi :
    def __init__(self, id_processo, username, password) :
        pass # Logica de negocio removida por seguranca corporativa


    def headers_api(self) :
        pass # Logica de negocio removida por seguranca corporativa

    
    def headers_api_tenant(self) :
        pass # Logica de negocio removida por seguranca corporativa


    def adicionar_segundos(self, segundos, timestamp = None):
        pass # Logica de negocio removida por seguranca corporativa

    
    def autenticar_api(self,payload) :
        pass # Logica de negocio removida por seguranca corporativa


    def read_ini(self,file,section,parameter) :
        pass # Logica de negocio removida por seguranca corporativa

        
    def register_ini_token(self,access_token,time_to_expire) :
            pass # Logica de negocio removida por seguranca corporativa

    
    def executar_processo(self,token,payload):
        pass # Logica de negocio removida por seguranca corporativa


    def executa_processo_ibm(self, payloadProcesso) :
        pass # Logica de negocio removida por seguranca corporativa


if __name__ == 'main' :

    ibm = IBMApi('fca530ac-8a56-4b0f-8bf5-26463e713c44','Nicolas.nasario@COMPANY_NAME.com.br','COMPANY_NAME')
    payload = "{ 'payload' : { 'usuarioCotefacil' : 'joaovl.COMPANY_NAME' } }"
    ibm.executa_processo_ibm(payload)