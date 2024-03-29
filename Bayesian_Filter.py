# Advanced Robotic Programming - Assignment 2
# Efosa Ogiesoba
# Bayesian Filter

# Import importaant libraries
import random
import matplotlib.pyplot as plt
import numpy as np

# Declare global variables
state_space = ["p0", "p1", "p2", "p3"]
state_space_range = len(state_space)
num_of_time_steps = 4
random_sensor = False
time_step_arr = []
belief_dictionary = {
    "bel_p0": [],
    "bel_p1": [],
    "bel_p2": [],
    "bel_p3": [],
}

# Define control probability function
def prob_control(state_previous, state_current):
    if state_current - state_previous == 0:\
        # 20% of the time it will slip and stay in the same grid.
        return 0.20
    elif state_current - state_previous == 1:
        # 70% of the time it moves correctly to the next grid (e.g. P1 from P0)
        return 0.70
    elif state_current - state_previous == 2:
        # 10% of the time it will move two grids over (P2 from P0).
        return 0.10
    else:
        # 0% chance the robot can move to the yellow grid located after P3, or backwards.
        return 0

# Define measurement probability function
def prob_measurement(state_unique, state_sensor):
    sensor_measurement = ["wall", "door", "wall", "door"]
    if random_sensor:
        random_sensor_index = random.randint(0, len(sensor_measurement) - 1)
        if sensor_measurement[state_unique] == "wall":
            if sensor_measurement[random_sensor_index] == "wall":
                return 0.75  # 75% of the time it will detect the wall.
            else:
                # 25% of the time it will detect incorrectly and see a door.
                return 0.25
        if sensor_measurement[state_unique] == "door":
            if sensor_measurement[random_sensor_index] == "door":
                # 30% of the time it will detect incorrectly and see a wall.
                return 0.70
            else:
                # 70% of the time it will detect correctly and detect a door.
                return 0.30
    else:
        if sensor_measurement[state_unique] == "wall":
            if sensor_measurement[state_sensor] == "wall":
                return 0.75  # 75% of the time it will detect the wall.
            else:
                # 25% of the time it will detect incorrectly and see a door.
                return 0.25
        if sensor_measurement[state_unique] == "door":
            if sensor_measurement[state_sensor] == "door":
                # 30% of the time it will detect incorrectly and see a wall.
                return 0.70
            else:
                # 70% of the time it will detect correctly and detect a door.
                return 0.30

# Define the bayesian filter function
def run_bayesian_filter():
    for time in range(num_of_time_steps):
        # Initialize bel_bar
        bel_bar = []

        if time == 0:
            # Current belief at time = 0
            bel_p0 = 0.25
            bel_p1 = 0.25
            bel_p2 = 0.25
            bel_p3 = 0.25

            # Add beliefs to belief_dictionary
            belief_dictionary["bel_p0"].append(bel_p0)
            belief_dictionary["bel_p1"].append(bel_p1)
            belief_dictionary["bel_p2"].append(bel_p2)
            belief_dictionary["bel_p3"].append(bel_p3)

            # Add new time step name to time_step_arr
            time_step_arr.append("time = " + str(time))

            # Dispilay bel_bar at current time stap
            print("bel_bar: ", bel_bar)

            # Dispilay bel at current time stap
            print("bel: [", bel_p0, ",", bel_p1, ",", bel_p2, ",", bel_p3, "]")
        else:
            # Calculate bel_bar
            for state_control in range(state_space_range):
                # Limit the value of state_control to a maximum of 3
                if state_control > 3:
                    state_control = 3

                # Calcualte each probability section in bel_bar
                prob_a = prob_control(0, state_control) * bel_p0
                prob_b = prob_control(1, state_control) * bel_p1
                prob_c = prob_control(2, state_control) * bel_p2
                prob_d = prob_control(3, state_control) * bel_p3

                # Calculate bel_bar_sum
                bel_bar_sum = prob_a + prob_b + prob_c + prob_d

                # Round bel_bar_sum to the nearest 3rd decimal place
                bel_bar_sum = round(bel_bar_sum, 3)

                # Add bel_bar_sum to the bel_bar array
                bel_bar.append(bel_bar_sum)

            # Dispilay bel_bar at current time stap
            print("bel_bar: ", bel_bar)

            # Let the value of time represent the state and limit the last state to 3
            state_sensor = time
            if state_sensor > 3:
                state_sensor = 3

            # Calculate bel_without_eta
            bel_without_eta_p0 = prob_measurement(0, state_sensor) * bel_bar[0]
            bel_without_eta_p1 = prob_measurement(1, state_sensor) * bel_bar[1]
            bel_without_eta_p2 = prob_measurement(2, state_sensor) * bel_bar[2]
            bel_without_eta_p3 = prob_measurement(3, state_sensor) * bel_bar[3]

            # Calculate eta
            eta = 1 / (bel_without_eta_p0 + bel_without_eta_p1 +
                       bel_without_eta_p2 + bel_without_eta_p3)

            # Calculate new beliefs at new time step
            bel_p0 = bel_without_eta_p0 * eta
            bel_p1 = bel_without_eta_p1 * eta
            bel_p2 = bel_without_eta_p2 * eta
            bel_p3 = bel_without_eta_p3 * eta

            # Round beliefs to the nearest 3rd decimal place
            bel_p0 = round(bel_p0, 3)
            bel_p1 = round(bel_p1, 3)
            bel_p2 = round(bel_p2, 3)
            bel_p3 = round(bel_p3, 3)

            # Dispilay bel at current time stap
            print("bel: [", bel_p0, ",", bel_p1, ",", bel_p2, ",", bel_p3, "]")

            # Add beliefs to belief_dictionary
            belief_dictionary["bel_p0"].append(bel_p0)
            belief_dictionary["bel_p1"].append(bel_p1)
            belief_dictionary["bel_p2"].append(bel_p2)
            belief_dictionary["bel_p3"].append(bel_p3)

            # Add new time step name to time_step_arr
            time_step_arr.append("time = " + str(time))

# Define the bayesian Filter Plot function
def plot_bayesian_filter_beliefs():
    x = np.arange(len(time_step_arr))  # The label locations
    width = 0.20  # The width of the belief bars
    multiplier = 0

    # Define figure
    fig, ax = plt.subplots(layout='constrained')

    # Create belief bars in the plot
    for state, beliefs in belief_dictionary.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, beliefs, width, label=state)
        ax.bar_label(rects, padding=3, label_type='edge', fontsize=8)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Probability')
    ax.set_title('Bayesian Filter Calculated Beliefs')
    xtick_space = x + width * (multiplier - 1) / 2
    ax.set_xticks(xtick_space, time_step_arr)
    ax.legend(loc='upper left', ncols=4)
    ax.set_ylim(0, 1)

    # Show plot
    plt.show()

# Run the bayesian filter algorithm
run_bayesian_filter()

# Plot Bayesian filter beliefs at each state at each time step
plot_bayesian_filter_beliefs()
