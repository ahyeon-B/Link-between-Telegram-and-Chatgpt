from openai import OpenAI
import telegram
import asyncio

client = OpenAI(
    api_key="YOUR_OPENAI_API_KEY"
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "WRITE_MESSAGE!"} 
  ],
)

async def send_telegram_message():
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    bot = telegram.Bot(token=token)
    chat_id = "6440619064"
    text = completion.choices[0].message.content
    await bot.sendMessage(chat_id=chat_id, text=text)

async def main():
    await send_telegram_message()

if __name__ == "__main__":
    asyncio.run(main())
