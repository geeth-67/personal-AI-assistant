from app import run_agent
import gradio as gr


def chat(user_query):
    return run_agent(user_query)

ui = gr.Interface(
    fn=chat,
    inputs=[gr.Textbox(lines=2 , placeholder="Ask questions about news .....")],
    outputs=gr.Textbox(lines=15),
    title="CClarke AI Assistant"
)
ui.launch("app.py")