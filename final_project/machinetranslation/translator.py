"""Translator API and functions"""

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(version='2018-05-01',
                                            authenticator=authenticator)

language_translator.set_service_url(url)

def english_to_french(english_text):
    """translates from english to french"""
    if len(english_text) == 0:
        return ""
    translation = language_translator.translate(text = str(english_text),
                                    model_id='en-fr').get_result()
    translation_json = json.dumps(translation, indent=2, ensure_ascii=False)
    translation_dict = json.loads(translation_json)
    return translation_dict["translations"][0]["translation"]

def french_to_english(french_text):
    """translates from french to english"""
    if len(french_text) == 0:
        return ""
    translation = language_translator.translate(text = str(french_text),
                                                model_id = 'fr-en').get_result()
    translation_json = json.dumps(translation, indent=2, ensure_ascii=False)
    translation_dict = json.loads(translation_json)
    return translation_dict["translations"][0]["translation"]
