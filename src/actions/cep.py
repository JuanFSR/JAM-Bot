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
        message = 'Rua: ' + str(response['logradouro']) + ', bairro: ' + str(response['bairro']) + ', ' + str(response['localidade']) + ' ' + str(response['uf'])
  
        dispatcher.utter_message(text=message)

        return []
