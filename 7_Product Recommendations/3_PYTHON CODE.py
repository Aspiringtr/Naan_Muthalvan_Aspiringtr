import openai 
import pandas as pd 
# Replace with your own OpenAI API key 
openai.api_key = "your_openai_api_key" 
# Sample user profile 
user_profile = { 
    "name": "Alice", 
    "age": 30, 
    "interests": ["fitness", "technology", "sustainable living"], 
    "past_purchases": ["yoga mat", "smartwatch", "reusable water bottle"] 
} 
# Sample product catalog 
product_catalog = pd.DataFrame([ 
    {"product": "Eco-Friendly Yoga Pants", "category": "fitness"}, 
    {"product": "Wireless Earbuds", "category": "technology"}, 
    {"product": "Smart Thermostat", "category": "technology"}, 
    {"product": "Organic Protein Powder", "category": "fitness"},  
    {"product": "Solar-Powered Charger", "category": "sustainable living"}, 
    {"product": "Stainless Steel Lunchbox", "category": "sustainable living"}, 
]) 
def generate_prompt(user_profile, product_catalog): 
    catalog_str = "\n".join(f"- {row['product']} ({row['category']})" 
                            for _, row in product_catalog.iterrows()) 
 
    prompt = f""" 
You are a personalized product recommendation assistant. 
User Profile: - Name: {user_profile['name']} - Age: {user_profile['age']} - Interests: {', '.join(user_profile['interests'])} - Past Purchases: {', '.join(user_profile['past_purchases'])} 
Product Catalog: 
{catalog_str} 
Based on the user profile and product catalog, recommend the top 3 most suitable 
products. Just list the product names. 
""" 
    return prompt.strip() 
def get_recommendations(prompt): 
    response = openai.ChatCompletion.create( 
        model="gpt-4", 
        messages=[{"role": "user", "content": prompt}], 
        temperature=0.7, 
    ) 
    return response.choices[0].message["content"].strip() 
# Generate prompt and get recommendations 
prompt = generate_prompt(user_profile, product_catalog) 
recommendations = get_recommendations(prompt) 
print("Recommended Products:") 
print(recommendations)