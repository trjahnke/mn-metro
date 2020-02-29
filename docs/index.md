# Welcome to mnmetro

- [What is mnmetro?](#what-is-mnmetro)
- [Installation](#installation)
    + [Development](#development)
- [Setup](#setup)
- [Functions](#functions)
- [Release Notes](#release-notes)
- [License](LICENSE.md)

## What is mnmetro?
mnmetro is a Python3 wrapper built for the Minnesota Metro Tranist API.

## Installation
You can install mnmetro using [pip](https://pypi.org)
```bash
$ pip install mnmetro
```

#### Development
To be add when setup. Otherwise PR's are always welcome.

## Setup
All you have to do to start using mnmetro is import it. [Then checkout the objects you can initialize!](/inner-workings/functions)
```python
import mnmetro
```

## Functions

|___[GetProviders()](/inner-workings/functions/#getproviders)___|___[GetRoutes()](/inner-workings/functions/#getroutes)___|___[GetDirections()](/inner-workings/functions/#getdirections)___|___[GetStops()](/inner-workings/functions/#getstops)___|___[GetDepartures()](/inner-workings/functions/#getdepartures)___|___[GetTimepointDepartures()](/inner-workings/functions/#gettimepointdepartures)___|___[GetVehicleLocations()](/inner-workings/functions/#getvehiclelocations)___
|:---------------:| ------------ | --------------- | ---------------- | ---------------- | ------------------------ | ---------------------
| all_providers() | all_routes() |                 | full_stops_for() | departure_for()  | times_for()              | all_vehicles()
| provider_for()  | route_ids()  |                 | stops_for()      |                  |                          | location_for()
|                 | route_for()  |                 |                  |                  |                          | 

## Release Notes
- [Version: 1.0.0](releases/1-0-0.md)
