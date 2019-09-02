import numpy as np 
import matplotlib.pyplot as plt
import os

class ResultVisualizer():
    def __init__(self, x, y, t, x_no_drag, y_no_drag, t_no_drag, u_0):
        fig, ax = plt.subplots()
        fig.suptitle("Bottle Rocket Simulation")
        ax.set_xlabel("y / [m]")
        ax.set_ylabel("x / [m]")
        ax.axis("equal")
        ax.grid("on")
        
        ax.plot(x, y, 
            label = "Flight path", zorder = 10)
        
        ax.scatter([x[0]], [y[0]], zorder = 11, color = "c", marker = "x",
            label = "Initial velocity: %0.2f m/s" %(u_0))

        max_value_index = np.argmax(y)
        max_height_coordinates = [x[max_value_index], y[max_value_index], t[max_value_index]]
        ax.scatter([max_height_coordinates[0]], [max_height_coordinates[1]], zorder = 12, color = "g",marker = "x",
            label = "Max height coordinates: (%0.2f m, %0.2f m)"%(max_height_coordinates[0], max_height_coordinates[1]))

        first_negative_y_index = np.argmax(y < 0)
        flight_length = x[first_negative_y_index]
        flight_duration = t[first_negative_y_index]
        ax.scatter([flight_length], 0, color = "r", marker = "x", zorder = 11,
            label = "Flight length: %0.2f m after %0.2f s" %(flight_length, flight_duration))


        no_drag_first_negative_y_index = np.argmax(y_no_drag < 0)
        no_drag_flight_length = x_no_drag[no_drag_first_negative_y_index]
        ax.plot(x_no_drag, y_no_drag, '--',
            label = "Path without air resistance: %0.2f m"%(no_drag_flight_length))

        ax.plot([min(x_no_drag), (max(x_no_drag)*1.05)], [0, 0], "--k")

        ax.legend()

    def show_plot(self):
        plt.show()

    def save_plot(self, path = "result.png"):
        plt.savefig(path, dpi = 300, facecolor = ".85", edgecolor = "k")
        os.startfile(path)