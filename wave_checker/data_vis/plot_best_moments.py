import matplotlib.pyplot as plt

def plot_best_moments(days_hours, best_moments_surfing_yes_no):
    plt.bar(days_hours, best_moments_surfing_yes_no)
    plt.savefig("best_moments_surfing.png")