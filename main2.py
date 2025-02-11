## Agents with Tools

from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.arxiv import ArxivTools

agent = Agent(
    model=Ollama(id="llama3.2"),
    # tools=[DuckDuckGoTools()],
    tools=[DuckDuckGoTools(), ArxivTools()],
    show_tool_calls=True,
    markdown=True
)

# Print the response in the terminal
# agent.print_response("What do you think of the Latest news on US deporting migrants.")

agent.print_response("Give me some deepseek-r1's latest news.")

# agent.print_response("What is 23+89.")
# agent.print_response("Search arxiv for 'Reinforcement Learning")

