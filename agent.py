from crewai import Agent, Task, Crew
from tools import yt_tool
from dotenv import load_dotenv
import os

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPEN_MODEL_NAME"] = "gpt-4-0125-preview"



## Create a Senior Blog Content Researcher 

blog_researcher=Agent(
    role='Blog Creator from Youtube Videos',
    goal='Get the relevant video content for the topic{topic} from Yt channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in Ai, Data Science, Machine Learning and Generative Ai and providing suggestion"
    ), 
    tool=[yt_tool],
    llm=llm,
    allow_delegation=True
)

## Creating a Senior blog Writer Agent with YT tool 
blog_writer=Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "Engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=False
) 
