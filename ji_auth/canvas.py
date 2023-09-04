from ji_auth.login import JaccountCLILogin
from aiohttp import ClientSession
from bs4 import BeautifulSoup


async def get_canvas_token(enable_mask: bool):
    authenticity_token = ""
    async with JaccountCLILogin("https://jicanvas.com/login/openid_connect") as cli:
        await cli.login(enable_mask)
        async with cli.session.get(
            "https://jicanvas.com/profile/settings"
        ) as response:
            body = await response.text()
        soup = BeautifulSoup(body, "html.parser")
        hidden_inputs = soup.select("#access_token_form > input[type=hidden]")
        for x in hidden_inputs:
            if x["name"] == "authenticity_token":
                authenticity_token = x["value"]
                break
        cookies = cli.get_cookies()
    url = "https://jicanvas.com/profile/tokens"
    async with ClientSession() as session:
        async with session.post(
            url,
            cookies={v.key: v.value for v in cookies.values()},
            data={
                "utf8": "",
                "authenticity_token": authenticity_token,
                "purpose": "JI-Auth generated",
                "access_token[purpose]": "JI-Auth generated",
                "expires_at": "",
                "access_token[expires_at]": "",
                "_method": "post",
            },
        ) as response:
            return (await response.json())["visible_token"]


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(get_canvas_token(True))
    print(res)
