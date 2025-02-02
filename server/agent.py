from uagents import Agent, Context, Model

# Define the query model
class QueryRequest(Model):
    query: str

class QueryResponse(Model):
    response: str

agent = Agent(name="QueryProcessor")

def x(query: str) -> str:
    return f"Processed: {query}"  # Modify this function as needed

@agent.on_message(model=QueryRequest, replies=QueryResponse)
async def handle_query(ctx: Context, sender: str, msg: QueryRequest):
    ctx.logger.info(f"Received query: {msg.query}")
    
    processed_query = x(msg.query)
    
    response_msg = QueryResponse(response=processed_query)
    await ctx.send(sender, response_msg)

if __name__ == "__main__":
    agent.run()
