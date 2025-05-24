import openai 
import os 
# Load your OpenAI API key from environment variable 
openai.api_key = os.getenv("OPENAI_API_KEY") 
 
def generate_predictive_text(prompt, max_tokens=50, temperature=0.7, model="gpt-4"): 
    """ 
    Generate predictive text from a given prompt. 
       Args: 
        prompt (str): The input text to complete. 
        max_tokens (int): Max number of tokens to predict. 
        temperature (float): Sampling temperature for creativity. 
        model (str): OpenAI model to use (e.g., "gpt-3.5-turbo", "gpt-4"). 
    Returns: 
        str: Generated continuation text. 
    """ 
    response = openai.ChatCompletion.create( 
        model=model, 
        messages=[ 
            {"role": "system", "content": "You are a helpful text autocompletion assistant."}, 
            {"role": "user", "content": prompt} 
        ], 
        max_tokens=max_tokens, 
        temperature=temperature 
    ) 
    return response['choices'][0]['message']['content'].strip() 
# Example usage 
if __name__ == "__main__": 
    user_input = "Once upon a time in a distant galaxy," 
    prediction = generate_predictive_text(user_input) 
    print("Predicted continuation:\n", prediction)