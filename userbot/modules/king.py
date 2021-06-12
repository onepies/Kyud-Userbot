# import userbot by apis

from time import sleep
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern="^.kyud(?: |$)(.*)")
async def _(event):
    event.pattern_match.group(1)
    await event.edit(
        " -^-^-^- **K** -^-^-^- \n"
        " -^-^-^- **Y** -^-^-^- \n"
        " -^-^-^- **U** -^-^-^- \n"
        " -^-^-^- **D** -^-^-^- \n"
        "__**USERBOT TELEGRAM**__ \n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"__**Hai aku adalah bot kyud assisten {ALIVE_NAME} yang menjaga akun ini**__ \n"
        "__**Terimakasih**__ \n"
        "`Enjoy:)` \n"
        "__**Owner by :**__ [Kyud](https://t.me/boyfriendnice) ")

CMD_HELP.update(
    {
        "king": "**✘ Plugin :** `kyud`\
        \n\n  •  **Perintah :** `.kyud`\
        \n  •  **Function : **Untuk melihat sesuatu yang menarik\
        \n\n  •  **Perintah :** `.sadboy`\
        \n  •  **Function : **Jadi sadboy:)\
        \n\n  •  **Perintah :** `.punten` | `.pantau`\
        \n  •  **Function : **Untuk punten dan pantau\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat owner kyud @boyfriendnice Jika ingin mengidekan sesuatu yang menarik **\
        \n\n  ** Perintah kosong **\
        \n  ** Harap chat owner kyud @boyfriendnice Jika ingin mengidekan sesuatu yang menarik **\
    "
    }
)
