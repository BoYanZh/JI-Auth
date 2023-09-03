from jaccount_auth import JaccountCLIAsyncIO
from getpass import getpass


class JaccountCLILogin(JaccountCLIAsyncIO):
    async def login(self, enable_mask=True):
        await self.init()
        captcha_ascii = self.captcha_generate_ascii()
        print("", captcha_ascii, "", sep="\n")
        captcha = input("Please enter the shown captcha: ")
        username = input("Please enter jaccount username: ")
        if enable_mask:
            password = getpass("Please enter password: ")
        else:
            password = input("Please enter password: ")
        await super().login(username, password, captcha)
