# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class FindCep(Action):

    def name(self) -> Text:
        return "action_find_cep"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        cep = 87300200
        response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
        response = response.json()
  
        
        nome = tracker.get_slot('nome')
        complemento = tracker.get_slot('complemento')
        num_casa = tracker.get_slot('numero_casa')

        message = f'{nome}, você mora na rua {str(response['logradouro'])}, bairro: {str(response['bairro'])}, {str(response['localidade'])} {str(response['uf'])}, numero: {num_casa}, complemento: {complemento}?'
        dispatcher.utter_message(text=message)
        
        return []
