import os
import openai
import json

openai.api_key = "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"

l_genre = ["Romance",    "Fantasy",    "Science fiction",    "Mystery",    "Thriller",
           "Horror",    "Motivational",    "Action",    "Comedy",    "Adventure"]
l_main_character_name = ['Aiden', 'Olivia', 'Ahmed', 'Marcus', 'Rachel']
l_age = ['18', '20', '30', '40', '50']
l_input_prompt = ['']
l_goals_or_challenges = ['']
l_other_characters = ['']
f_prompt = "Imagine a {genre}-themed story featuring a {main_character_name} who is {age} years old.{input_prompt}. Also include main character's goal or challenges {goals_or_challenges}, any other characters {other_characters} if provided. Write out the entire story in great detail:"
f_sub_prompt = "{genre}, {main_character_name}, {age}, {input_prompt}, {goals_or_challenges}, {other_characters}"

responses = []
for genre in l_genre:
    for main_character_name in l_main_character_name:
        for age in l_age:
            for input_prompt in l_input_prompt:
                for goals_or_challenges in l_goals_or_challenges:
                    for other_characters in l_other_characters:
                        prompt = f_prompt.format(genre=genre, main_character_name=main_character_name, age=age, input_prompt=input_prompt,
                                                 goals_or_challenges=goals_or_challenges, other_characters=other_characters)
                        sub_prompt = f_sub_prompt.format(genre=genre, main_character_name=main_character_name, age=age, input_prompt=input_prompt,
                                                         goals_or_challenges=goals_or_challenges, other_characters=other_characters)
                        # print(sub_prompt)
                        print(prompt)
                        response = openai.Completion.create(
                            model="text-davinci-003",
                            prompt=prompt,
                            temperature=0.9,
                            max_tokens=500,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0
                        )
                        # print(response)
                        finish_reason = response['choices'][0]['finish_reason']
                        response_txt = response['choices'][0]['text']
                        print(response_txt)
                        response_dict = {"genre": genre,
                                         "main_character_name": main_character_name,
                                         "age": age,
                                         "input_prompt": input_prompt,
                                         "goals_or_challenges": goals_or_challenges,
                                         "other_characters": other_characters,
                                         'prompt': prompt,
                                         'sub_prompt': sub_prompt,
                                         'Completion': response_txt,
                                         'finish_reason': finish_reason}
                        responses.append(response_dict)

# Save responses to a JSON file
with open('dataset_story.json', 'w') as f:
    json.dump(responses, f)
