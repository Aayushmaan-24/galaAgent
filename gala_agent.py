import random
import ddgs
from smolagents import CodeAgent, InferenceClientModel
from tools import DuckDuckGoSearchTool, WeatherInfoTool, HubStatsTool
from retriever import guest_info_tool

# Initialize the Hugging Face model
model = InferenceClientModel()

# Initialize the web search tool
search_tool = DuckDuckGoSearchTool()

# Initialize the weather tool
weather_info_tool = WeatherInfoTool()

# Initialize the Hub stats tool
hub_stats_tool = HubStatsTool()


# Create Alfred with all the tools
alfred = CodeAgent(
    tools=[guest_info_tool, weather_info_tool, hub_stats_tool, search_tool], 
    model=model,
    add_base_tools=True,  # Add any additional base tools
    planning_interval=3   # Enable planning every 3 steps
)

query = "Tell me about 'Lady Ada Lovelace'"
response = alfred.run(query)

print("🎩 Alfred's Response:")
print(response)


query = "What's the weather like in Paris tonight? Will it be suitable for our fireworks display?"
response = alfred.run(query, reset=False)

print("🎩 Alfred's Response:")
print(response)

query = "One of our guests is from Qwen. What can you tell me about their most popular model?"
response = alfred.run(query, reset=False)

print("🎩 Alfred's Response:")
print(response)


query = "I need to speak with Dr. Nikola Tesla about recent advancements in wireless energy. Can you help me prepare for this conversation?"
response = alfred.run(query, reset=False)

print("🎩 Alfred's Response:")
print(response)

