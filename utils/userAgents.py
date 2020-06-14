import random
from enum import Enum

class OS(Enum):
    MACOS = "macos"

class Browser(Enum):
    CHROME = "chrome"

user_agents = {
    "macos": {
        "chrome": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
            ],
        "safari": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15",
            ],
        "firefox": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0",
            ],
        "edge": [
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36 Edg/83.0.478.37",
            ]
    },
    "windows": {
        "chrome": [

        ],
        "safari": [

        ],
        "firefox": [

        ],
        "edge": [

        ],
    },
    "ios": {
        "chrome": [

        ],
        "safari": [

        ],
        "firefox": [

        ],
        "edge": [
            
        ],
    },
    "android": {
       "chrome": [

        ],
        "safari": [

        ],
        "firefox": [

        ],
        "edge": [
            
        ],
    }
}

def get_user_agent(os, browser):
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    try:
        os = user_agents[os]
        browsers = os[browser]
        user_agent = browsers[random.randint(0, len(browsers) - 1)]
    except:
        pass
    return user_agent