import textbase
from textbase.message import Message
from textbase import models
import os
from typing import List

# Load your OpenAI API key
models.OpenAI.api_key = "my-api-key-here"
# or from environment variable:
# models.OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """Suppose that your name is Pregchat a Gynecology base chat application designed to help women in their pregnancy journey, you are currently deployed there as a chat service in a rural area,, make sure to give simple and easy to understand language as the woman in the rural area are not so well versed in medical or technical terms , also you chat tone should be very loving and caring nature , you should ask follow up questions like name, pregnancy month, age, first birth or not ,and other details related to pregnancy in order to assist them.
"""

# we can use further add to give "concise and precise answer" to have smaller and precise but I prefer longer answer so that the user get better understanding of the conditions .


@textbase.chatbot("talking-bot")
def on_message(message_history: List[Message], state: dict = None):
    """Your chatbot logic here
    message_history: List of user messages
    state: A dictionary to store any stateful information

    Return a string with the bot_response or a tuple of (bot_response: str, new_state: dict)
    """

    if state is None or "counter" not in state:
        state = {"counter": 0}
    else:
        state["counter"] += 1

    # # Generate GPT-3.5 Turbo response
    bot_response = models.OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history,
        model="gpt-3.5-turbo",
    )

    return bot_response, state
