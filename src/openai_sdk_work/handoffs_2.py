from .configurations import model
import agents


historyTeacher = agents.Agent(
    name="History teacher",
    instructions=(
        "You are a specialized history teacher. You provide clear, concise, and factual answers"
        "to any questions related to history — including historical events, timelines, and important figures."
    ),
    handoff_description="Handles all history-related questions, such as events, people, or timelines.",
    model=model,
)

chemistryTeacher = agents.Agent(
    name="Chemistry teacher",
    instructions=(
        "You are a specialized chemistry teacher. You provide explanations about chemical elements, compounds, reactions,"
        "and general chemistry-related topics in a simple and accurate manner."
    ),
    handoff_description="Handles all chemistry-related questions, such as elements, reactions, and chemical principles.",
    model=model,
)


def onHistoryHandoff(context):
    print("Handing off to history teacher")


def onChemistryHandoff(context):
    print("Handing off to chemistry teacher")


normalTeacher = agents.Agent(
    name="Teacher",
    instructions=(
        "You are a general teacher responsible for deciding how to handle a student's question."
        "- If the question is related to chemistry (e.g., elements, compounds, reactions), hand it off to the Chemistry Teacher."
        "- If the question is related to history (e.g., historical events, people, timelines), hand it off to the History Teacher."
        "- If the question is unrelated to either chemistry or history, provide a helpful general answer yourself."
        "After responding, clearly mention whether you answered the question yourself or which specialized teacher you handed it off to and why."
    ),
    handoffs=[
        agents.handoff(historyTeacher, on_handoff=onHistoryHandoff),
        agents.handoff(chemistryTeacher, on_handoff=onChemistryHandoff),
    ],
    model=model,
)


def runAgent():
    result = agents.Runner.run_sync(
        starting_agent=normalTeacher, input="Who started WW2?, answer in 3 lines."
    )
    print("result:", result.final_output)
