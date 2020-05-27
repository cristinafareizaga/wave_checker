import re

def get_best_moments (days_hours, wind_speed, wind_gust, wind_direction, wave_level, orientation):
    WINDS = {"N": [135, 225],
             "NE": [180, 270],
             "E": [225, 315],
             "SE": [270, 360],
             "S": [315, 45],
             "SW": [360, 90],
             "W": [45, 135],
             "NW": [90, 180]}

    best_moments_surfing = []
    best_moments_surfing_yes_no = []
    for day_hour,speed,gust,direction,level in zip(days_hours,wind_speed,wind_gust,wind_direction,wave_level):
        # Preprocess wind direction to get degrees
        pattern = re.compile(r"\((\d+)\)")
        degrees = float(pattern.findall(direction)[0])
        minimum, maximum = WINDS[orientation]
        #wind_direction in WINDS[orientation]
        if  speed < 20 and gust < 20  and  maximum+10 > degrees > minimum-10 and level >= 0.6:
            best_moments_surfing.append(day_hour)
            best_moments_surfing_yes_no.append(1)
        else:
            best_moments_surfing_yes_no.append(0)
    return best_moments_surfing, best_moments_surfing_yes_no