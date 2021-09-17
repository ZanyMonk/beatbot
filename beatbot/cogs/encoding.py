import base64
import binascii
import urllib.parse
from discord.ext import commands


# Encoding/Decoding from various schemes.
class Encoding(commands.Cog):
    async def cog_command_error(self, ctx, error):
        await ctx.send("There was an error with the data :[")

    @commands.command(help="encode/decode **base__64__**")
    async def b64(self, ctx, encode_or_decode, string):
        byted_str = str.encode(string)

        if encode_or_decode == 'decode':
            decoded = base64.b64decode(byted_str).decode('utf-8')
            await ctx.send(decoded)

        if encode_or_decode == 'encode':
            encoded = base64.b64encode(byted_str).decode('utf-8').replace('\n', '')
            await ctx.send(encoded)

    @commands.command(help="encode/decode **base__32__**")
    async def b32(self, ctx, encode_or_decode, string):
        byted_str = str.encode(string)

        if encode_or_decode == 'decode':
            decoded = base64.b32decode(byted_str).decode('utf-8')
            await ctx.send(decoded)

        if encode_or_decode == 'encode':
            encoded = base64.b32encode(byted_str).decode('utf-8').replace('\n', '')
            await ctx.send(encoded)

    @commands.command(help="encode/decode **binary**")
    async def binary(self, ctx, encode_or_decode, string):
        if encode_or_decode == 'decode':
            string = string.replace(" ", "")
            data = int(string, 2)
            decoded = data.to_bytes((data.bit_length() + 7) // 8, 'big').decode()
            await ctx.send(decoded)

        if encode_or_decode == 'encode':
            encoded = bin(int.from_bytes(string.encode(), 'big')).replace('b', '')
            await ctx.send(encoded)

    @commands.command(help="encode/decode **hexadecimal**")
    async def hex(self, ctx, encode_or_decode, string):
        if encode_or_decode == 'decode':
            string = string.replace(" ", "")
            decoded = binascii.unhexlify(string).decode('ascii')
            await ctx.send(decoded)

        if encode_or_decode == 'encode':
            byted = string.encode()
            encoded = binascii.hexlify(byted).decode('ascii')
            await ctx.send(encoded)

    @commands.command(help="encode/decode **URL encoding**")
    async def url(self, ctx, encode_or_decode, message):
        if encode_or_decode == 'decode':

            if '%20' in message:
                message = message.replace('%20', '(space)')
                await ctx.send(urllib.parse.unquote(message))
            else:
                await ctx.send(urllib.parse.unquote(message))

        if encode_or_decode == 'encode':
            await ctx.send(urllib.parse.quote(message))


def setup(bot):
    bot.add_cog(Encoding())
