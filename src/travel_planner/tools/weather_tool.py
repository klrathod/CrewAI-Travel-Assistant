from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class WeatherLookupInput(BaseModel):
    """Input schema for WeatherLookupTool."""
    destination: str = Field(..., description="City to look up weather for.")
    start_date: str = Field(..., description="Start of the travel period (YYYY-MM-DD).")
    end_date: str = Field(..., description="End of the travel period (YYYY-MM-DD).")


class WeatherLookupTool(BaseTool):
    name: str = "Weather Lookup Tool"
    description: str = (
        "Looks up typical or forecast weather conditions for a destination during "
        "a given travel period. Returns expected temperature range and conditions."
    )
    args_schema: Type[BaseModel] = WeatherLookupInput

    def _run(self, destination: str, start_date: str, end_date: str) -> str:
        # TODO: Replace with a real weather API (e.g. OpenWeatherMap, WeatherAPI).
        return (
            f"Sample weather outlook for {destination} ({start_date} - {end_date}):\n"
            f"Average temperature: 18-26C, mostly sunny with a chance of light rain.\n"
            f"Pack: light layers, a rain jacket and comfortable walking shoes."
        )
