import agents
from .configurations import model

@agents.function_tool
def getWeather(city: str):
    weather = None
    coldCities = ["Moscow", "New York", "London"]
    if city in coldCities:
        weather = "cold"
    else:
        weather = "sunny"
    return f"Weather of {city} is {weather}"


@agents.function_tool
def getTemperature(city: str):
    return f"Temperature of {city} is 35 degrees"


weatherAgent = agents.Agent(
    name="Weather Teller",
    instructions="You are weather agent, you have to tell temperature or weather about provided city.",
    tools=[getWeather, getTemperature],
    model=model
)


def runAgent():
    result = agents.Runner.run_sync(
        starting_agent=weatherAgent,
        input="How is weather and temperature of Karachi?.",
    )
    print("Result:", result.final_output)
