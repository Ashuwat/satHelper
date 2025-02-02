from uagents import Agent, Context
from pre_processing import parquet_to_tabular
from sentence_transformer import sentence_transformer

# Define the agent
agent = Agent(name="SentenceTransformerAgent")


@agent.on_event("startup")
async def initialize_storage(ctx: Context):
    ctx.logger.info("Agent has started!")

@agent.on_event("query_received")
async def handle_query(ctx: Context):
    query = ctx.args.get("query", "")  # Query passed from client
    result = sentence_transformer(query)
    ctx.logger.info(f"Transformed query: {result}")
    ctx.storage.set("transformed_query", result)

if __name__ == "__main__":
    agent.run()
