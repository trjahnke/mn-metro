# Welcome to mnmetro

- [What is mnmetro?](#what-is-mnmetro)
- [Installation](#installation)
    + [Development](#development)
- [Setup](#setup)
- [Functions](#functions)
- [Release Notes](#release-notes)
- [License](LICENSE.md)

<!-- toc -->

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
All you have to do to start using mnmetro is import it. [Then checkout the objects you can initialize!](#functions)
```python
import mnmetro
```

## Functions
There are seven object classes so far each with their own functions. In order to use whatever function that is needed you first need to intialize its parent class object ie:
```python
import mnmetro
...
providers = GetProviders()
routes = GetRoutes()
directions = GetDirections()
providers = GetStops()
departures = GetDepartures()
timepoints = GetTimepointDepartures()
locations = GetVechicleLocations()
...
```

## Release Notes
- [Version: 1.0.0](releases/1-0-0.md)
