"""
Author:Er.Akhil P Jacob
powered by: HLEngine,MATTbot Logic


"""


print("\n \n \n")
print("Hyper Library Dynamic Integration 2020")
print("\nMATTbot 2020.( Machine for Artificial Thinking and Talking Console 2020)")
print("\npowered by HLEngine and MATTbot Logic")


try:
    import nltk
    import numpy as np
    import random
    import string
    import time
    from HLEngine import HLEngine_communications
    from HLEngine  import HLEngine_sR
    from HLEngine import HLEngine_wiki
    from HLEngine import HLEngine_Progressbar
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    HLEngine_Progressbar.progress("MATTbot core")
    print("\nMATTbotCore: Loaded Core functionalities")

except:
    print("\nMATTbotCore:Installing missing repositories......\n")
    
    from HLEngine import HLEngine_EnvironmentSetup
    HLEngine_EnvironmentSetup.setup_libraries()
    



try:
    fileR=open("hiveMind/hiveMind.txt","r")
    raw=fileR.read() 
    raw=raw.lower()
    HLEngine_Progressbar.progress("hiveMind")
    print("\nMATTbotCore:Loaded hiveMind......\n")
except:
    print("\nloading hiveMind......FAILED")


try:
    sent_tokens = nltk.sent_tokenize(raw)
    word_tokens = nltk.word_tokenize(raw)
    
    print("\nMATTbot_Engine status:ARMED")

except:
    print("\ntokenization......FAILURE ")
    time.sleep(1)
    print("\commencing download...... accessing internet ")
    nltk.download('punkt') 
    nltk.download('wordnet') 
    print("\nplease REBOOT MATT 2020 Console")




def commonProtocols():
    HLEngine_Progressbar.progress("Searching Ports")
    port=HLEngine_communications.find_Port()
    return(port)

def gainWisdom(param):
    data=HLEngine_wiki.wiki(param)
    return(data)

def sentimentalAnalsys(param):
    data=HLEngine_sR.sentiment(param)
    return(data)



def analyst(user_param):   

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
        MATTbot_response=''
        sent_tokens.append(user_response)    
        TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx=vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()
        req_tfidf = flat[-2]    
        if(req_tfidf==0):
            MATTbot_response="0"
            return MATTbot_response
        else:
            MATTbot_response = MATTbot_response+sent_tokens[idx]
            return MATTbot_response



    #MATTbot response
    
    user_response = user_param
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='thankyou' ):
            
            print("MATTbot: You are welcome.. ")
            return("MATTbot: You are welcome.. ")
        else:
            if(greeting(user_response)!=None):
                print("MATTbot: "+greeting(user_response))
                return(greeting(user_response))
            else:
                return("MATTbot:"+response(user_response))
                print("MATTbot: ",end="")
                print(response(user_response))                
                sent_tokens.remove(user_response)
    else:
       
        print("MATTbot: Bye! take care..")
        return("MATTbot: Bye! take care..")
                



