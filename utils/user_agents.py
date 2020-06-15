import random
from enum import Enum
import json

class OS(Enum):
    MACOS = "macos"

class Browser(Enum):
    CHROME = "chrome"

def get_user_agent(os, browser):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    try:
        with open('user_agents.json', 'r') as json_file:
            user_agents = json.load(json_file)
        user_agent = random.choice(user_agents[os][browser])
    except:
        pass
    return user_agent