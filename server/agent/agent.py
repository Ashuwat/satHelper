from uagents import Agent, Context
from sentence_transformer import sentence_transformer
agent = Agent(name="bob")
 
@agent.on_event("startup")
async def initialize_storage(ctx: Context):
    ctx.storage.set("count", 0)
 
@agent.on_interval(period=1.0)
async def on_interval(ctx: Context):
    current_count = ctx.storage.get("count")
    ctx.logger.info(f"My count is: {current_count}")
    ctx.storage.set("count", current_count + 1)
 
agent.run()
