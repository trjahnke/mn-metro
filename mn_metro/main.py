import requests
import json


headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

base_url = "http://svc.metrotransit.org/NexTrip/"


class GetProviders(object):
    def __init__(self):
        self.name = "Providers"

    def info(self):
        r = requests.get(url=f"{base_url}{self.name}", headers=headers)
        return r.text

    # add one where it returns a list of all routes by provider

class GetRoutes(object):
    def __init__(self):
        self.name = "Routes"
        self.r = requests.get(url=f"{base_url}{self.name}", headers=headers)

    def all_routes(self):
        data = self.r.json()
        return data

    def route_ids(self):
        data = self.r.json()
        route_ids = []

        for route in data:
            route_ids.append(route["Route"])

        return route_ids

    def route(self, route_id):
        if not hasattr(route_id, "__pow__"):
            raise TypeError(f"{type(route_id)} is an unsupported operand. Should be an int.")

        for item in self.all_routes():
            if int(item["Route"]) == route_id:
                return item
        return f"The provided route_id: {route_id} does not appear in the Routes."


class GetDirections(object):
    """
    Returns the two directions that are valid for a given route. Either North/South or East/West. The result includes text/value pair with the direction name and an ID. Directions are identified with an ID value. 1 = South, 2 = East, 3 = West, 4 = North.
    """

    def __init__(self):
        self.name = "Directions"
    
    def info(self, route):
        self.route = route
        print(self.route)


class GetStops(object):
    def __init__(self):
        pass


class GetDepartures(object):
    def __init__(self):
        pass


class GetTimepointDepartures(object):
    def __init__(self):
        pass


class GetVehicleLocations(object):
    def __init__(self):
        pass
