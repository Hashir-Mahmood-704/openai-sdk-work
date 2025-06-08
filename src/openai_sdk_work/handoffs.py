from .configurations import model
import agents
import pydantic


class HistorianSingleOutput(pydantic.BaseModel):
    country: str
    paragraph: str


historianAgent = agents.Agent(
    name="Historian",
    instructions=(
        "You are a historian agent. You will be given a list of country names, "
        "and for each country, you must write a short paragraph (maximum 4 lines) "
        "summarizing an interesting historical fact or background about it. "
        "Also, print the list of countries you received at the top of your response."
    ),
    output_type=list[HistorianSingleOutput],
    model=model,
)

countryPicker = agents.Agent(
    name="Country Selector",
    instructions=(
        "You are a country selector agent. When given the name of a continent, "
        "you must select three real countries from that continent. Then, pass the list "
        "of selected country names to the Historian agent for further processing."
    ),
    handoffs=[historianAgent],
    model=model,
)


def runAgent():
    result = agents.Runner.run_sync(starting_agent=countryPicker, input="Asia")
    print("Result:", result.final_output)
