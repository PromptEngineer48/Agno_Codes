from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.newspaper4k import Newspaper4kTools
from agno.models.ollama import Ollama

hn_researcher = Agent(
    name="HackerNews Researcher",
    # model=OpenAIChat("gpt-4o"),
    model=Ollama(id="llama3.2"),
    role="Gets top stories from hackernews.",
    tools=[HackerNewsTools()],
)

web_searcher = Agent(
    name="Web Searcher",
    # model=OpenAIChat("gpt-4o"),
    model=Ollama(id="llama3.2"),
    role="Searches the web for information on a topic",
    tools=[DuckDuckGoTools()],
    add_datetime_to_instructions=True,
)

article_reader = Agent(
    name="Article Reader",
    # model=OpenAIChat("gpt-4o"),
    model=Ollama(id="llama3.2"),
    role="Reads articles from URLs.",
    tools=[Newspaper4kTools()],
)

hn_team = Agent(
    name="Hackernews Team",
    # model=OpenAIChat("gpt-4o"),
    model=Ollama(id="llama3.2"),
    team=[hn_researcher, web_searcher, article_reader],
    instructions=[
        "First, search hackernews for what the user is asking about.",
        "Then, ask the article reader to read the links for the stories to get more information.",
        "Important: you must provide the article reader with the links to read.",
        "Then, ask the web searcher to search for each story to get more information.",
        "Finally, provide a thoughtful and engaging summary.",
    ],
    show_tool_calls=True,
    markdown=True,
)
hn_team.print_response("Write an article about the top 2 stories on hackernews", stream=True)
