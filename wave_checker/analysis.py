import pandas as pd
import matplotlib.pyplot as plt

def analysis_csv(csv):
    df = pd.read_csv(csv)
    days_hours = df.loc[0]
    wind_speed = df.loc[1].astype(int)
    wind_gust = df.loc[2].astype(int)
    wind_direction = df.loc[3]
    wave_level = df.loc[4].astype(float)
    best_moments_surfing = []
    best_moments_surfing_yes_no = []
    for day_hour,speed,gust,direction,level in zip(days_hours,wind_speed,wind_gust,wind_direction,wave_level):
        if  speed < 20 and gust < 20 and "N " not in direction and level >= 0.6:
            best_moments_surfing.append(day_hour)
            best_moments_surfing_yes_no.append(1)
        else:
            best_moments_surfing_yes_no.append(0)
    plt.bar(days_hours, best_moments_surfing_yes_no)
    plt.show()
    print(best_moments_surfing)
    print(best_moments_surfing_yes_no)

# Score de las opciones que son buenas
# Comparar condiciones entre playas 