import openai 
# Set your OpenAI API key 
openai.api_key = "your-api-key" 
def generate_plot(genre="fantasy", style="dramatic", length="short"): 
    prompt = ( 
        f"Generate a {length} {genre} story plot with a {style} tone. " 
        "Include a beginning, middle, and twist ending." 
    ) 
    response = openai.ChatCompletion.create( model="gpt-4", messages=[{"role": "system", "content": "You are a creative story writer AI."}, {"role": "user", "content": prompt}], temperature=0.8,max_tokens=300) 
    return response['choices'][0]['message']['content'] 
def write_story(plot_description, length="medium"): 
    prompt = ( 
        f"Write a {length} story based on this plot:\n\n" 
        f"{plot_description}\n\n" 
        "Make it immersive with character development, dialogue, and vivid description." ) 
    response = openai.ChatCompletion.create(model="gpt-4",messages=[ {"role": "system", "content": "You are a master fiction author."},{"role": "user", "content": prompt}],temperature=0.9,max_tokens=1000) 
    return response['choices'][0]['message']['content'] 
# Example usage 
if __name__ == "__main__": 
    plot = generate_plot(genre="sci-fi", style="mysterious", length="short") 
    print("Generated Plot:\n", plot) 
    story = write_story(plot_description=plot, length="long") 
    print("\nGenerated Story:\n", story)
