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
        if  (
            len(tracker.events) >= 5
            and tracker.events[-5].get("name") == "action_default_fallback"
        ):            
            dispatcher.utter_message(template="utter_default")

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_iamabot")
        
        return [UserUtteranceReverted()]
