# Classes and Functions

[TOC]

There are seven object classes so far each with their own functions. In order to use whatever function that is needed you first need to initialize its parent class object ie:

## GetProviders()

```python
from mnmetro import *
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
from mnmetro import *
...
R = GetRoutes()
...
```

### all_routes()

```python
from mnmetro import *
...
R.all_routes()
...
```

all_routes() doesn't take in any arguments, but when called will return a list of dictionaries. Each dictionary in the list is comprised of key values `"Description":<str>` describing the route, `"ProviderID":<int>` for the designated provider, and finally the `"Route":<int>` describing the route number. Example:

```JSON
    {   'Description': '716 - Zane Av - 63rd Av - Crystal - Robbinsdale',
        'ProviderID': 11,
        'Route': 716},
```

### route_ids()

```python
from mnmetro import *
...
R.route_ids()
...
```

route_ids() doesn't take in any arguments, but when called will return a list of all available route ids as `<int>`. Example:

```JSON
[   2,
    3,
    4,
    5,
    6,
    7,
    9]
```

### route_for()

```python
from mnmetro import *

R = GetRoutes()

R.route_for(route_id=3)
```

route_for() takes in one argument and that is an `<int>` for the route_id. You can either simply pass through the integar or pass it through as `route_id=<int>` both ways will work. This will return a full route information for the given route_id.

This will return the following:

```JSON
{   'Description': '3 - U of M - Como Av - Energy Park Dr - Maryland Av',
    'ProviderID': 8,
    'Route': 3}

```

