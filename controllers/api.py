import ephem
import dateutil.parser
from datetime import date, datetime

exec('from applications.%s.modules.astro import Astro' % request.application)

def index():
    redirect('/')


def lookup():
    # astronomy api
    if request.vars['lat'] and request.vars['lng'] and request.vars['dateTime']:
        try:
            astro = Astro(request.vars['lat'], request.vars['lng'], request.vars['dateTime'])
            astro.observe()
        except Exception, e:
            result_message = 'error: %s' % e
            return dict(message=result_message)
        else:
            result_message = 'ok'
            return dict(message=result_message, 
                previous_sunrise=astro.observations["previous_sunrise"],
                next_sunrise=astro.observations["next_sunrise"],
                previous_sunset=astro.observations["previous_sunset"],
                next_sunset=astro.observations["next_sunset"],

                civil_previous_rising=astro.observations["civil_previous_rising"],
                civil_next_rising=astro.observations["civil_next_rising"],
                civil_previous_setting=astro.observations["civil_previous_setting"],
                civil_next_setting=astro.observations["civil_next_setting"],

                astronomical_previous_rising=astro.observations["astronomical_previous_rising"],
                astronomical_next_rising=astro.observations["astronomical_next_rising"],
                astronomical_previous_setting=astro.observations["astronomical_previous_setting"],
                astronomical_next_setting=astro.observations["astronomical_next_setting"],

                previous_moonrise=astro.observations["previous_moonrise"],
                next_moonrise=astro.observations["next_moonrise"],
                previous_moonset=astro.observations["previous_moonset"],
                next_moonset=astro.observations["next_moonset"],
                previous_moon_transit=astro.observations["previous_moon_transit"],
                next_moon_transit=astro.observations["next_moon_transit"],
                moon_altitude=astro.observations["moon_altitude"],
                moon_azimuth=astro.observations["moon_azimuth"],
                moon_phase=astro.observations["moon_phase"],
                moon_magnitude=astro.observations["moon_magnitude"],

                previous_venusrise=astro.observations["previous_venusrise"],
                next_venusrise=astro.observations["next_venusrise"],
                previous_venusset=astro.observations["previous_venusset"],
                next_venusset=astro.observations["next_venusset"],
                previous_venus_transit=astro.observations["previous_venus_transit"],
                next_venus_transit=astro.observations["next_venus_transit"],
                venus_altitude=astro.observations["venus_altitude"],
                venus_azimuth=astro.observations["venus_azimuth"],
                venus_magnitude=astro.observations["venus_magnitude"],

                previous_jupiterrise=astro.observations["previous_jupiterrise"],
                next_jupiterrise=astro.observations["next_jupiterrise"],
                previous_jupiterset=astro.observations["previous_jupiterset"],
                next_jupiterset=astro.observations["next_jupiterset"],
                previous_jupiter_transit=astro.observations["previous_jupiter_transit"],
                next_jupiter_transit=astro.observations["next_jupiter_transit"],
                jupiter_altitude=astro.observations["jupiter_altitude"],
                jupiter_azimuth=astro.observations["jupiter_azimuth"],
                jupiter_magnitude=astro.observations["jupiter_magnitude"],

                previous_marsrise=astro.observations["previous_marsrise"],
                next_marsrise=astro.observations["next_marsrise"],
                previous_marsset=astro.observations["previous_marsset"],
                next_marsset=astro.observations["next_marsset"],
                previous_mars_transit=astro.observations["previous_mars_transit"],
                next_mars_transit=astro.observations["next_mars_transit"],
                mars_altitude=astro.observations["mars_altitude"],
                mars_azimuth=astro.observations["mars_azimuth"],
                mars_magnitude=astro.observations["mars_magnitude"],

                previous_saturnrise=astro.observations["previous_saturnrise"],
                next_saturnrise=astro.observations["next_saturnrise"],
                previous_saturnset=astro.observations["previous_saturnset"],
                next_saturnset=astro.observations["next_saturnset"],
                previous_saturn_transit=astro.observations["previous_saturn_transit"],
                next_saturn_transit=astro.observations["next_saturn_transit"],
                saturn_altitude=astro.observations["saturn_altitude"],
                saturn_azimuth=astro.observations["saturn_azimuth"],
                saturn_magnitude=astro.observations["saturn_magnitude"],

                previous_mercuryrise=astro.observations["previous_mercuryrise"],
                next_mercuryrise=astro.observations["next_mercuryrise"],
                previous_mercuryset=astro.observations["previous_mercuryset"],
                next_mercuryset=astro.observations["next_mercuryset"],
                previous_mercury_transit=astro.observations["previous_mercury_transit"],
                next_mercury_transit=astro.observations["next_mercury_transit"],
                mercury_altitude=astro.observations["mercury_altitude"],
                mercury_azimuth=astro.observations["mercury_azimuth"],
                mercury_magnitude=astro.observations["mercury_magnitude"],

                previous_siriusrise=astro.observations["previous_siriusrise"],
                next_siriusrise=astro.observations["next_siriusrise"],
                previous_siriusset=astro.observations["previous_siriusset"],
                next_siriusset=astro.observations["next_siriusset"],
                previous_sirius_transit=astro.observations["previous_sirius_transit"],
                next_sirius_transit=astro.observations["next_sirius_transit"],
                sirius_altitude=astro.observations["sirius_altitude"],
                sirius_azimuth=astro.observations["sirius_azimuth"],
                sirius_magnitude=astro.observations["sirius_magnitude"],

                previous_arcturusrise=astro.observations["previous_arcturusrise"],
                next_arcturusrise=astro.observations["next_arcturusrise"],
                previous_arcturusset=astro.observations["previous_arcturusset"],
                next_arcturusset=astro.observations["next_arcturusset"],
                previous_arcturus_transit=astro.observations["previous_arcturus_transit"],
                next_arcturus_transit=astro.observations["next_arcturus_transit"],
                arcturus_altitude=astro.observations["arcturus_altitude"],
                arcturus_azimuth=astro.observations["arcturus_azimuth"],
                arcturus_magnitude=astro.observations["arcturus_magnitude"],

                previous_vegarise=astro.observations["previous_vegarise"],
                next_vegarise=astro.observations["next_vegarise"],
                previous_vegaset=astro.observations["previous_vegaset"],
                next_vegaset=astro.observations["next_vegaset"],
                previous_vega_transit=astro.observations["previous_vega_transit"],
                next_vega_transit=astro.observations["next_vega_transit"],
                vega_altitude=astro.observations["vega_altitude"],
                vega_azimuth=astro.observations["vega_azimuth"],
                vega_magnitude=astro.observations["vega_magnitude"],

                previous_capellarise=astro.observations["previous_capellarise"],
                next_capellarise=astro.observations["next_capellarise"],
                previous_capellaset=astro.observations["previous_capellaset"],
                next_capellaset=astro.observations["next_capellaset"],
                previous_capella_transit=astro.observations["previous_capella_transit"],
                next_capella_transit=astro.observations["next_capella_transit"],
                capella_altitude=astro.observations["capella_altitude"],
                capella_azimuth=astro.observations["capella_azimuth"],
                capella_magnitude=astro.observations["capella_magnitude"],

                previous_rigelrise=astro.observations["previous_rigelrise"],
                next_rigelrise=astro.observations["next_rigelrise"],
                previous_rigelset=astro.observations["previous_rigelset"],
                next_rigelset=astro.observations["next_rigelset"],
                previous_rigel_transit=astro.observations["previous_rigel_transit"],
                next_rigel_transit=astro.observations["next_rigel_transit"],
                rigel_altitude=astro.observations["rigel_altitude"],
                rigel_azimuth=astro.observations["rigel_azimuth"],
                rigel_magnitude=astro.observations["rigel_magnitude"]
                )
    else:
        return dict(message="error - missing required parameters.")


