from typing_extensions import TypeDict


class AgentState(TypeDict):
    input: str
    route: str
    response: str
    blocked: bool