The same structure of that returned in [all_routes()](#all_routes)

## GetDirections()

```python
from mnmetro import *

D = GetDirections()

D.direction_for(route_id=3)
```

GetDirections() only has one function which is used to get the directions of the given route. Either Northbound/Southbound or Eastbound/Westbound. The output is a dictionary with two keys, either Northbound/Southbound or Eastbound/Westbound and two corresponding `<int>` values which correspond with the following: North = 4, South = 1, East = 2, and West = 3.
Example output:

```JSON
{'EASTBOUND': 2, 'WESTBOUND': 3}
```

## GetStops()

```python
from mnmetro import *
...
S = GetStops()
...
```

### full_stops_for()

```python
from mnmetro import *

S = GetStops()

S.full_stops_for(route_id=<int>)
```

full_stops_for() takes in one argument as the route_id(`<int>`). It returns a dictionary with two key value pairs. Each key is that routes direction, so either Northbound/Southbound or Eastbound/Westbound. Their values are dictionaries of the upcoming stops for that route_id and it's corresponding direction. Example:

```python
from mnmetro import *

S = GetStops()

S.full_stops_for(route_id=3)

<<<<<<<<<<OUTPUT>>>>>>>>>
{   'Eastbound': {   '4th St  and Nicollet Mall': '4NIC',
                     'Anderson Hall ': 'ANHA',
                     'Capitol/Rice St Station ': 'RIUN',
                     'Cedar St and 5th St': '5CED',
                     'Como Ave and Eustis St': 'COES',
                     'Como Ave and Hamline Ave': 'HLCO',
                     'Como Ave and Raymond Ave': 'COCL',
                     'Como Ave and Snelling Ave': 'COSN',
                     'Front Ave and Dale St': 'DAFR',
                     'Front Ave and Lexington Pkwy': 'FRLE',
                     'Jones Hall and Eddy Hall ': 'JOED',
                     'Kasota Ave and Kasota Circle': 'KACR',
                     'Maryland Ave and Dale St': 'MDAL',
                     'Maryland Ave and Rice St': 'MARI',
                     'Norris Circle and Energy Park Dr': 'ELNO',
                     'Ramp B/5th St  Transit Center': '5GAR',
                     'Union Depot ': 'UNDP'},
    'Westbound': {   '3rd St and Hennepin Ave': '3SHE',
                     '7th St & Nicollet Station (Late Night)': '7SNI',
                     'Capitol/Rice St Station ': 'RIUN',
                     'Como Ave and Cleveland Ave': 'COCL',
                     'Como Ave and Eustis St': 'COES',
                     'Como Ave and Hamline Ave': 'HLCO',
                     'Como Ave and Snelling Ave': 'COSN',
                     'Front Ave and Dale St': 'DAFR',
                     'Front Ave and Lexington Pkwy': 'FRLE',
                     'Jones Hall and Eddy Hall ': 'JOED',
                     'Kasota Ave and Kasota Circle': 'KACR',
                     'Maryland Ave and Dale St': 'MDAL',
                     'Maryland Ave and Rice St': 'MARI',
                     'Minnesota St and 4th St': '4MIN',
                     'Norris Circle and Energy Park Dr': 'ELNO',
                     'Ramp B/5th St  Transit Center': '5GAR',
                     'Union Depot ': 'UNDP',
                     'Willey Hall ': 'WIHA'}}
<<<<<<<<<<<<>>>>>>>>>>
```

### stops_for()

```python
from mnmetro import *

S = GetStops()

S.stops_for(route_id=<int>, direction=<int>)
```

stops_for() will only return a single dictionary with that routes upcoming directions on it's corresponding direction. Directions are `<int>`s with the [following pattern](#getdirections). Example:

```python
from mnmetro import *

S = GetStops()

S.stops_for(route_id=3, direction=2)

<<<<<<<<<<OUTPUT>>>>>>>>>
{   '4th St  and Nicollet Mall': '4NIC',
    'Anderson Hall ': 'ANHA',
    'Capitol/Rice St Station ': 'RIUN',
    'Cedar St and 5th St': '5CED',
    'Como Ave and Eustis St': 'COES',
    'Como Ave and Hamline Ave': 'HLCO',
    'Como Ave and Raymond Ave': 'COCL',
    'Como Ave and Snelling Ave': 'COSN',
    'Front Ave and Dale St': 'DAFR',
    'Front Ave and Lexington Pkwy': 'FRLE',
    'Jones Hall and Eddy Hall ': 'JOED',
    'Kasota Ave and Kasota Circle': 'KACR',
    'Maryland Ave and Dale St': 'MDAL',
    'Maryland Ave and Rice St': 'MARI',
    'Norris Circle and Energy Park Dr': 'ELNO',
    'Ramp B/5th St  Transit Center': '5GAR',
    'Union Depot ': 'UNDP'}
<<<<<<<<<<<<<<>>>>>>>>>>>>>>
```

## GetDepartures()

GetDepartures() only has one builtin function called departure_for(). This function only takes in one arguement which is in `<int>` for the stop_id. At the moment I don't have a database or anything with all the stops in them. So if you need to look one up because you don't know the id you can find the publicly available data set for it [here](https://gisdata.mn.gov/dataset/us-mn-state-metc-trans-transit-schedule-google-fd).

### departure_for()

The return of departure_for() is a list of dictionaries for the upcoming departures from the given stop. The schema for the response is as follows, taken from [here the API docs](https://svc.metrotransit.org/nextrip):

> __Actual__ : bool indicates the departure time is based on current information from the vehicle <br>
> __BlockNumber__ : indicates the work for a vehicle <br>
> __DepartureText__ : displays time format for scheduled time and countdown format for real-time departures. (Actual=true) <br>
> __DepartureTime__ : datetime value of the departure time <br>
> __Description__ : describes the trip destination <br>
> __Gate__ : indicates the stop or gate identifier where applicable <br>
> __Route__ : the current route for this departure <br>
> __RouteDirection__ : the current trip direction <br>
> __Terminal__ : the route branch letter where applicable <br>
> __VehicleHeading__ : this value is currently not available and always returns 0. (maybe someday) <br>
> __VehicleLatitude__ : last reported latitude. only included with real-time departures. (Actual=true) <br>
> __VehicleLongitude__ : last reported longitude. only included with real-time departures. (Actual=true) <br>

```python
from mnmetro import *

D = GetDepartures()

D.departure_for(stop_id=1000)

<<<<<<<<<OUTPUT>>>>>>>>>
[   {   'Actual': True,
        'BlockNumber': 1292,
        'DepartureText': '3 Min',
        'DepartureTime': '/Date(1583008560000-0600)/',
        'Description': '46St-42St/St. Paul-7St/Via Bryant',
        'Gate': '',
        'Route': '46',
        'RouteDirection': 'EASTBOUND',
        'Terminal': 'E',
        'VehicleHeading': 0,
        'VehicleLatitude': 44.91258,
        'VehicleLongitude': -93.32927},
    {   'Actual': False,
        'BlockNumber': 1290,
        'DepartureText': '3:05',
        'DepartureTime': '/Date(1583010300000-0600)/',
        'Description': '46St-42St/St. Paul-7St/Via Bryant',
        'Gate': '',
        'Route': '46',
        'RouteDirection': 'EASTBOUND',
        'Terminal': 'E',
        'VehicleHeading': 0,
        'VehicleLatitude': 44.91971,
        'VehicleLongitude': -93.2759},]
<<<<<<<<<<<<>>>>>>>>>>>>
```

## GetTimepointDepartures()

GetTimepointDepartures() is similar to GetDepartures() with the difference being it's return is a little more detailed as it only returns data for the stop for a directioned route parameter. This class is still in progress to make it a better solution. Please stay tuned.

### times_for()
Takes in three arguments: route_id=`<int>` for the route id, direction=`<int>` for the direction of the route North/South, East/West, and finally node_id=`<str>` which is the node identification of a stop which can be found from the stops_for() function. Future work will be put into making a more accessible version of node ids.

```python
from mnmetro import *

T = GetTimepointDepartures()

T.times_for(route_id=5, direction=4, stop_id="7SOL")

<<<<<<<<<OUTPUT>>>>>>>>>
[   {   'Actual': True,
        'BlockNumber': 1044,
        'DepartureText': '3 Min',
        'DepartureTime': '/Date(1583010840000-0600)/',
        'Description': 'Fremont Av/Brklyn Ctr/Transit Ctr',
        'Gate': '',
        'Route': '5',
        'RouteDirection': 'NORTHBOUND',
        'Terminal': 'M',
        'VehicleHeading': 0,
        'VehicleLatitude': 44.97883,
        'VehicleLongitude': -93.27684},
    {   'Actual': True,
        'BlockNumber': 1060,
        'DepartureText': '18 Min',
        'DepartureTime': '/Date(1583011740000-0600)/',
        'Description': 'Fremont Av/Brklyn Ctr/Transit Ctr',
        'Gate': '',
        'Route': '5',
        'RouteDirection': 'NORTHBOUND',
        'Terminal': 'M',
        'VehicleHeading': 0,
        'VehicleLatitude': 44.95753,
        'VehicleLongitude': -93.2626}]
<<<<<<<<<<<<>>>>>>>>>>>>
```

## GetVehicleLocations()

```python
from mnmetro import *
...
locations = GetVechicleLocations()
...
```

GetVehicleLocations() has two functions one for returning all vehicles out and one to return only those on a given route. 
> __As a Note:__
> Bearing, Odometer, and Speed are not yet being used on all vehicles and thus can't be trusted to be accurate or included on all responses. Metro says they are coming in the future.

### all_vehicles()

all_vehicles() doesn't take in any arguments and returns a list of dictionaries with data about vehicles in use.

```python
from mnmetro import *

L = GetVehicleLocations()

L.all_routes()

<<<<<<<<<<OUTPUT>>>>>>>>>>
[   {   'Bearing': 178,
        'BlockNumber': 34514,
        'Direction': 3,
        'LocationTime': '/Date(1583013020000-0600)/',
        'Odometer': 0,
        'Route': '495',
        'Speed': 0,
        'Terminal': 'A',
        'VehicleLatitude': 44.854071,
        'VehicleLongitude': -93.238187},
    {   'Bearing': 180,
        'BlockNumber': 34554,
        'Direction': 4,
        'LocationTime': '/Date(1583012925000-0600)/',
        'Odometer': 0,
        'Route': '903',
        'Speed': 26.8224,
        'Terminal': '',
        'VehicleLatitude': 44.84833,
        'VehicleLongitude': -93.24772}]
<<<<<<<<<<<<<>>>>>>>>>>>>>
```

### location_for()

location_for() takes in one argument, route_id=`<int>` and returns a list or dictionaries for vehicles on the given route.

```python
from mnmetro import *

L = GetVehicleLocations()

L.location_for(route_id=3)

<<<<<<<<<<OUTPUT>>>>>>>>>>
[   {   'Bearing': 270,
        'BlockNumber': 1018,
        'Direction': 3,
        'LocationTime': '/Date(1583013197000-0600)/',
        'Odometer': 0,
        'Route': '3',
        'Speed': 8.9408,
        'Terminal': '',
        'VehicleLatitude': 44.98786,
        'VehicleLongitude': -93.2275},
    {   'Bearing': 90,
        'BlockNumber': 1019,
        'Direction': 2,
        'LocationTime': '/Date(1583013200000-0600)/',
        'Odometer': 0,
        'Route': '3',
        'Speed': 11.176,
        'Terminal': 'S',
        'VehicleLatitude': 44.97693,
        'VehicleLongitude': -93.17916}]

<<<<<<<<<<<<<>>>>>>>>>>>>>
```

