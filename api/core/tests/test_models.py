"""
Tests for models.
"""

from django.test import TestCase

from core import models 

from datetime import datetime

def create_airport():
    return models.Airport.objects.create(
        name="Myrtle Beach International",
        airport_code="MYR",
        address="1100 Jetport Rd",
        city="Myrtle Beach",
        state="SC",
        zip_code="29577"
    )


class ModelTests(TestCase):

    def test_create_airport(self):
        """Test Creating an Airport is Successful."""
        airport = models.Airport.objects.create(
            name="Myrtle Beach International",
            airport_code="MYR",
            address="1100 Jetport Rd",
            city="Myrtle Beach",
            state="SC",
            zip_code="29577"
        )

        self.assertEqual(str(airport), airport.name)


    def test_create_airline(self):
        """Test Creating an Airline is Successful."""
        airline = models.Airline.objects.create(
            name="Delta Airlines",
            airline_code="DL"
        )

        self.assertEqual(str(airline), airline.name)

    def test_create_runway(self):
        """Test Creating a Runway is Successful."""
        runway = models.Runway.objects.create(
            airport = create_airport(),
            runway_number = 18,
            runway_designation = "N",
            length=5000,
            width=5000
        )

        self.assertEqual(str(runway), str(runway.runway_number)+runway.runway_designation)


    def test_create_flight(self):
        """Test Creating a Flight is Successful."""
        airline = models.Airline.objects.create(
            name='Delta Airlines',
            airline_code='DL'
        )

        flight = models.Flight.objects.create(
            origin = create_airport(),
            destination = create_airport(),
            airline = airline,
            flight_number = 1954,
            departure = datetime.now(),
            arrival = datetime.now(),
            aircraft_type = 'B747',
        )

        self.assertEqual(str(flight), flight.airline.airline_code + str(flight.flight_number))