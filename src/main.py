%load_ext autoreload
%autoreload 2
import openai

from settings import settings
from openaiapi import OpenaiApi

def main():
    engine_id = 'davinci'
    openaiapi = OpenaiApi()
    text = """
    Emma is very sweet, and now she"""
    res = openaiapi.create_completion(engine_id, text=text, max_tokens=400, temperature=0.2)
    print(res)

if __name__ == "__main__":
    main()