#Advanced Robotic Programming - Assignment 2
#Bayesian Filter

#Declare global variables
state_space = ["p0", "p1", "p2","p3"]
num_time_steps = 4 #Each time step is 1 sec
user = "jane"

def greet(name):
    for i in range(num_time_steps):
        print(str(i) + " " + name)

        for i in range(num_time_steps):
            bel_bar_p0 = 34
            bel_bar_p1 = 34
            bel_bar_p2 = 34
            bel_bar_p3 = 34

            bel_without_eta_p0 = 334
            bel_without_eta_p1 = 334
            bel_without_eta_p2 = 334
            bel_without_eta_p3 = 334

        eta = 1 / (bel_without_eta_p0 + bel_without_eta_p1 + bel_without_eta_p2 + bel_without_eta_p3)
        bel_p0 = bel_without_eta_p0 * eta
        bel_p1 = bel_without_eta_p1 * eta
        bel_p2 = bel_without_eta_p2 * eta
        bel_p3 = bel_without_eta_p3 * eta

greet(user)


# Plot the Bayesian Filter Robot Location Probabilities
# import matplotlib.pyplot as plt
# import numpy as np

# species = ("Adelie", "Chinstrap", "Gentoo")
# penguin_means = {
#     'Bill Depth': (18.35, 18.43, 14.98),
#     'Bill Length': (38.79, 48.83, 47.50),
#     'Flipper Length': (189.95, 195.82, 217.19),
# }

# x = np.arange(len(species))  # the label locations
# width = 0.25  # the width of the bars
# multiplier = 0

# fig, ax = plt.subplots(layout='constrained')

# for attribute, measurement in penguin_means.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     ax.bar_label(rects, padding=3)
#     multiplier += 1

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Length (mm)')
# ax.set_title('Penguin attributes by species')
# ax.set_xticks(x + width, species)
# ax.legend(loc='upper left', ncols=3)
# ax.set_ylim(0, 250)

# plt.show()