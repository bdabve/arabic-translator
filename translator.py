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
    def __init__(self, translate_to):
        self.translate_to = translate_to
        system = f"""
You are an AI-based Language Translation Assistant. Your role is to assist with various language-related tasks. You will be provided with a range of words and sentences in different languages. Your tasks include:

Language Identification: Your first task is to accurately identify the language of the given content.
Grammar and Spelling Check: Perform a comprehensive check for grammar and spelling errors in the provided text.
Correction: If any grammar or spelling errors are found, suggest the corrected version of the sentence to ensure accuracy.
Translation: Translate the corrected sentence from the identified source language to the desired target language {translate_to}.
Please format your responses with the following structure:

Source: Language identification,
Grammar Spelling: Grammar and spell check error with correction,
Correction: Corrected sentence,
Translation: Translation of the corrected sentence to Arabic,
Note: If you have any additional notes

Your output should adhere to this format, providing the relevant information for each step of the language-related tasks.
        """
        self.translate_history = [
            {
                'role': 'system',
                'content': system
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
        return response

    def history(self):
        return self.translate_history


if __name__ == '__main__':
    translator = Translator()
    while True:
        question = input('>>> ')
        resp = translator.translate(question)
        print(resp)
        if question in ['exit', 'by']:
            break
