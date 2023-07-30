# Textbase

✨ Textbase is a framework for building chatbots using NLP and ML. ✨

Just implement the `on_message` function in `main.py` and Textbase will take care of the rest :)

Since it is just Python you can use whatever models, libraries, vector databases and APIs you want.

_Coming soon:_

- [ ] PyPI package
- [ ] SMS integration
- [ ] Easy web deployment via `textbase deploy`
- [ ] Native integration of other models (Claude, Llama, ...)

## Installation

Clone the repository and install the dependencies using [Poetry](https://python-poetry.org/) (you might have to [install Poetry](https://python-poetry.org/docs/#installation) first).

```bash
git clone https://github.com/cofactoryai/textbase
cd textbase
poetry install
```

## Start development server

> If you're using the default template, **remember to set the OpenAI API key** in `main.py`.

Run the following command:

```bash
poetry run python textbase/textbase_cli.py test main.py
```

# Prompt for GPT-3.5 Turbo
'''python
SYSTEM_PROMPT = """Suppose that your name is Pregchat, a Gynecology-based chat application designed to help women in their pregnancy journey. You are currently deployed as a chat service in a rural area, where the women may not be well-versed in medical or technical terms. Your chat tone should be very loving and caring in nature. Please ask follow-up questions, such as name, pregnancy month, age, first birth or not, and other details related to pregnancy, in order to assist them.
"""

# We can use further add to give "concise and precise answer" to have smaller and precise but I prefer longer answers so that the user gets a better understanding of the conditions.
'''


Now go to [http://localhost:4000](http://localhost:4000) and start chatting with your bot! The bot will automatically reload when you change the code.

_Simpler version using PyPI package and CLI coming soon!_

## Contributions

Contributions are welcome! Please open an issue or a pull request.
