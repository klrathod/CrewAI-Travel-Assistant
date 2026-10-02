from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class FlightSearchInput(BaseModel):
    """Input schema for FlightSearchTool."""
    origin: str = Field(..., description="Departure city or airport code.")
    destination: str = Field(..., description="Arrival city or airport code.")
    start_date: str = Field(..., description="Outbound travel date (YYYY-MM-DD).")
    end_date: str = Field(..., description="Return travel date (YYYY-MM-DD).")


class FlightSearchTool(BaseTool):
    name: str = "Flight Search Tool"
    description: str = (
        "Searches for flight options between an origin and a destination for the "
        "given travel dates. Returns a list of candidate flights with airline, "
        "price, duration and number of stops."
    )
    args_schema: Type[BaseModel] = FlightSearchInput

    def _run(self, origin: str, destination: str, start_date: str, end_date: str) -> str:
        # TODO: Replace with a real flight search API (e.g. Amadeus, Skyscanner, Kiwi).
        return (
            f"Sample flight options from {origin} to {destination} "
            f"({start_date} - {end_date}):\n"
            f"1. Airline A - Nonstop - 6h 30m - $450 round trip\n"
            f"2. Airline B - 1 stop - 9h 15m - $320 round trip\n"
            f"3. Airline C - 1 stop - 10h 45m - $290 round trip"
        )
