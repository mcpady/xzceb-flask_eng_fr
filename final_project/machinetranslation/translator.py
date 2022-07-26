"""Translate module."""
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator('0gBKP8BttYbq8pbLVySak_iGnkLo2Sz82g4fVsKRo5zW')
language_translator = LanguageTranslatorV3(
version='2018-05-01',
authenticator=authenticator
)

language_translator.set_service_url('https://api.us-east.language-translator.watson.cloud.ibm.com/instances/59e62690-6a27-42a7-b17b-02d8d70184fa')

def englishtofrench(englishtext):
    """ translate english to french """
    translation = language_translator.translate(
    text=englishtext,
    model_id='en-fr').get_result()
    frenchtext = translation['translations'][0]['translation']
    return frenchtext

def frenchtoenglish(frenchtext):
    """ translate french to english """
    translation = language_translator.translate(
    text=frenchtext,
    model_id='fr-en').get_result()
    englishtext = translation['translations'][0]['translation']
    return englishtext
