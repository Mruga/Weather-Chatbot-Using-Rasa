Weather Chatbot Using Rasa

Training the NLU Model

Train the model by running:

rasa train nlu

Once the model is trained, test the model:

rasa shell nlu

Training the dialogue model

In Rasa Core model custom action 'action_weather' needs to run on a separate server. 
That server has to be configured in a 'endpoints.yml' file. This is how to train and run the dialogue management model:

Start the custom action server by running:
rasa run actions

Open a new terminal and train the Rasa Core model by running:
rasa train

Talk to the chatbot once it's loaded after running:
rasa x


