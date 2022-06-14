"""
This file will create graphs every five or ten minutes based on data from a file with copied information
from the main data stream
"""

import matplotlib.pyplot as plt
import numpy as np
# from TextSim import data_lines


# Sets the run condition to True for the graph_dynamic function
run = True
def on_close(evt="None"):
    global run
    run = False


# This is a class for each data point, with a value for time, x, y, and z
class Measurement:
    def __init__(self, line):
        self.line = line

        try:
            # Time
            line_time = line.split(" ")
            if len(line) == 2:
                self.time = "00:00:00"
            else:
                self.time = line_time[1].strip(":")
            # X
            line_x = line.split("X,")
            line_x = line_x[1].split(",")
            self.x = float(line_x[0])

            # Y
            line_y = line.split("Y,")
            line_y = line_y[1].split(",")
            self.y = float(line_y[0])

            # Z
            line_z = line.split("Z,")
            line_z = line_z[1].split(",")
            self.z = float(line_z[0])

            self.is_valid = True
                
        except (ValueError, IndexError):
            self.is_valid = False

    def __str__(self):
        return "Time: " + str(self.time) + " X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + \
               str(self.z)

    def __repr__(self):
        return self.line


# Loads a file with measurement formatting and returns each line as an item in a list
def load_file(file):
    handle = open(file, 'r')
    all_measurements = []
    lines = handle.readlines()
    for line in lines:
        item = Measurement(line)
        if item.is_valid:
            all_measurements.append(item)

    """
    if len(lines) <= 60:
        for line in lines:
            item = Measurement(line)
            if item.is_valid:
                all_measurements.append(item)
    elif len(lines) <= 120:
        print("<=120")
        for line in lines[0::2]:
            item = Measurement(line)
            if item.is_valid:
                all_measurements.append(item)
    else:
        print(">120")
        for line in lines[0::5]:
            item = Measurement(line)
            if item.is_valid:
                all_measurements.append(item)
    """
    # all_measurements.reverse()
    return all_measurements


# Graphs a file that is being updated
def graph_dynamic(file):
    fig = plt.figure()

    # Hides the toolbar
    fig.canvas.toolbar.pack_forget()

    # Sets the title of the graph to the name of the file
    title = file.split("\\")[-1]

    plt.ion()
    plt.show()

    fig.canvas.mpl_connect("close_event", on_close)
    global run
    while run:
        # Sets header
        plt.title("Graph of " + title)

        # Loads given file
        p1 = load_file(file)

        # Sets t, x, y, and z values based on file then plots them as lines
        t = list(map(lambda Measurement: Measurement.time, p1))
        x = list(map(lambda Measurement: Measurement.x, p1))
        y = list(map(lambda Measurement: Measurement.y, p1))
        z = list(map(lambda Measurement: Measurement.z, p1))

        plt.plot(t, x, label="x", color="red")
        plt.plot(t, y, label="y", color="blue")
        plt.plot(t, z, label="z", color="green")
        plt.legend(loc="lower right")

        # This method lets you customize axis ticks - the x-ticks are rotated 90 degrees
        # so that they all fit on screen and are legible
        plt.tick_params(axis="x", labelrotation=90, pad=1)

        # Omits some x labels to avoid crowding as more x labels come into play
        if len(x) <= 15:
            plt.xticks(np.arange(0, len(x), 1))
        elif len(x) < 45:
            plt.xticks(np.arange(0, len(x), 3))
        elif len(x) < 90:
            plt.xticks(np.arange(0, len(x), 8))
        elif len(x) < 160:
            plt.xticks(np.arange(0, len(x), 15))
        elif len(x) < 240:
            plt.xticks(np.arange(0, len(x), 23))
        elif len(x) < 320:
            plt.xticks(np.arange(0, len(x), 31))
        elif len(x) < 450:
            plt.xticks(np.arange(0, len(x), 44))
        elif len(x) < 900:
            plt.xticks(np.arange(0, len(x), 89))
        elif len(x) < 1500:
            plt.xticks(np.arange(0, len(x), 149))
        elif len(x) < 2000:
            plt.xticks(np.arange(0, len(x), 199))
        elif len(x) < 2500:
            plt.xticks(np.arange(0, len(x), 249))
        elif len(x) < 3000:
            plt.xticks(np.arange(0, len(x), 299))
        elif len(x) < 3500:
            plt.xticks(np.arange(0, len(x), 349))
        elif len(x) < 4000:
            plt.xticks(np.arange(0, len(x), 399))
        elif len(x) < 4500:
            plt.xticks(np.arange(0, len(x), 449))
        elif len(x) < 5000:
            plt.xticks(np.arange(0, len(x), 499))
        elif len(x) < 5500:
            plt.xticks(np.arange(0, len(x), 549))
        else:
            plt.xticks(np.arange(0, len(x), 2400))

        plt.draw()
        plt.pause(30)

        # data_lines(file, "09:54:35:", 5)
        plt.clf()
        print("after clear")


# Graphs a file that is not being changed
def graph_static(file):
    fig = plt.figure()

    # Finds the name of the file and sets it to the graph title
    title = file.split("/")[-1]

    # Turns off the toolbar
    fig.canvas.toolbar.pack_forget()

    # Sets header
    plt.title("Graph of " + title)

    # Loads given file
    p1 = load_file(file)

    # Sets t, x, y, and z values based on file then plots them as lines
    t = list(map(lambda Measurement: Measurement.time, p1))
    x = list(map(lambda Measurement: Measurement.x, p1))
    y = list(map(lambda Measurement: Measurement.y, p1))
    z = list(map(lambda Measurement: Measurement.z, p1))

    plt.plot(t, x, label="x", color="red")
    plt.plot(t, y, label="y", color="blue")
    plt.plot(t, z, label="z", color="green")
    plt.legend(loc="lower right")

    # This method lets you customize axis ticks - the x-ticks are rotated 90 degrees
    # so that they all fit on screen and are legible
    plt.tick_params(axis="x", labelrotation=90, pad=1)

    # Omits some x labels to avoid crowding as more x labels come into play
    if len(x) <= 15:
        plt.xticks(np.arange(0, len(x), 1))
    elif len(x) < 45:
        plt.xticks(np.arange(0, len(x), 3))
    elif len(x) < 90:
        plt.xticks(np.arange(0, len(x), 8))
    else:
        plt.xticks(np.arange(0, len(x), 2400))

    plt.show()


def main():
    file = "daily_files/2022-06-07.txt"
    graph_static(file)


if __name__ == "__main__":
    main()
