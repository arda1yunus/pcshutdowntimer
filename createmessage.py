from gtts import gTTS

#for other languages:
#Türkçe: tr
#English: en
#Española : es
#Deutsch : de
#Français : fr
#Italiano : it

def main():
  SpeakText()

def SpeakText():
    msg = 'Goodnight my friend.'
    engine = gTTS(text=msg, lang='en') #If you want to use this in your languages, you can change the (lang="Your lang code") keyword like this.
    engine.save('goodnight.mp3') 

if __name__ == "__main__":
    main()
