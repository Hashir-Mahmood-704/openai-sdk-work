import dotenv
import os
import agents

dotenv.load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise Exception("GEMINI KEY not found")

# we need to setup an external and custom client if we are using a non-openai LLM model
# as we are using GEMINI Model, i am making a custom client
customClient = agents.AsyncOpenAI(  # type: ignore
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=GEMINI_API_KEY,
)

agents.set_default_openai_client(customClient)
agents.set_tracing_disabled(True)

model = agents.OpenAIChatCompletionsModel(
    model="gemini-2.0-flash", openai_client=customClient
)
