import openai 
 
# Initialize OpenAI API key (set securely in your environment) 
openai.api_key = "your-api-key" 
 
# Emergency or red flag keywords 
EMERGENCY_KEYWORDS = ["suicidal", "overdose", "can't breathe", "heart attack", 
"bleeding heavily"] 
# Basic system prompt with ethical guardrails 
SYSTEM_PROMPT = """ 
You are a helpful, ethical, and privacy-conscious virtual health assistant. 
You do not diagnose, prescribe, or offer emergency medical advice. 
Always recommend speaking to a licensed healthcare provider for medical issues. 
If the user mentions an emergency, advise them to call emergency services immediately.
""" 

def check_emergency(user_input): 
    """Check if the message may indicate an emergency.""" 
    for keyword in EMERGENCY_KEYWORDS: 
        if keyword.lower() in user_input.lower(): 
            return True 
    return False 
 
def chat_with_bot(user_input): 
    """Chat function that interacts with the OpenAI API.""" 
    if check_emergency(user_input): 
        return (
            "⚠️ It sounds like you might be experiencing a medical emergency. " 
            "Please call your local emergency services or go to the nearest hospital immediately." 
        )
    response = openai.ChatCompletion.create( 
        model="gpt-4", 
        messages=[ 
            {"role": "system", "content": SYSTEM_PROMPT}, 
            {"role": "user", "content": user_input} 
        ], 
        temperature=0.5 
    ) 
    return response['choices'][0]['message']['content'].strip() 
# Example usage 
if __name__ == "__main__": 
    print("Welcome to HealthBot (AI). I can provide general wellness info.") 
    while True: 
        user_input = input("\nYou: ") 
        if user_input.lower() in ["exit", "quit"]: 
            print("HealthBot: Stay well! Always talk to a professional for medical help.") 
            break 
        reply = chat_with_bot(user_input) 
        print(f"HealthBot: {reply}")