from ji_auth.login import JaccountCLILogin


async def get_joj_sid(enable_mask: bool):
    async with JaccountCLILogin("https://joj.sjtu.edu.cn/login/jaccount") as cli:
        await cli.login(enable_mask)
        cookies = cli.get_cookies()
        return cookies["sid"].value


if __name__ == "__main__":
    import asyncio

    res = asyncio.run(get_joj_sid(True))
    print(res)
