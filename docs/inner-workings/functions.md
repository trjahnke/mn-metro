# Classes and Functions

[TOC]

There are seven object classes so far each with their own functions. In order to use whatever function that is needed you first need to initialize its parent class object ie:

## GetProviders()

```python
import mnmetro
...
P = GetProviders()
...
```

GetProviders has two builtin functions after initialization:

### all_providers()

```python
...
P.all_providers()
...
```

all_providers() returns a dictionary with provider ids as keys and provider names as values.

```json
{   1: 'University of Minnesota',
    2: 'Airport (MAC)',
    3: 'Other',
    4: 'Prior Lake',
    5: 'Scott County',
    6: 'Metro Transit/Met Council',
    7: 'SouthWest Transit',
    8: 'Metro Transit',
    9: 'Minnesota Valley',
    10: 'Plymouth',
    11: 'Met Council',
    12: 'Maple Grove'}
```

### provider_for()

provider_for() takes one of two arguments. Either a `name=<str>` or a `id=<int>` and will return the reverse for what is given.

```python
...
P.provider_for(name="University of Minnesota")
1 # Output

P.provider_for(id=4)
"Prior Lake" # Output
...
```

## GetRoutes()

```python
import mnmetro
...
routes = GetRoutes()
...
```

## GetDirections()

```python
import mnmetro
...
directions = GetDirections()
...
```

## GetStops()

```python
import mnmetro
...
providers = GetStops()
...
```

## GetDepartures()

```python
import mnmetro
...
departures = GetDepartures()
...
```

## GetTimepointDepartures()

```python
import mnmetro
...
timepoints = GetTimepointDepartures()
...
```

## GetVehicleLocations()

```python
import mnmetro
...
locations = GetVechicleLocations()
...
```
