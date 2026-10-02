#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from travel_planner.crew import TravelPlanner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'origin': 'New York',
        'destination': 'Paris',
        'start_date': '2026-06-10',
        'end_date': '2026-06-17',
        'travelers': 2,
        'budget': 4000,
        'currency': 'USD',
        'preferences': 'Interested in museums, local food and walkable neighborhoods.',
    }

    try:
        TravelPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
