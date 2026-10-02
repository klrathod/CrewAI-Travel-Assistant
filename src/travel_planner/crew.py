from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from travel_planner.tools.flight_tool import FlightSearchTool
from travel_planner.tools.hotel_tool import HotelSearchTool
from travel_planner.tools.weather_tool import WeatherLookupTool


@CrewBase
class TravelPlanner():
    """TravelPlanner crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

    @agent
    def flight_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['flight_agent'], # type: ignore[index]
            tools=[FlightSearchTool()],
            verbose=True
        )

    @agent
    def hotel_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['hotel_agent'], # type: ignore[index]
            tools=[HotelSearchTool()],
            verbose=True
        )

    @agent
    def weather_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['weather_agent'], # type: ignore[index]
            tools=[WeatherLookupTool()],
            verbose=True
        )

    @agent
    def budget_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['budget_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def itinerary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['itinerary_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['flight_search_task'], # type: ignore[index]
        )

    @task
    def hotel_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['hotel_search_task'], # type: ignore[index]
        )

    @task
    def weather_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['weather_analysis_task'], # type: ignore[index]
        )

    @task
    def budget_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['budget_analysis_task'], # type: ignore[index]
            context=[self.flight_search_task(), self.hotel_search_task()],
        )

    @task
    def itinerary_task(self) -> Task:
        return Task(
            config=self.tasks_config['itinerary_task'], # type: ignore[index]
            context=[
                self.flight_search_task(),
                self.hotel_search_task(),
                self.weather_analysis_task(),
                self.budget_analysis_task(),
            ],
            output_file='itinerary.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TravelPlanner crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
