pip install gTTS playsound
import random
from gtts import gTTS
import playsound

# List of words
word_list = ["arable","surfactant","nitrogen","paralysis","metronome","attorney","snivel","contemptible","altimeter","jugular","insolent","aura","propitious","ellipsis","thyroid","elongated","lasso","incandescent","bureaucrats","refuge","shoal","perpendicularity","antechamber","jeopardy","sauna","concilatory","forsook","boba","animatronics","frijoles","minimus","senscent","secreted","aspirin","aptitude","Chicana","bilge","simultaniously","Copenhagen","Bunsen burner","defoilant","aerosol","Ramadan","photosynthesis","malignant","matterhorn","divot","pixels","antonyms","Trinidadian","mangels","nopales","Gilgamesh","conjunto","Sumerian","pinyin","Taoism","Daoism","lymphona","scandium","dendochronology","palamino","retinis pigentosa","fens","haw","peplos","moira","Erlenmeyer flask","Samian","luciferin","megaron","sphagnum","pronaos","craquelure","Macau","silicon","Albequerque","Mumbai","turquoise","Assam","lanthanides","antimony","amphoras","amphoras","hypocaust","avens","grebe","pipette","leks","pullets","Macedonia","centrifuge","coleus","Tetrazzini","Pleiades","coccidiosis","rooibos tea","Versailles","meitnerium","Okefenokee","Popocatepetl","Shannxi"]

# Function to choose a random word
def choose_random_word(word_list):
    return random.choice(word_list)

# Function to pronounce the word
def pronounce_word(word):
    tts = gTTS(word)
    tts.save("pronunciation.mp3")
    playsound.playsound("pronunciation.mp3")

# Function to ask the user to spell the word
def spelling_bee_game(word):
    print("Welcome to the Spelling Bee Challenge!")
    print(f"Listen to the word and spell it: {word}")
    
    pronounce_word(word)
    
    user_input = input("Your spelling: ").lower()
    
    if user_input == word:
        print("Correct! You spelled it right. Good job!")
    else:
        print(f"Oops! You misspelled the word. The correct spelling is: {word}")

if __name__ == "__main__":
    while True:
        # Choose a random word from the list
        random_word = choose_random_word(word_list)
        
        # Play the Spelling Bee game with the chosen word
        spelling_bee_game(random_word)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
