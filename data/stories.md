
## unregistered
* greet  
  - utter_greet
  - slot{"is_registered":false}
  - utter_greet_is_eligible

## registered
* greet
  - utter_greet
  - slot{"is_registered":true} 
  - slot{"user_state": []} 
  - utter_bot_offer_help

## first time after registration
* greet
  - utter_greet
  - slot{"is_registered":true} 
  - slot{"user_state": ["first_time_after_registration"]}
  - utter_registration_success

## second time after registration
* greet
  - utter_greet
  - slot{"is_registered":true} 
  - slot{"user_state": ["second_or_more_time_after_registration"]}
  - utter_welcome_regular_user

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## out of scope
* out_of_scope
  - action_default_fallback
