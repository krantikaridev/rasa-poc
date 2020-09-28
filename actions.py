# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List, Optional, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (SlotSet, SessionStarted, ActionExecuted, EventType, ConversationPaused, UserUtteranceReverted)
import logging
logger = logging.getLogger(__name__)
from random import seed
from random import randint

class ActionFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    # def __init__(self):
    #     super(ActionFallback, self).__init__("utter_default", silent_fail=True)

    # https://github.com/RasaHQ/rasa-demo/blob/master/actions/actions.py
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        
        # only utter the template if it is available
        seed(1)
        number_of_fallback= randint(0, 100)
        logger.debug("Hit fall back.")
        logger.info(f"number_of_fallback:{number_of_fallback}")
        if number_of_fallback%2==1:

            dispatcher.utter_message(template="utter_iamabot")

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_default")
        
        return [UserUtteranceReverted()]
