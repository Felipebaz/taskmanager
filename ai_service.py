import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Carga las variables de entorno desde el archivo .env

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) 

def create_simple_task(description): 
    if not client.api_key:
        return ["Error: OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable."]
    try: 
        prompt = f"""Break down this complex task into 3 or 4 simple and concrete subtasks: 

Task : {description}

Answer format:

- Subtask 1
- Subtask 2
- Subtask 3
- etc.

Answer only with one subtask per line, without any additional text or formatting and starting with a dash."""

        params = {
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are an assistant that helps break down complex tasks into simple, actionable subtasks."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 300,
            "temperature": 0.3
        }
        response = client.chat.completions.create(**params)

        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)
        return subtasks if subtasks else ["Error: No subtasks were generated. Please try again."]
    
    except Exception as e:
        print(f"DEBUG ERROR: {e}")
        return ["Error: An error occurred while generating subtasks. Please try again."]    


    