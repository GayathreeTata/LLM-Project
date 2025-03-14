# -*- coding: utf-8 -*-
"""LLM PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16ep35sZobZg_3G-gq94tONX6YyF_ZlsU
"""

import requests

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
HEADERS = {"Authorization": "Bearer Your_hugging_face key"}

def query_llm(prompt):
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=HEADERS, json=data)
    return response.json()

# Example usage
prompt = "What is Artificial Intelligence?" #Write your query
response = query_llm(prompt)

print(response)