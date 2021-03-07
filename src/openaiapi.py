import requests
from requests.auth import HTTPBasicAuth
import logging
from dataclasses import dataclass
from typing import Dict, List
import jmespath

from settings import openaisettings

log = logging.getLogger(__name__)

class OpenaiApi():
    def __init__(self):
        self.version = 'v1'
        self.openai_base_url = openaisettings.OPENAI_BASE_URL
        self.api_key = openaisettings.OPENAI_API_KEY
        self.org_id = openaisettings.OPENAI_ORG_ID

    def list_engines(self):
        res = self.get(edge='engines')
        engines = res['data']
        return engines

    def get_engine_id(self, name: str=None):
        engines = self.list_engines()
        engine_ids = jmespath.search("[?ready].id", engines)
        if name:
            assert name in engine_ids, "name is not in available ids"
            engine_id = name
        else:
            engine_id = engine_ids[0]
        return engine_id

    def retrieve_engine(self, engine_id: str):
        res = self.get(edge=f'engines/{engine_id}')

        return res

    def create_completion(self, engine_id: str='davinci', text=str, max_tokens: str=30, temperature: float=0.5):
        body = {'prompt': text, "max_tokens": max_tokens, "temperature": temperature}
        res = self.post(edge=f"engines/{engine_id}/completions", body=body)
        choice_res = jmespath.search('choices[?index == `0`].text', res)[0]
        return text + choice_res

    #@dataclass
    #class TokenResponse:
    #    access_token: str
    #    expires: datetime

    def oauth_get_access_token(self):
        raise NotImplementedError()

    def get(self, edge: str):
        api_key = self.api_key.get_secret_value()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(api_key),
        }
        url = f"{self.openai_base_url}/{self.version}/{edge}"
        res = requests.get(
            url, headers=headers
        )
        res.raise_for_status()

        return res.json()

    def post(self, edge: str, body: dict):
        api_key = self.api_key.get_secret_value()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(api_key),
        }
        url = f"{self.openai_base_url}/{self.version}/{edge}"
        res = requests.post(
            url, headers=headers, json=body
        )
        res.raise_for_status()

        return res.json()

if __name__ == '__main__':
    self = AcousticApi()
    res = self.get(version='v1', edge='application')
    res = self.segments()

    openai.list_engines()


import openai
openai.organization = openaisettings.OPENAI_ORG_ID.get_secret_value()
openai.api_key = openaisettings.OPENAI_API_KEY.get_secret_value()
openai.Engine.list()