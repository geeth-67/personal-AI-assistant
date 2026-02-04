# from envs.tf.Lib.typing import TypedDict
from typing import TypedDict

from langgraph.constants import START, END
from langgraph.graph import StateGraph

from agents import news_agent, router_agent
from guardralls import input_guardrail


class AgentState(TypedDict):
    input : str
    route : str
    response : str
    blocked : bool

def input_decision(state):
    if state["blocked"]:
        return "end"
    return "router"

def router_decision(state):
    if state["route"] == "news":
        return "news"
    return "end"

graph = StateGraph(AgentState)

graph.add_node("input_guard", input_guardrail)
graph.add_node("news_agent", news_agent)
graph.add_node("router_agent", router_agent)

# graph.add_edge(START, "input_guard")
graph.set_entry_point("input_guard")
graph.add_conditional_edges("input_guard", input_decision,
                            {"router": "router_agent", "end" : END})
graph.add_conditional_edges("router_agent", router_decision,
                            {"news" : "news_agent", "end" : END})
graph.add_edge("news_agent", END)

ai_assistant_compiled = graph.compile()



def router_decision(state):
    if state["route"] == "news":
        return "news"
    elif state["route"] == "scam":
        return "scam"
    else:
        return "news"

graph.add_conditional_edges("router", router_decision,
                            {"news": "news_agent",
                                     "scam" : "scam_agent"})

graph.add_edge("news_agent", END)
graph.add_edge("scam_agent" , END)

compiled_graph = graph.compile()