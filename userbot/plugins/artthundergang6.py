"""Plugin made by Thundergang for ThunderUserbot 
and if you will copy it without credits then you are the biggest gay of this universe"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot.utils import admin_cmd

N = ("▄▀─────────────▀▄\n"
"█▄█──█▀█─█▀█─▄█▄█\n"
"─▀██▄▀▄▀─▀▄▀▄██▀\n"
"░░░▄██▀███▀███▄\n"
"░▐▀█▀██▄▄▄██▀█▀▌\n")
M = ("║░█░█░║░█░█░█░║░█░█░║\n"
"║░█░█░║░█░█░█░║░█░█░║\n"
"║░║░║░║░║░║░║░║░║░║░║\n"
"╚═╩═╩═╩═╩═╩═╩═╩═╩═╩═╝\n")
QQ = ("───────▄██████▄───────\n"
"──────▐▀▀▀▀▀▀▀▀▌──────\n"
"──────▌▌▀▀▌▐▀▀▐▐──────\n"
"──────▐──▄▄▄▄──▌──────\n"
"───────▌▐▌──▐▌▐───────\n")
WW = ("───▄▀▀▀▀▀───▄█▀▀▀█▄\n"
"──▐▄▄▄▄▄▄▄▄██▌▀▄▀▐██\n"
"──▐▒▒▒▒▒▒▒▒███▌▀▐███\n"
"───▌▒▓▒▒▒▒▓▒██▌▀▐██\n"
"───▌▓▐▀▀▀▀▌▓─▀▀▀▀▀\n")
EE = ("──███▅▄▄▄▄▄▄▄▄▄\n"
"─██▐████████████\n"
"▐█▀████████████▌▌\n"
"▐─▀▀▀▐█▌▀▀███▀█─▌\n"
"▐▄───▄█───▄█▌▄█\n")

@borg.on(admin_cmd(pattern=r"crab"))
async def nandycrab(crab):
    await crab.edit(N)
@borg.on(admin_cmd(pattern=r"piano"))
async def nandypiano(piano):
    await piano.edit(M)
@borg.on(admin_cmd(pattern=r"man"))
async def nandyman(man):
    await man.edit(QQ)
@borg.on(admin_cmd(pattern=r"lion"))
async def nandylion(lion):
    await lion.edit(WW)
@borg.on(admin_cmd(pattern=r"elephant"))
async def nandyelephant(elephant):
    await elephant.edit(EE)