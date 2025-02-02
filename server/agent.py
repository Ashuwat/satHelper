from uagents import Agent, Context, Model

# Define the query model
class QueryRequest(Model):
    query: str

class QueryResponse(Model):
    response: str

# Create the uAgent
agent = Agent(name="QueryProcessor")

# Function 'x' that processes the query
def x(query: str) -> str:
    return f"Processed: {query}"  # Modify this function as needed

# Define the behavior when receiving a query
@agent.on_message(model=QueryRequest, replies=QueryResponse)
async def handle_query(ctx: Context, sender: str, msg: QueryRequest):
    ctx.logger.info(f"Received query: {msg.query}")
    
    # Call function 'x' and get the response
    processed_query = x(msg.query)
    
    # Send back the processed query
    response_msg = QueryResponse(response=processed_query)
    await ctx.send(sender, response_msg)

# Run the agent
if __name__ == "__main__":
    agent.run()
