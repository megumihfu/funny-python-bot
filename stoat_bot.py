from stoat import Client
import os
from dotenv import load_dotenv
load_dotenv()
import aiohttp

class MyClient(Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session = None

    async def get_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    async def on_ready(self, _, /):      
        await self.get_session() 
        print(f'Logged on as ', self.me)

    async def on_message(self, message, /):
        if message.author_id == self.me.id:
            return 
        
        clean_msg = message.content.strip()

        if clean_msg.startswith('!gif'):
            clean_words = clean_msg.split() 
            words = " ".join(clean_words[1:])

            print(f"words = ", words)
            
            if len(clean_words) == 1:
                endpoint = os.environ['TRENDING_ENDPOINT']
                gif_url = await self.find_trending_gif(endpoint)
            else: 
                endpoint = os.environ['SEARCH_ENDPOINT']
                gif_url = await self.find_corresponding_gif(words, endpoint)

            if gif_url:
                await message.channel.send(gif_url)
        

    async def find_corresponding_gif(self, keywords, endpoint) -> str: 
        param = {
            'api_key' : os.environ['GIPHY_API_KEY'],
            'q' : keywords,
            'limit' : 1
        }
        
        async with self.session.get(endpoint, params=param) as response:
            data = await response.json()

        if data:
            return data["data"][0]["images"]["original"]["url"]

        return ""

        
    async def find_trending_gif(self, endpoint) -> str:
        param = {
            'api_key' : os.environ['GIPHY_API_KEY'],
            'limit' : 1
        }

        async with self.session.get(endpoint, params=param) as response:
            data = await response.json()
        
        if data.get("data"):
            return data["data"][0]["images"]["original"]["url"]
        
        return ""
    

    async def close(self):
        if self.session:
            await self.session.close()

        await super().close()


if __name__ == "__main__":
    client = MyClient()
    client.run(os.environ["BOT_TOKEN"])