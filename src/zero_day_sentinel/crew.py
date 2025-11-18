import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from zero_day_sentinel.tools.custom_tool import CVESearchTool
from crewai.llm import LLM


@CrewBase
class ZeroDaySentinel:
    """ZeroDay Sentinel - Autonomous Vulnerability Research & Patch Crew"""

    def __init__(self):
        self.search_tool = SerperDevTool()
        self.gemini_llm = LLM(
            model="gemini/gemini-2.5-flash",
            api_key=os.getenv("GEMINI_API_KEY"),
            temperature=0.1,
            max_tokens=1000,
        )

    @agent
    def threat_hunter(self) -> Agent:
        return Agent(
            config=self.agents_config["threat_hunter"],
            tools=[self.search_tool],
            verbose=True,
            llm=self.gemini_llm,
        )

    @agent
    def exploit_developer(self) -> Agent:
        return Agent(
            config=self.agents_config["exploit_developer"],
            tools=[self.search_tool],
            verbose=True,
            llm=self.gemini_llm,
        )

    @agent
    def patch_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["patch_engineer"],
            verbose=True,
            llm=self.gemini_llm,
        )

    @agent
    def security_comms(self) -> Agent:
        return Agent(
            config=self.agents_config["security_comms"],
            verbose=True,
            llm=self.gemini_llm,
        )

    @task
    def threat_hunt_task(self) -> Task:
        return Task(
            config=self.tasks_config["threat_hunt_task"], agent=self.threat_hunter()
        )

    @task
    def exploit_development_task(self) -> Task:
        return Task(
            config=self.tasks_config["exploit_development_task"],
            agent=self.exploit_developer(),
        )

    @task
    def patch_development_task(self) -> Task:
        return Task(
            config=self.tasks_config["patch_development_task"],
            agent=self.patch_engineer(),
        )

    @task
    def advisory_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config["advisory_creation_task"],
            agent=self.security_comms(),
            output_file="reports/security_advisory.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            memory=False,
            max_rpm=100,
        )
