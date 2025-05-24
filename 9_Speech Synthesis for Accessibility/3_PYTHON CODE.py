"""                                             WRITE ANY ONE                                                         """
#OPTION 1
import openai 
import pyttsx3 
 
# Set your OpenAI API key 
openai.api_key = "your-openai-api-key" 
# Function to get simplified or summarized version of the input text 
def get_accessible_text(input_text): 
    response = openai.ChatCompletion.create( 
        model="gpt-4", 
        messages=[ 
            {"role": "system", "content": "You simplify text for better accessibility."}, 
            {"role": "user", "content": f"Simplify or summarize this: {input_text}"} 
        ] 
    ) 
    simplified_text = response['choices'][0]['message']['content'] 
    return simplified_text.strip() 
# Function to convert text to speech 
def speak_text(text): 
    engine = pyttsx3.init() 
    engine.setProperty('rate', 150)  # Slower speech rate 
    engine.say(text) 
    engine.runAndWait() 
# Main function 
def main(): 
    input_text = input("Enter text to simplify and read aloud:\n") 
    simplified_text = get_accessible_text(input_text) 
    print("\nSimplified Text:\n", simplified_text) 
    speak_text(simplified_text) 
if __name__ == "__main__": 
    main() 

#OPTION 2
from gtts import gTTS 
import openai 
import os 
from playsound import playsound 
 
openai.api_key = "your-openai-api-key" 
def get_accessible_text(input_text): 
    response = openai.ChatCompletion.create( 
        model="gpt-4", 
        messages=[ 
            {"role": "system", "content": "You simplify text for better accessibility."}, 
            {"role": "user", "content": f"Simplify or summarize this: {input_text}"} 
        ] 
    ) 
    return response['choices'][0]['message']['content'].strip() 
def speak_text_gtts(text, filename="output.mp3"): 
    tts = gTTS(text) 
    tts.save(filename) 
    playsound(filename) 
    os.remove(filename) 
def main(): 
    input_text = input("Enter text to simplify and read aloud:\n") 
    simplified_text = get_accessible_text(input_text) 
    print("\nSimplified Text:\n", simplified_text) 
    speak_text_gtts(simplified_text) 
if __name__ == "__main__": 
    main() 