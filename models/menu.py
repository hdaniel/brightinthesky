# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A('BrightInTheSky', _class="brand",_href="/")
response.title = 'Bright in the Sky'
response.subtitle = 'a web api for bright astronomical bodies'

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'SightingsReport.com'
response.meta.description = 'This is a web api to return the brightest astronomical bodies in the sky for a given time and location. It is a web api to the PyEphem python package.'
response.meta.keywords = 'astronomy, bright objects in the sky'
response.meta.generator = ''

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    ('on GitHub', False, 'https://github.com/hdaniel/brightinthesky', [])
]

