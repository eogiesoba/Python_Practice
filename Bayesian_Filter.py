#Advanced Robotic Programming - Assignment 2
#Bayesian Filter

# Import importaant libraries
import random
import matplotlib.pyplot as plt
import numpy as np

#Declare global variables
state_space = ["p0", "p1", "p2","p3"]
state_space_range = len(state_space)
random_sensor = False
time_step_arr = []
belief_dictionary = {
    "bel_p0" : [],
    "bel_p1" : [],
    "bel_p2" : [],
    "bel_p3" : [],
}

#Define control probability function
def prob_control(state_previous, state_current):
    if state_current - state_previous == 0:
        return 0.20
    elif state_current - state_previous == 1:
        return 0.70
    elif state_current - state_previous == 2:
        return 0.10
    else:
        return 0

#Define measurement probability function
def prob_measurement(state_unique, state_sensor):
    sensor_measurement = ["wall","door","wall","door"]
    if random_sensor: 
        random_sensor_index = random.randint(0, len(sensor_measurement) - 1)
        if sensor_measurement[state_unique] == "wall":
            if sensor_measurement[random_sensor_index] == "wall":
                return 0.75
            else:
                return 0.25
        if sensor_measurement[state_unique] == "door":
            if sensor_measurement[random_sensor_index] == "door":
                return 0.70
            else:
                return 0.30
    else:
        if sensor_measurement[state_unique] == "wall":
            if sensor_measurement[state_sensor] == "wall":
                return 0.75
            else:
                return 0.25
        if sensor_measurement[state_unique] == "door":
            if sensor_measurement[state_sensor] == "door":
                return 0.70
            else:
                return 0.30

#Define the bayesian filter function
def run_bayesian_filter():
    for time in range(state_space_range):
        #Initialize bel_bar
        bel_bar = []

        if time == 0:
            #Current belief at time = 0
            bel_p0 = 0.25
            bel_p1 = 0.25
            bel_p2 = 0.25
            bel_p3 = 0.25

            #Add beliefs to belief_dictionary
            belief_dictionary["bel_p0"].append(bel_p0)
            belief_dictionary["bel_p1"].append(bel_p1)
            belief_dictionary["bel_p2"].append(bel_p2)
            belief_dictionary["bel_p3"].append(bel_p3)

            #Add new time step name to time_step_arr
            time_step_arr.append("time = " + str(time))
            
            print("bel_bar: ", bel_bar)
            print("bel: ", bel_p0, bel_p1, bel_p2, bel_p3)
        else:            
            #Current belief at time t > 0 
            for state_control in range(state_space_range):
                print(state_control)
                prob_a = prob_control(0, state_control) * bel_p0 
                prob_b = prob_control(1, state_control) * bel_p1
                prob_c = prob_control(2, state_control) * bel_p2 
                prob_d = prob_control(3, state_control) * bel_p3
                bel_bar_sum = prob_a + prob_b + prob_c + prob_d
                bel_bar.append(bel_bar_sum)
            print("bel_bar: " , bel_bar)
            # Let the value of time represent the state
            state_sensor = time 

            #Calculate bel_without_eta
            bel_without_eta_p0 = prob_measurement(0, state_sensor) * bel_bar[0]
            bel_without_eta_p1 = prob_measurement(1, state_sensor) * bel_bar[1]
            bel_without_eta_p2 = prob_measurement(2, state_sensor) * bel_bar[2]
            bel_without_eta_p3 = prob_measurement(3, state_sensor) * bel_bar[3]
            print("bel_without_eta: " , bel_without_eta_p0, bel_without_eta_p1, bel_without_eta_p2, bel_without_eta_p3)
            #Calculate eta
            eta = 1 / (bel_without_eta_p0 + bel_without_eta_p1 + bel_without_eta_p2 + bel_without_eta_p3)
            print("eta: " , eta)
            #Calculate new beliefs at new time step
            bel_p0 = bel_without_eta_p0 * eta
            bel_p1 = bel_without_eta_p1 * eta
            bel_p2 = bel_without_eta_p2 * eta
            bel_p3 = bel_without_eta_p3 * eta
            print("bel: ", bel_p0, bel_p1, bel_p2, bel_p3)

            #Add beliefs to belief_dictionary
            belief_dictionary["bel_p0"].append(bel_p0)
            belief_dictionary["bel_p1"].append(bel_p1)
            belief_dictionary["bel_p2"].append(bel_p2)
            belief_dictionary["bel_p3"].append(bel_p3)

            #Add new time step name to time_step_arr
            time_step_arr.append("time = " + str(time))

    print(belief_dictionary)
    print(time_step_arr)

# Define the bayesian Filter Plot function
def plot_bayesian_filter_beliefs():
    x = np.arange(len(belief_dictionary))  # the label locations
    width = 0.20  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for time_step, belief in belief_dictionary.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, belief, width, label=time_step)
        ax.bar_label(rects, padding=3, label_type='edge', fontsize=8)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Probability')
    ax.set_title('Bayesian Filter Calculated Beliefs')
    ax.set_xticks(x + width, time_step_arr)
    ax.legend(loc='upper left', ncols=4)
    ax.set_ylim(0, 1)

    plt.show()

#Run the bayesian filter algorithm
run_bayesian_filter()  

#Plot Bayesian filter beliefs at each state at each time step
plot_bayesian_filter_beliefs()