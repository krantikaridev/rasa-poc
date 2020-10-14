## POC demonstrates the following
 1. how to use action_default_fallback to provide different message based on some condition, we wanted the human handover to take place in case the bot is going into fallback message twice in a row
 2. CI/CD: train and upload a model to S3 and rasa-x
 3. Create action Image

## SHELL
docker run  --user $(id -u):$(id -g) -it -v $(pwd):/app --entrypoint rasa rasa/rasa:1.10.15-full shell  --debug
## TRAIN
docker run  --user $(id -u):$(id -g) -it -v $(pwd):/app --entrypoint rasa rasa/rasa:1.10.15-full train  --debug
## ACTION
docker run -v $(pwd):/app rasa/rasa:1.10.15-full run actions --port 5006 --debug

FYI: The actions are disabled and secret keys have been removed as this was a POC, I removed them once everything was verified
