from .configurations import model
import agents


simpleAgent = agents.Agent(name="Helper", instructions="You are a simple instructor helper", model=model)


def runAgent():
    output = agents.Runner.run_sync(
        starting_agent=simpleAgent, input="How are you? What is capital of Iraq?"
    )
    print("Output:", output.final_output)

