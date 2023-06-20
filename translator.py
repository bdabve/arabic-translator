#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import openai
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,        # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


translate_history = [
    {
        'role': 'system',
        'content': """
As an Arabic translator, your role is to assist with language-related tasks. I will provide you with a variety of words and sentences in different languages. Your tasks include identifying the language, checking for grammar and spelling errors, and translating the content to Arabic.

Please format your responses to a python dict:
{
    'source': 'Language identification'
    'grammar_spelling': 'Grammar and spell check'
    'Correction': 'Corrected sentence'
    'Translation': 'Translation of the corrected sentence to Arabic'
    'Note': 'If you have any one'
}
        """
    }
]


def translate(question):
    translate_history.append({'role': 'user', 'content': f"{question}"})
    response = get_completion_from_messages(translate_history)
    translate_history.append({'role': 'assistant', 'content': f'{response}'})
    trans_result = parse_translation_response(response)
    return trans_result


def parse_translation_response(response):
    # Split the response into individual lines
    lines = response.strip().split("\n")
    try:
        translation_result = {
            'source': lines[1].split(": ")[1],
            'grammar_spell_check': lines[2].split(": ")[1],
            'corrected_sentence': lines[3].split(": ")[1],
            'translation': lines[4].split(": ")[1]
        }

        return translation_result
    except IndexError:
        return lines


if __name__ == '__main__':
    while True:
        question = input('>>> ')
        resp = translate(question)
        print(resp)
        if question in ['exit', 'by']:
            break
