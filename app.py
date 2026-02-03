from graph import ai_assistant_compiled


def run_agent(user_query : str):
    resp = ai_assistant_compiled.invoke({
        "input" : user_query
    })

    if resp.get("blocked"):
        return "Identified Blocked content" + resp.get("response")

    return resp.get("response")



if __name__ == "__main__":
    while True:
        user_query = input("Enter your prompt : ")

        print(run_agent(user_query))