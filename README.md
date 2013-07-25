brightinthesky
==============

An api running on [web2py](http://web2py.com/) that uses [PyEphem](http://rhodesmill.org/pyephem/index.html) to return information for the brightest astronomical bodies in the sky for a given time and location.

Pass latitude, longitude, and date/time to get a JSON or XML result containing rise/set times, transit times, altitude, azimuth, and magnitude for the Sun, Moon, Mercury, Venus, Mars, Jupiter, Saturn, Sirius, Arcturus, Vega, Capella, and Rigel.

Returns values for Naval Observatory sunrise and sunset times, as well as civil and astronomical twilight.  All date/times are passed and returned in ISO 8601 format in UTC.

See the [documentation for PyEphem](http://rhodesmill.org/pyephem/index.html) for more information about the values returned.

Example XML call and result:

http://brightinthesky.sightingsreport.com/astro/api/lookup.xml?lat=27.955591&lng=-82.24914551&dateTime=2000-03-05T12:00:00Z

And JSON:

http://brightinthesky.sightingsreport.com/astro/api/lookup.json?lat=27.955591&lng=-82.24914551&dateTime=2000-03-05T12:00:00Z
