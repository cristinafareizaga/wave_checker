import wave_checker.analysis.reader as rea
import wave_checker.analysis.best_moments as be
import wave_checker.data_vis.plot_best_moments as pl

def analysis_csv(csv, orientation):
    # Read csv
    days_hours, wind_speed, wind_gust, wind_direction, wave_level = rea.read_csv(csv)

    best_moments_surfing, best_moments_surfing_yes_no = be.get_best_moments(
        days_hours, wind_speed, wind_gust, wind_direction, wave_level,orientation)

    pl.plot_best_moments(days_hours,best_moments_surfing_yes_no)
    print(best_moments_surfing)
    print(best_moments_surfing_yes_no)

# Data visualization
# Mareas