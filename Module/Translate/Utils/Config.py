# MIT License
# Copyright (c) 2025 kenftr


import os
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..','..'))

class Config:
    @staticmethod
    def _read():
        with open(os.path.join(ROOT, 'config.yml'), 'r', encoding='utf-8') as f:
            return yaml.load(stream=f, Loader=yaml.SafeLoader)


    class Discord:
        @staticmethod
        def Token():
            return (Config._read()).get('Discord', {}).get('token', '')

        @staticmethod
        def Prefix():
            return (Config._read()).get('Discord', {}).get('prefix', '!')

        @staticmethod
        def Intents():
            return (Config._read()).get('Discord', {}).get('intents', [])

        @staticmethod
        def Status():
            return (Config._read()).get('Discord', {}).get('status', 'online')

        @staticmethod
        def Activity():
            return (Config._read()).get('Discord', {}).get('activity', {})


    class Gemini:
        @staticmethod
        def ApiKey():
            return (Config._read()).get('Gemini', {}).get('api_key', '')
        @staticmethod
        def Temperature():
            return (Config._read()).get('Gemini', {}).get('temperature', 0.3)
        @staticmethod
        def Top_p():
            return (Config._read()).get('Gemini', {}).get('top_p', 0.9)
        @staticmethod
        def Top_k():
            return (Config._read()).get('Gemini', {}).get('top_k', 50)
        @staticmethod
        def Max_output_tokens():
            return (Config._read()).get('Gemini', {}).get('max_output_tokens', 8192)

        @staticmethod
        def System_instruction():
            return (Config._read()).get('Gemini', {}).get('system_instruction', '')

    class TranslateCommand:
        @staticmethod
        def Name():
            return (Config._read()).get('translate_command', {}).get('name', 'config-translate')

        @staticmethod
        def Description():
            return (Config._read()).get('translate_command', {}).get('description', '')

        @staticmethod
        class Describe:
            @staticmethod
            def Translate_to_description():
                return (Config._read()).get('translate_command', {}).get('describe', {}).get('translate_to_description','translate to')
            @staticmethod
            def Config_file_description():
                return (Config._read()).get('translate_command', {}).get('describe', {}).get('config_file_description','Please upload your config file here, not exceeding 8 MB.')
        @staticmethod
        def Enabled():
            return (Config._read()).get('translate_command', {}).get('enabled', True)

        @staticmethod
        def Cooldown():
            return (Config._read()).get('translate_command', {}).get('cooldown', 5)

        @staticmethod
        def RolesAllowed():
            return (Config._read()).get('translate_command', {}).get('permissions', {}).get('roles_allowed', [])

        @staticmethod
        def UsersAllowed():
            return (Config._read()).get('translate_command', {}).get('permissions', {}).get('users_allowed', [])