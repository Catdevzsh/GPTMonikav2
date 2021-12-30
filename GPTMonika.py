## this is a alexa clone using the gpt-2 model
import os as os
import sys as sys
import huggingface as huggingface
import requests as requests
import json as json
import time as time 
import openai
import random as random
## write a alexa like program using gpt2 model
## this is a alexa clone using the gpt-2 model
GPTMonikaProgram = openai.OpenAI('gpt2', 'gpt2-medium', 'gpt2-medium')
## use openai private key to get access to the gpt2 prommpt
GPTMonikaProgram.set_credentials('gpt2-medium', 'gpt2-medium')
## get the gpt2 model
GPTMonikaModel = GPTMonikaProgram.model
## write a cli interface for talking to the bot
def GPTMonikaCLI():
    ## get the user input
    userInput = input("What would you like to ask GPTMonika? ")
    ## get the bot response
    botResponse = GPTMonikaModel.generate(userInput)
    ## print the bot response
    print(botResponse)
    ## call the cli again
    GPTMonikaCLI()

    print(GPTMonikaCLI)

