from requests import get

class NoAPIKeySpecified(Exception):
    def __init__(self, apikey, message = "You should specify your API key first. API keys can be found at https://t.me/BotFather"):
        self.apikey = apikey
        self.message = message
        super().__init__(self.message)

class TooManyArgs(Exception):
    def __init__(self, apikey, arg_amount = 0, message = f"Got too many arguments, please specify %thismany% arguments" ):
        self.apikey = apikey
        self.message = message.replace('%thismany%', str(arg_amount))
        super().__init__(self.message)

class BotNotExisting(Exception):
    def __init__(self, apikey, message = "Either no internet, or this bot doesn't exist. Make sure you pasted your api token correctly."):
        self.apikey = apikey
        self.message = message
        super().__init__(self.message)

def CheckForAPIKey(apikey = None):
    if apikey is not None:
        response = get(f'https://api.telegram.org/bot{apikey}/getMe')
        if response.status_code == 200:
            return True
        raise BotNotExisting(apikey)
    raise NoAPIKeySpecified(apikey)
##testing area:
#CheckForAPIKey()

