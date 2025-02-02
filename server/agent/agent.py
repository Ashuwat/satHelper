from agent.sentenceTransformer import sentenceTransformer
from uagents import Agent, Context
import asyncio

agent = Agent(name="TST")

@agent.on_event("startup")
async def initialize_storage(ctx: Context):
    current_count = ctx.storage.get("count")
    ctx.logger.info(f"My count is: {current_count}")
    ctx.storage.set("count", current_count + 1)

async def manual_run(context: Context):
    result = sentenceTransformer()
    context.logger.info(f"{result}")
 
agent.run()
asyncio.run(manual_run(agent.context))
