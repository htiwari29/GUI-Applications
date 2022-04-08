from gtts import gTTS
  
import os
mytext = "Welcome to my Github Profile. You'll find other interesting projects in this repo."
  
language = 'en'
  
myAudio = gTTS(text=mytext, lang=language, slow=False)
  
myAudio.save("welcome.mp3")
  
os.system("afplay welcome.mp3")