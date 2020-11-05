from .. import loader, utils
import siaskynet as skynet

@loader.tds
class IPLookupMod(loader.Module):
    """siasky.net uploader by @blazeftg"""
    strings = {"name": "FileUploader"}

    async def uploadcmd(self, message):
        """ .upload <реплай на файл>"""
        await message.edit(f"<b>Загружаю...</b>")
        client = skynet.SkynetClient()
        reply = await message.get_reply_message()
        if not reply:
            await message.edit("Нужен реплай")
            return
        file = await reply.download_media()
        link = client.upload_file(file)
        filtered = link.split('sia://')
        link = 'https://siasky.net/' +  str(filtered[1])
        await message.edit("Линк: \n" + link)