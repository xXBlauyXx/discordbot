from discord.ext import commands
import discord.member
import discord
import os
import pathlib


os.system("start D:/Benedikt/Projekte/StatusBot.py")




bot = commands.Bot(command_prefix="'")



@bot.command()
async def hilfe(ctx):
    embed = discord.Embed(title="Hilfe für den **UserInfoBot**", description="**Commands:**",
                          color=0xFF0000)
    embed.add_field(name="**'hilfe**", value="zeigt Hilfe für den Bot an",
                    inline=False)
    embed.add_field(name="**'userinfo [Name]**", value="zeigt die Benutzerinfo an",
                    inline=False)
    embed.set_thumbnail(url=bot.user.avatar_url)
    mess = await ctx.send(embed=embed)



@bot.command()
async def userinfo(ctx, member: discord.Member):
                embed = discord.Embed(title="Userinfo für {}".format(member.name),
                                      description="Nickname: {}".format(member.mention),
                                      color=0xFF0000)
                embed.add_field(name="Server beigetreten", value=member.joined_at.strftime("%d/%m/%Y, %H:%M:%S"),
                                inline=True)
                embed.add_field(name="Discord beigetreten", value=member.created_at.strftime("%d/%m/%Y, %H:%M:%S"),
                                inline=True)
                rollen = " "
                for role in member.roles:
                    if not role.is_default():
                        rollen += "{} \r\n".format(role.mention)
                if rollen:
                    embed.add_field(name="Rollen", value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text="Anfrage von {}".format(ctx.author))
                mess = await ctx.send(embed=embed)


@userinfo.error
async def userinfo_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Ich kann keine Userinfo für diesen Benutzer anzeigen.")












bot.run(pathlib.Path("Zugangsdaten/UserInfoBot.credentials.txt").read_text())

