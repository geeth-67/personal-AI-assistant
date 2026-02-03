from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

from system_prompts import ROUTER_AGENT_SYSTEM_PROMPT, NEWS_SYSTEM_PROMPT
load_dotenv()

llm = ChatOpenAI(model="gpt-4.1-mini-2025-04-14")

def router_agent(state):
    prompt = ChatPromptTemplate.from_messages([
        ("system", ROUTER_AGENT_SYSTEM_PROMPT),
        ("human" , "{input}")
    ])
    routing_chain = prompt | llm

    routing_category = routing_chain.invoke({"input" : state["input"]})

    return {"route" : routing_category.content}

def news_agent(state):
    web_search_tool = TavilySearch(max_results=5)
    agent = create_agent(
        model="gpt-4.1-mini-2025-04-14",
        system_prompt=NEWS_SYSTEM_PROMPT,
        tools=[web_search_tool]
    )

    result = agent.invoke({
        "messages" : [{
            "role" : "user",
            "content" : state["input"]
        }]
    })

    return {"response" : result["messages"][-1].content}