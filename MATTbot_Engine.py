"""
Author:Er.Akhil P Jacob
MATTbot Logic 2020

"""

import nltk
import numpy as np
import random
import string

from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_wiki

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def analyst(raw):
    nltk.download('punkt')
    nltk.download('wordnet')
    raw=raw.lower()
    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)

#preprocess

    lemmer = nltk.stem.WordNetLemmatizer()
    def LemTokens(tokens):
        return [lemmer.lemmatize(token) for token in tokens]
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

    def LemNormalize(text):
        return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

    #greeting

    GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
    GREETING_RESPONSES = ["hi...", "hey..", "wassup...", "hi there...", "hello...", "I am glad! You are talking to me"]


    def greeting(sentence):
    
        for word in sentence.split():
            if word.lower() in GREETING_INPUTS:
                return random.choice(GREETING_RESPONSES)


    #user response
    def response(user_response):
        Doodle_response=''
        sent_tokens.append(user_response)    
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]    
        if(req_tfidf==0):
            Doodle_response=Doodle_response+"I am sorry! I don't understand you"
            return Doodle_response
        else:
            Doodle_response = Doodle_response+sent_tokens[idx]
            return Doodle_response



    #MATTbot response

    flag=True
    print("MACHINE FOR ARTIFICIAL THINKING AND TALKING (MATT2020) ")
    
    name="Achacha"
    print("\nMATTbot: Hi my name is MATTbot, the chat bot. I am at your service "+name)
    
    while(flag==True):
        user_response = input()
        user_response=user_response.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' or user_response=='thankyou' ):
                flag=False
                print("MATTbot: You are welcome.. "+name+"The academic councillor will call you to get feedback")
            else:
                if(greeting(user_response)!=None):
                    print("MATTbot: "+greeting(user_response))
                else:
                    print("MATTbot: ",end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag=False
            print("MATTbot: Bye! take care.."+name)
                



