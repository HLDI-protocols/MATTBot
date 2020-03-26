"""
Author:Er.Akhil P Jacob
Bot:MATTbot 2020(Machine for Artificial Thinking & Talking)

"""
import MATTbot_Engine
from HLEngine import HLEngine_sR
wisdom=open("wisdom/wisdom.txt","r")
raw=wisdom.read()    
raw=raw.lower()
MATTbot_Engine.analyst(raw)


