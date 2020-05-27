import pandas as pd


def read_csv(csv):
    df = pd.read_csv(csv)
    days_hours = df.loc[0]
    wind_speed = df.loc[1].astype(int)
    wind_gust = df.loc[2].astype(int)
    wind_direction = df.loc[3]
    wave_level = df.loc[4].astype(float)
    return days_hours, wind_speed, wind_gust, wind_direction, wave_level