import openai


# Function for Generating Story Prompt

def get_story_prompt():
    genre = input('Enter the genre: ')
    main_character_name = input("Enter main character's name: ")
    age = input('Enter the age of main character: ')
    input_prompt = input(
        "Write the initial lines of any length describing the main character: ")
    goals_or_challenges = input(
        "Write about the goals and challenges that the main character will face: ")
    other_characters = input("Enter any other characters: ")
    f_prompt = f"Imagine a {genre}-themed story featuring {main_character_name} who is {age} years old. {input_prompt}. Also include the main character's goal or challenges such as {goals_or_challenges}, any other characters such as {other_characters} if provided. Write out the entire story in great detail:"
    prompt = f_prompt.format(genre=genre, main_character_name=main_character_name, age=age, input_prompt=input_prompt,
                             goals_or_challenges=goals_or_challenges, other_characters=other_characters)
    return prompt

# Function for Generating Story


def generate_text(prompt, openai_token):
    openai.api_key = openai_token
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1.0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_txt = response['choices'][0]['text'].strip()
    return response_txt

# Function for Storing the response inside a list


def clean_text(response_txt):
    text = response_txt.split('\n')
    text_list = [line.strip() for line in text if line.strip()]
    return text_list


if __name__ == "__main__":
    # Generating the story using the above defined Functions
    prompt = get_story_prompt()
    openai_token = "ENTER YOU ACCESS TOKEN HERE"
    response = generate_text(prompt, openai_token)
    text_list = clean_text(response)
    print(text_list)
