#IMPORTS ARE IN IMPORTS FILE#
async def on_message(message):
     import json
     async def user_voted(author_id=message.author.id):
         
         voteurl=f"https://discordbots.org/api/bots/543966796944769044/check?userId={author_id}"
         async with aiohttp.ClientSession(headers=dblheaders).get(voteurl) as r:
                 
            
       #  dblvotes.votes.votes.user_voted(client, messager.author.id)
             json=await r.text()
 #        return json[9]
         if int(json[9]) >0:
             return True
         else:
             return False
     async def getServerInfo(self=client):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=json.loads(await client.http.request(
            discord.http.Route(
            'GET', '/guilds/'+_gid)))
       #  channeldata= [d for d in data if d['id'] == message.server.id][0]
         return data
     class nitro():             
      async def tier(self=client):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=await client.http.request(
            discord.http.Route(
            'GET', '/guilds/'+_gid))
       #  channeldata= [d for d in data if d['id'] == message.server.id][0]
         return data["premium_tier"]
      async def count(self=client):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=await client.http.request(
            discord.http.Route(
            'GET', '/guilds/'+_gid))
       #  channeldata= [d for d in data if d['id'] == message.server.id][0]
         return data["premium_subscription_count"]
     async def nitro_tier(self=client):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=await client.http.request(
            discord.http.Route(
            'GET', '/guilds/'+_gid))
       #  channeldata= [d for d in data if d['id'] == message.server.id][0]
         return data["premium_tier"]
     async def nitro_count(self=client):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=await client.http.request(
            discord.http.Route(
            'GET', '/guilds/'+_gid))
       #  channeldata= [d for d in data if d['id'] == message.server.id][0]
         return data["premium_subscription_count"]
     async def is_nsfw(self=client,channel=message.channel):
         try:
            _gid=message.server.id
         except AttributeError:
            return False
         data=await self.http.request(
            discord.http.Route(
            'GET', '/guilds/{guild_id}/channels', guild_id=_gid))
         channeldata= [d for d in data if d['id'] == channel.id][0]
         return channeldata['nsfw']
     async def IsDm(self=client,channel=message.channel):
        try:
         try:
            _gid=message.server.id
         except AttributeError:
            try:
                _gid=message.channel.id
            except AttributeError:
                return False
         data=await self.http.request(
            discord.http.Route(
            'GET', '/guilds/{guild_id}/channels', guild_id=_gid))
         channeldata= [d for d in data if d['id'] == channel.id][0]
         if channeldata['type'] == 1:
             return True
         
         else:
                 return False
        except discord.errors.NotFound:
                return True         
         
     async def channelinfo(self=client,channel=message.channel):
        try:
            _gid=message.server.id
        except AttributeError:
            return False
        data=await self.http.request(
            discord.http.Route(
            'GET', '/guilds/{guild_id}/channels', guild_id=_gid))
        channeldata= [d for d in data if d['id'] == channel.id][0]
        return channeldata
     
     if message.content.startswith(prefix+"neko"):
          embed=discord.Embed(title="Nekos!")
          embed.set_image(nbapi.random.neko())
          embed.set_footer(text="Made by LazyNeko",icon_url="http://neko-bot.net/images/ownericon.round.png")
     if message.content.startswith(prefix+"anime"):
          embed=discord.Embed(title="Anime!")
          embed.set_image(nbapi.random.anime())
          embed.set_footer(text="Made by LazyNeko",icon_url="http://neko-bot.net/images/ownericon.round.png")
          
