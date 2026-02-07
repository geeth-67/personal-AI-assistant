def input_guardrail(state):

    input_text = state["input"]
    blocked_words = [
        "Bomb" , "Weapon" ,"Drugs" , "Hack" , "Explosives"
    ]

    for word in blocked_words:
        if word in input_text:
            return {"Blocked" : True , "response" : "Blocked - Detected Harmful content"}

    return {"blocked" : False}
