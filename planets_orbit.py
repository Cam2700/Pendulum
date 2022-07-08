import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import math

def next_state(state, h):
    print(state)
    k1 = diff_value(state)
    k2 = diff_value(state + (k1*(h/2)))
    k3 = diff_value(state + (k2*(h/2)))
    k4 = diff_value(state + (k3*h))

    delta = (k1 + k2*2 + k3*2 + k4)*(h/6)

    state = state + delta

    return state

def diff_value(state):
    temp = np.zeros((3, 7))

    # pos_x, pos_y = state[0], state[1]
    # ax, ay = state[2], state[3]
    # vx, vy = state[4], state[5]

    for i in range(3):
        for j in range(3):
            if i == j:
                continue
        
            dis_x = state[j, 0] - state[i, 0]
            dis_y = state[j, 1] - state[i, 1]

            dis_uc = math.sqrt(dis_x**2 + dis_y**2)

            temp[i, 2] += ((state[j, 6]*dis_x)/dis_uc**3)
            temp[i, 3] += ((state[j, 6]*dis_y)/dis_uc**3)

        temp[i, 4] = temp[i, 2]
        temp[i, 5] = temp[i, 3]

        temp[i, 0] = state[i, 4]
        temp[i, 1] = state[i, 5]

    return temp

def update(num, dot1, dot2, dot3, trail4, trail5, trail6, x, y):
    val = max(0, num - 175)
    ax.set_title(num)

    dot1.set_data(x[num, 0], y[num, 0])
    dot2.set_data(x[num, 1], y[num, 1])
    dot3.set_data(x[num, 2], y[num, 2])

    trail4.set_data(x[val:num, 0], y[val:num, 0])
    trail5.set_data(x[val:num, 1], y[val:num, 1])
    trail6.set_data(x[val:num, 2], y[val:num, 2])

size = 1000
skip = 10

x_matrix = np.zeros(shape = (size, 3))
y_matrix = np.zeros(shape = (size, 3))
print(x_matrix)

pos_x = [0.97000436, -0.97000436, 0]
pos_y = [-0.24308753, 0.24308753, 0]
ax = [0, 0, 0]
ay = [0, 0, 0]
vx = [0.93240737/2, 0.93240737/2, -0.93240737]
vy = [0.86473146/2, 0.86473146/2, -0.86473146]
mass = [1, 1, 1]

vector = np.zeros((3, 7))

for i in range(3):
    vector[i ,:] = pos_x[i], pos_y[i], ax[i], ay[i], vx[i], vy[i], mass[i]

for i in range(size*skip):
    for j in range(3):
        if i%skip == 0:
            x_matrix[i//skip, j] = vector[j, 0]
            y_matrix[i//skip, j] = vector[j, 1]

    vector = next_state(vector, 0.001)

fig = plt.figure()
ax = fig.add_subplot()

x = x_matrix
y = y_matrix

dot1, = ax.plot(x[:, 0], y[:, 0], 'o', color = "#2ca02c")
dot2, = ax.plot(x[:, 1], y[:, 1], 'o', color = "#1f77b4")
dot3, = ax.plot(x[:, 2], y[:, 2], 'o', color = "#ff7f0e")

trail4, = ax.plot(x[:, 0], y[:, 0], '-.', color = "#2ca02c")
trail5, = ax.plot(x[:, 1], y[:, 1], '-.', color = "#1f77b4")
trail6, = ax.plot(x[:, 2], y[:, 2], '-.', color = "#ff7f0e")

ani = animation.FuncAnimation(fig, update, size, fargs=(dot1, dot2, dot3, trail4, trail5, trail6, x, y), interval = 1)

plt.show()