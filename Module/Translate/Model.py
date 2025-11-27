# MIT License
# Copyright (c) 2025 kenftr


from google import genai
from google.genai import types
from Module.Translate.Utils import Config

class Model:
    def __init__(self,target,config_data):
        self.config_data = config_data
        self.target = target
        self.Client = genai.Client(
            api_key=Config.Gemini.ApiKey()
        )
        self.model = 'gemini-2.5-flash'
        self.gemini_config = types.GenerateContentConfig(
            temperature=Config.Gemini.Temperature(),
            top_p=Config.Gemini.Top_p(),
            top_k=Config.Gemini.Top_k(),
            max_output_tokens=Config.Gemini.Max_output_tokens(),
            system_instruction = [
                types.Part.from_text(text=Config.Gemini.System_instruction()),
            ],
        )

    def StartTranslate(self):
        config_data = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=f"target: {self.target}"
                                              f"ConfigData: {self.config_data}"),
                ],
            ),
        ]

        full_result = []

        for ResponseChunk in self.Client.models.generate_content_stream(
            model=self.model,
            contents=config_data,
            config=self.gemini_config
        ):
            full_result.append(ResponseChunk.text)
        return (''.join(full_result)).replace('```yaml','').replace('```','').replace('```json','```')


