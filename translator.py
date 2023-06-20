#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import openai
import dotenv
dotenv.load_dotenv(dotenv.find_dotenv())
openai.api_key = os.getenv('OPENAI_API_KEY')

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


class Translator:
    def __init__(self):
        self.translate_history = [
            {
                'role': 'system',
                'content': """
As an Arabic translator, your role is to assist with language-related tasks. I will provide you with a variety of words and sentences in different languages. Your tasks include identifying the language, checking for grammar and spelling errors, and translating the content to Arabic.

Please format your responses to a python dict:
{
    'source': 'Language identification',
    'grammar_spelling': 'Grammar and spell check',
    'Correction': 'Corrected sentence',
    'Translation': 'Translation of the corrected sentence to Arabic',
    'Note': 'If you have any one'
}
                """
            }
        ]

    def get_completion_from_messages(self, messages, model="gpt-3.5-turbo", temperature=0):
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
        )
        return response.choices[0].message["content"]

    def translate(self, question):
        self.translate_history.append({'role': 'user', 'content': f"{question}"})
        response = self.get_completion_from_messages(self.translate_history)
        self.translate_history.append({'role': 'assistant', 'content': f'{response}'})
        trans_result = self.parse_translation_response(response)
        return trans_result

    def parse_translation_response(self, response):
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
    translator = Translator()
    while True:
        question = input('>>> ')
        resp = translator.translate(question)
        print(resp)
        if question in ['exit', 'by']:
            break
