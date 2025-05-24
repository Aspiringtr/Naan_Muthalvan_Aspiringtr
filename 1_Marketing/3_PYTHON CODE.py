import openai 

# Set your OpenAI API key 
openai.api_key = "your-api-key-here" 
 
def generate_marketing_content(prompt, tone="professional", max_tokens=150): 
    """ 
    Generate marketing content using OpenAI's GPT model. 
     
    Parameters: 
    - prompt (str): The idea or product to promote. 
    - tone (str): Desired tone of the content ("professional", "funny", "persuasive"). 
    - max_tokens (int): Length of the output. 
     
    Returns: 
    - str: Generated marketing content. 
    """ 
    formatted_prompt = ( 
        f"Write a {tone} marketing message about the following:\n" 
        f"{prompt}\n" 
        f"Make it catchy and suitable for use on a website or social media." 
    ) 
 
    response = openai.ChatCompletion.create( 
        model="gpt-4", 
        messages=[ 
            {"role": "system", "content": "You are a marketing copywriter."}, 
            {"role": "user", "content": formatted_prompt} 
        ],
        max_tokens=max_tokens, 
        temperature=0.8, 
        n=1 
    ) 
 
    content = response['choices'][0]['message']['content'] 
    return content.strip() 

# Example usage 
if __name__ == "__main__": 
    product_idea = "A new AI-powered analytics tool that helps small businesses understand customer behavior" 
    generated_copy = generate_marketing_content(product_idea, tone="persuasive") 
    print("Generated Marketing Content:\n") 
    print(generated_copy)