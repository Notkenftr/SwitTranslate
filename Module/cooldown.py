import time
from Module.Translate.Utils import Config
users = {}

class CoolDown:
    @staticmethod
    def add(user_id):
        users[user_id] = time.time()
        return 0
    @staticmethod
    def check(user_id):
        if user_id in users:
            elapsed = time.time() - users[user_id]
            if elapsed < Config.TranslateCommand.Cooldown():
                return 1
            else:
                return 2
        else:
                return 0
    @staticmethod
    def remove(user_id):
        users.pop(user_id, None)
        return 0