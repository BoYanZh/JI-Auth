from ji_auth.login import JaccountCLILogin


async def get_coursesel_jsid(enable_mask: bool):
    async with JaccountCLILogin("https://coursesel.umji.sjtu.edu.cn/") as cli:
        await cli.login(enable_mask)
        cookies = cli.get_cookies()
        return cookies["JSESSIONID"].value


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(get_coursesel_jsid(True))
    print(res)
