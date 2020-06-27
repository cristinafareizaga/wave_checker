import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_best_moments(days_hours, best_moments_surfing_yes_no):
    plt.ylabel("No surfing = 0/Surfing = 1")
    plt.xlabel("Days and hours")
    plt.title("Best moments for surfing")
    plt.xticks(rotation=90)
    plt.tick_params(labelsize=4)
    sns.barplot(x=np.array(days_hours), y=np.array(best_moments_surfing_yes_no), color="blue")
    plt.ylim(0, 1.5)
    plt.show()