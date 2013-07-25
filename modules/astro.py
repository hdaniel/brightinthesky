import ephem
import dateutil.parser
from datetime import date, datetime


# set to Naval Observatory settings
# see: http://rhodesmill.org/pyephem/rise-set.html#naval-observatory-risings-and-settings
def standard_pressure():
    pressure = 0
    return pressure

def standard_horizon():
    horizon = '-0:34'
    return horizon

# twilight
# see: http://rhodesmill.org/pyephem/rise-set.html#naval-observatory-risings-and-settings
def civil_horizon():
    horizon = '-6'
    return horizon

def astronomical_horizon():
    horizon = '-18'
    return horizon

def to_date_time(ephem_date):
    return datetime.strptime(str(ephem_date), "%Y/%m/%d %H:%M:%S").isoformat()


class Astro(object):

    def __init__(self, lat, lng, date_time, extra_args={}):
        self.observed_location = ephem.Observer()
        self.observed_location.lat = lat
        self.observed_location.lon = lng
        self.observed_location.date = dateutil.parser.parse(date_time)
        self.observed_location.pressure = standard_pressure()
        self.observations = {}

    def observe(self, extra_args={}):
        self.sun_observations()
        self.civil_observations()
        self.astronomical_observations()
        self.moon_observations()
        self.venus_observations()
        self.jupiter_observations()
        self.mars_observations()
        self.saturn_observations()
        self.mercury_observations()
        self.sirius_observations()
        self.arcturus_observations()
        self.vega_observations()
        self.capella_observations()
        self.rigel_observations()

    def sun_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        try:
            self.observations["previous_sunrise"] = to_date_time(self.observed_location.previous_rising(ephem.Sun()))
        except Exception, e:
            self.observations["previous_sunrise"] = ""
        try:
           self.observations["next_sunrise"] = to_date_time(self.observed_location.next_rising(ephem.Sun()))
        except Exception, e:
           self.observations["next_sunrise"] = ""
        try:
           self.observations["previous_sunset"] = to_date_time(self.observed_location.previous_setting(ephem.Sun()))
        except Exception, e:
           self.observations["previous_sunset"] = ""
        try:
           self.observations["next_sunset"] = to_date_time(self.observed_location.next_setting(ephem.Sun()))
        except Exception, e:
           self.observations["next_sunset"] = ""

    def civil_observations(self, extra_args={}):
        self.observed_location.horizon = civil_horizon()
        try:
            self.observations["civil_previous_rising"] = to_date_time(self.observed_location.previous_rising(ephem.Sun(), use_center=True))
        except Exception, e:
            self.observations["civil_previous_rising"] = ""
        try:
           self.observations["civil_next_rising"] = to_date_time(self.observed_location.next_rising(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["civil_next_rising"] = ""
        try:
           self.observations["civil_previous_setting"] = to_date_time(self.observed_location.previous_setting(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["civil_previous_setting"] = ""
        try:
           self.observations["civil_next_setting"] = to_date_time(self.observed_location.next_setting(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["civil_next_setting"] = ""

    def astronomical_observations(self, extra_args={}):
        self.observed_location.horizon = astronomical_horizon()
        try:
            self.observations["astronomical_previous_rising"] = to_date_time(self.observed_location.previous_rising(ephem.Sun(), use_center=True))
        except Exception, e:
            self.observations["astronomical_previous_rising"] = ""
        try:
           self.observations["astronomical_next_rising"] = to_date_time(self.observed_location.next_rising(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["astronomical_next_rising"] = ""
        try:
           self.observations["astronomical_previous_setting"] = to_date_time(self.observed_location.previous_setting(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["astronomical_previous_setting"] = ""
        try:
           self.observations["astronomical_next_setting"] = to_date_time(self.observed_location.next_setting(ephem.Sun(), use_center=True))
        except Exception, e:
           self.observations["astronomical_next_setting"] = ""

    def moon_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        moon = ephem.Moon()
        try:
            self.observations["previous_moonrise"] = to_date_time(self.observed_location.previous_rising(moon))
        except Exception, e:
            self.observations["previous_moonrise"] = ""
        try:
           self.observations["next_moonrise"] = to_date_time(self.observed_location.next_rising(moon))
        except Exception, e:
           self.observations["next_moonrise"] = ""
        try:
           self.observations["previous_moonset"] = to_date_time(self.observed_location.previous_setting(moon))
        except Exception, e:
           self.observations["previous_moonset"] = ""
        try:
           self.observations["next_moonset"] = to_date_time(self.observed_location.next_setting(moon))
        except Exception, e:
           self.observations["next_moonset"] = ""
        self.observations["previous_moon_transit"] = to_date_time(self.observed_location.previous_transit(moon))
        self.observations["next_moon_transit"] = to_date_time(self.observed_location.next_transit(moon))
        moon.compute(self.observed_location)
        self.observations["moon_altitude"] = str(moon.alt)
        self.observations["moon_azimuth"] = str(moon.az)
        self.observations["moon_phase"] = moon.moon_phase
        self.observations["moon_magnitude"] = moon.mag

    def venus_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        venus = ephem.Venus()
        try:
            self.observations["previous_venus_rise"] = to_date_time(self.observed_location.previous_rising(venus))
        except Exception, e:
            self.observations["previous_venus_rise"] = ""
        try:
            self.observations["next_venus_rise"] = to_date_time(self.observed_location.next_rising(venus))
        except Exception, e:
            self.observations["next_venus_rise"] = ""
        try:
            self.observations["previous_venus_set"] = to_date_time(self.observed_location.previous_setting(venus))
        except Exception, e:
            self.observations["previous_venus_set"] = ""
        try:
            self.observations["next_venus_set"] = to_date_time(self.observed_location.next_setting(venus))
        except Exception, e:
            self.observations["next_venus_set"] = ""
        self.observations["previous_venus_transit"] = to_date_time(self.observed_location.previous_transit(venus))
        self.observations["next_venus_transit"] = to_date_time(self.observed_location.next_transit(venus))
        venus.compute(self.observed_location)
        self.observations["venus_altitude"] = str(venus.alt)
        self.observations["venus_azimuth"] = str(venus.az)
        self.observations["venus_magnitude"] = venus.mag

    def jupiter_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        jupiter = ephem.Jupiter()
        try:
            self.observations["previous_jupiter_rise"] = to_date_time(self.observed_location.previous_rising(jupiter))
        except Exception, e:
            self.observations["previous_jupiter_rise"] = ""
        try:
            self.observations["next_jupiter_rise"] = to_date_time(self.observed_location.next_rising(jupiter))
        except Exception, e:
            self.observations["next_jupiter_rise"] = ""
        try:
            self.observations["previous_jupiter_set"] = to_date_time(self.observed_location.previous_setting(jupiter))
        except Exception, e:
            self.observations["previous_jupiter_set"] = ""
        try:
            self.observations["next_jupiter_set"] = to_date_time(self.observed_location.next_setting(jupiter))
        except Exception, e:
            self.observations["next_jupiter_set"] = ""
        self.observations["previous_jupiter_transit"] = to_date_time(self.observed_location.previous_transit(jupiter))
        self.observations["next_jupiter_transit"] = to_date_time(self.observed_location.next_transit(jupiter))
        jupiter.compute(self.observed_location)
        self.observations["jupiter_altitude"] = str(jupiter.alt)
        self.observations["jupiter_azimuth"] = str(jupiter.az)
        self.observations["jupiter_magnitude"] = jupiter.mag

    def mars_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        mars = ephem.Mars()
        try:
            self.observations["previous_mars_rise"] = to_date_time(self.observed_location.previous_rising(mars))
        except Exception, e:
            self.observations["previous_mars_rise"] = ""
        try:
            self.observations["next_mars_rise"] = to_date_time(self.observed_location.next_rising(mars))
        except Exception, e:
            self.observations["next_mars_rise"] = ""
        try:
            self.observations["previous_mars_set"] = to_date_time(self.observed_location.previous_setting(mars))
        except Exception, e:
            self.observations["previous_mars_set"] = ""
        try:
            self.observations["next_mars_set"] = to_date_time(self.observed_location.next_setting(mars))
        except Exception, e:
            self.observations["next_mars_set"] = ""
        self.observations["previous_mars_transit"] = to_date_time(self.observed_location.previous_transit(mars))
        self.observations["next_mars_transit"] = to_date_time(self.observed_location.next_transit(mars))
        mars.compute(self.observed_location)
        self.observations["mars_altitude"] = str(mars.alt)
        self.observations["mars_azimuth"] = str(mars.az)
        self.observations["mars_magnitude"] = mars.mag

    def saturn_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        saturn = ephem.Saturn()
        try:
            self.observations["previous_saturn_rise"] = to_date_time(self.observed_location.previous_rising(saturn))
        except Exception, e:
            self.observations["previous_saturn_rise"] = ""
        try:
            self.observations["next_saturn_rise"] = to_date_time(self.observed_location.next_rising(saturn))
        except Exception, e:
            self.observations["next_saturn_rise"] = ""
        try:
            self.observations["previous_saturn_set"] = to_date_time(self.observed_location.previous_setting(saturn))
        except Exception, e:
            self.observations["previous_saturn_set"] = ""
        try:
            self.observations["next_saturn_set"] = to_date_time(self.observed_location.next_setting(saturn))
        except Exception, e:
            self.observations["next_saturn_set"] = ""
        self.observations["previous_saturn_transit"] = to_date_time(self.observed_location.previous_transit(saturn))
        self.observations["next_saturn_transit"] = to_date_time(self.observed_location.next_transit(saturn))
        saturn.compute(self.observed_location)
        self.observations["saturn_altitude"] = str(saturn.alt)
        self.observations["saturn_azimuth"] = str(saturn.az)
        self.observations["saturn_magnitude"] = saturn.mag

    def mercury_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        mercury = ephem.Mercury()
        try:
            self.observations["previous_mercury_rise"] = to_date_time(self.observed_location.previous_rising(mercury))
        except Exception, e:
            self.observations["previous_mercury_rise"] = ""
        try:
            self.observations["next_mercury_rise"] = to_date_time(self.observed_location.next_rising(mercury))
        except Exception, e:
            self.observations["next_mercury_rise"] = ""
        try:
           self.observations["previous_mercury_set"] = to_date_time(self.observed_location.previous_setting(mercury))
        except Exception, e:
           self.observations["previous_mercury_set"] = ""
        try:
           self.observations["next_mercury_set"] = to_date_time(self.observed_location.next_setting(mercury))
        except Exception, e:
           self.observations["next_mercury_set"] = ""
        self.observations["previous_mercury_transit"] = to_date_time(self.observed_location.previous_transit(mercury))
        self.observations["next_mercury_transit"] = to_date_time(self.observed_location.next_transit(mercury))
        mercury.compute(self.observed_location)
        self.observations["mercury_altitude"] = str(mercury.alt)
        self.observations["mercury_azimuth"] = str(mercury.az)
        self.observations["mercury_magnitude"] = mercury.mag

    def sirius_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        sirius = ephem.star('Sirius')
        try:
            self.observations["previous_sirius_rise"] = to_date_time(self.observed_location.previous_rising(sirius))
        except Exception, e:
            self.observations["previous_sirius_rise"] = ""
        try:
           self.observations["next_sirius_rise"] = to_date_time(self.observed_location.next_rising(sirius))
        except Exception, e:
           self.observations["next_sirius_rise"] = ""
        try:
           self.observations["previous_sirius_set"] = to_date_time(self.observed_location.previous_setting(sirius))
        except Exception, e:
           self.observations["previous_sirius_set"] = ""
        try:
           self.observations["next_sirius_set"] = to_date_time(self.observed_location.next_setting(sirius))
        except Exception, e:
           self.observations["next_sirius_set"] = ""
        self.observations["previous_sirius_transit"] = to_date_time(self.observed_location.previous_transit(sirius))
        self.observations["next_sirius_transit"] = to_date_time(self.observed_location.next_transit(sirius))
        sirius.compute(self.observed_location)
        self.observations["sirius_altitude"] = str(sirius.alt)
        self.observations["sirius_azimuth"] = str(sirius.az)
        self.observations["sirius_magnitude"] = sirius.mag

    def arcturus_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        arcturus = ephem.star('Arcturus')
        try:
            self.observations["previous_arcturus_rise"] = to_date_time(self.observed_location.previous_rising(arcturus))
        except Exception, e:
            self.observations["previous_arcturus_rise"] = ""
        try:
           self.observations["next_arcturus_rise"] = to_date_time(self.observed_location.next_rising(arcturus))
        except Exception, e:
           self.observations["next_arcturus_rise"] = ""
        try:
           self.observations["previous_arcturus_set"] = to_date_time(self.observed_location.previous_setting(arcturus))
        except Exception, e:
           self.observations["previous_arcturus_set"] = ""
        try:
           self.observations["next_arcturus_set"] = to_date_time(self.observed_location.next_setting(arcturus))
        except Exception, e:
           self.observations["next_arcturus_set"] = ""
        self.observations["previous_arcturus_transit"] = to_date_time(self.observed_location.previous_transit(arcturus))
        self.observations["next_arcturus_transit"] = to_date_time(self.observed_location.next_transit(arcturus))
        arcturus.compute(self.observed_location)
        self.observations["arcturus_altitude"] = str(arcturus.alt)
        self.observations["arcturus_azimuth"] = str(arcturus.az)
        self.observations["arcturus_magnitude"] = arcturus.mag

    def vega_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        vega = ephem.star('Vega')
        try:
            self.observations["previous_vega_rise"] = to_date_time(self.observed_location.previous_rising(vega))
        except Exception, e:
            self.observations["previous_vega_rise"] = ""
        try:
           self.observations["next_vega_rise"] = to_date_time(self.observed_location.next_rising(vega))
        except Exception, e:
           self.observations["next_vega_rise"] = ""
        try:
           self.observations["previous_vega_set"] = to_date_time(self.observed_location.previous_setting(vega))
        except Exception, e:
           self.observations["previous_vega_set"] = ""
        try:
           self.observations["next_vega_set"] = to_date_time(self.observed_location.next_setting(vega))
        except Exception, e:
           self.observations["next_vega_set"] = ""
        self.observations["previous_vega_transit"] = to_date_time(self.observed_location.previous_transit(vega))
        self.observations["next_vega_transit"] = to_date_time(self.observed_location.next_transit(vega))
        vega.compute(self.observed_location)
        self.observations["vega_altitude"] = str(vega.alt)
        self.observations["vega_azimuth"] = str(vega.az)
        self.observations["vega_magnitude"] = vega.mag

    def capella_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        capella = ephem.star('Capella')
        try:
            self.observations["previous_capella_rise"] = to_date_time(self.observed_location.previous_rising(capella))
        except Exception, e:
            self.observations["previous_capella_rise"] = ""
        try:
            self.observations["next_capella_rise"] = to_date_time(self.observed_location.next_rising(capella))
        except Exception, e:
            self.observations["next_capella_rise"] = ""
        try:
            self.observations["previous_capella_set"] = to_date_time(self.observed_location.previous_setting(capella))
        except Exception, e:
            self.observations["previous_capella_set"] = ""
        try:
            self.observations["next_capella_set"] = to_date_time(self.observed_location.next_setting(capella))
        except Exception, e:
            self.observations["next_capella_set"] = ""
        self.observations["previous_capella_transit"] = to_date_time(self.observed_location.previous_transit(capella))
        self.observations["next_capella_transit"] = to_date_time(self.observed_location.next_transit(capella))
        capella.compute(self.observed_location)
        self.observations["capella_altitude"] = str(capella.alt)
        self.observations["capella_azimuth"] = str(capella.az)
        self.observations["capella_magnitude"] = capella.mag

    def rigel_observations(self, extra_args={}):
        self.observed_location.horizon = standard_horizon()
        rigel = ephem.star('Rigel')
        try:
            self.observations["previous_rigel_rise"] = to_date_time(self.observed_location.previous_rising(rigel))
        except Exception, e:
            self.observations["previous_rigel_rise"] = ""
        try:
            self.observations["next_rigel_rise"] = to_date_time(self.observed_location.next_rising(rigel))
        except Exception, e:
            self.observations["next_rigel_rise"] = ""
        try:
            self.observations["previous_rigel_set"] = to_date_time(self.observed_location.previous_setting(rigel))
        except Exception, e:
            self.observations["previous_rigel_set"] = ""
        try:
            self.observations["next_rigel_set"] = to_date_time(self.observed_location.next_setting(rigel))
        except Exception, e:
            self.observations["next_rigel_set"] = ""
        self.observations["previous_rigel_transit"] = to_date_time(self.observed_location.previous_transit(rigel))
        self.observations["next_rigel_transit"] = to_date_time(self.observed_location.next_transit(rigel))
        rigel.compute(self.observed_location)
        self.observations["rigel_altitude"] = str(rigel.alt)
        self.observations["rigel_azimuth"] = str(rigel.az)
        self.observations["rigel_magnitude"] = rigel.mag

