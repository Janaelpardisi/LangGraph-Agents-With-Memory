from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langchain.memory import ConversationBufferMemory
from typing import TypedDict
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Define state schema
class AgentState(TypedDict):
    topic: str
    research: str
    summary: str
    feedback: str
    conversation: str

# LLM setup
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.2)
memory = ConversationBufferMemory(memory_key="conversation", return_messages=True)

# Agents
def researcher(state):
    topic = state["topic"]
    history = memory.load_memory_variables({})["conversation"]
    prompt = f"""
    Previous conversation context:
    {history}

    Continue the research if related.
    Provide concise and clear research info about: {topic}.
    """
    response = llm.predict(prompt)
    state["research"] = response
    memory.save_context({"user": topic}, {"assistant": response})
    return state

def summarizer(state):
    info = state["research"]
    history = memory.load_memory_variables({})["conversation"]
    prompt = f"""
    Previous conversation context:
    {history}

    Summarize the following clearly:
    {info}
    """
    summary = llm.predict(prompt)
    state["summary"] = summary
    memory.save_context({"user": "summarize"}, {"assistant": summary})
    return state

def critic(state):
    summary = state["summary"]
    history = memory.load_memory_variables({})["conversation"]
    prompt = f"""
    Previous conversation context:
    {history}

    Review and evaluate this summary for clarity and accuracy:
    {summary}
    """
    feedback = llm.predict(prompt)
    state["feedback"] = feedback
    memory.save_context({"user": "review"}, {"assistant": feedback})
    return state

# Build Graph
graph = StateGraph(AgentState)
graph.add_node("researcher", researcher)
graph.add_node("summarizer", summarizer)
graph.add_node("critic", critic)


graph.add_edge("researcher", "summarizer")
graph.add_edge("summarizer", "critic")
graph.add_edge("critic", END)
graph.set_entry_point("researcher")


app_graph = graph.compile()

def run_agent(topic):
    input_data = {"topic": topic}
    result = app_graph.invoke(input_data)
    return {
        "research": result["research"],
        "summary": result["summary"],
        "feedback": result["feedback"]
    }
