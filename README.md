Ghaouthi Brahim 22102881
Lema Xavier Santiago 22108098
speech-assistant
https://mygit.th-deg.de/bg07881/speech-assistant

# Project Description
We used RASA python library to develop an NLU Chatbot. The purpose of the chatbot is to help the user find some interesting exercises adequate for their needs. The system, chatbot, has a name. It is called Jim. And it will try to be as fluent as possible in human natural language. For example, you can ask it how it feels, who it is, and what's its purpose to make some chitchat.

# Installation
To run the chatbot the required libraries should be installed first:

pip install -r requirements.txt


If the dependencies are fulfilled, just run the command rasa shell to start a conversation with Jim.

# Basic Usage
The conversation can go through various paths. The bot will ask aggressively sometimes but is not necessary to answer its questions directly. If at some point Jim doesn't detect your intent correctly, you can just inform it by saying something like That is not what I was asking. It won't be offended, it doesn't have feelings.

# Implementation of the Requests
The bot can deliver many different routines of exercises for different needs such as:

. Losing weight
. Gaining muscle mass
. Cardio training
. Light exercises
. Train at home

It can also suggest routines focusing on a specific muscle or muscle group such as:

. Legs
. Abs
. Back
. Triceps

And more.

Work done
First we chose our domain and created some user journey flows.
Then we created Personas to get a better understanding of the kind of language and exercises the bot would be retrieving.
We built some conversations examples, got the exercises from a single API call to api-ninjas and then hard-coded each routine in a response text.
We filled the nlu with intents, set up some rules and wrote basic stories. Based on the desired stories we created the responses. Then we trained with the interactive training mode to strengthen the conversation paths.
