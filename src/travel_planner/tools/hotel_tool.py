from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class HotelSearchInput(BaseModel):
    """Input schema for HotelSearchTool."""
    destination: str = Field(..., description="City to search hotels in.")
    start_date: str = Field(..., description="Check-in date (YYYY-MM-DD).")
    end_date: str = Field(..., description="Check-out date (YYYY-MM-DD).")
    budget: float = Field(..., description="Total trip budget available for accommodation.")


class HotelSearchTool(BaseTool):
    name: str = "Hotel Search Tool"
    description: str = (
        "Searches for hotel options in a destination city for the given stay dates "
        "and budget. Returns a list of candidate hotels with location, rating, "
        "amenities and price."
    )
    args_schema: Type[BaseModel] = HotelSearchInput

    def _run(self, destination: str, start_date: str, end_date: str, budget: float) -> str:
        # TODO: Replace with a real hotel search API (e.g. Amadeus, Booking.com, Expedia).
        return (
            f"Sample hotel options in {destination} ({start_date} - {end_date}, "
            f"budget {budget}):\n"
            f"1. City Center Hotel - 4 stars - Free WiFi, Breakfast - $120/night\n"
            f"2. Budget Inn - 3 stars - Free WiFi - $70/night\n"
            f"3. Luxury Suites - 5 stars - Pool, Spa, Breakfast - $220/night"
        )
