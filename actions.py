# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (SlotSet, SessionStarted, ActionExecuted, EventType, ConversationPaused, UserUtteranceReverted)

class ActionFallback(Action):

    def name(self) -> Text:
        return "action_default_fallback"

    # def __init__(self) -> None:
    #     super(ActionFallback, self).__init__("utter_default")

    async def run(
        self,
        output_channel: "OutputChannel",
        nlg: "NaturalLanguageGenerator",
        tracker: "DialogueStateTracker",
        domain: "Domain",
    ) -> List[EventType]:
        # only utter the response if it is available
        evts = await super(ActionFallback, self).run(output_channel, nlg, tracker, domain)

        return evts + [UserUtteranceReverted()]
