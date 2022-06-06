"""
This file will create graphs every five or ten minutes based on data from a file with copied information
from the main data stream
"""

import matplotlib.pyplot as plt
import numpy as np
from TextSim import data_lines


# import time

# This is a class for each data point, with a value for time, x, y, and z
class Measurement:
    def __init__(self, line):
        self.line = line

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

    def __str__(self):
        return "Time: " + str(self.time) + " X: " + str(self.x) + " Y: " + str(self.y) + " Z: " + str(self.z)

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

    # all_measurements.reverse()
    return all_measurements


# Graphs a file that is being updated
def graph_dynamic(file):
    title = file.split("\\")[-1]
    plt.ion()
    plt.ylim(-40000, 40000)
    plt.show()

    while True:
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

        plt.draw()
        plt.pause(5)

        data_lines(file, "09:54:35:", 5)
        plt.clf()
        print("after clear")


# Graphs a file that is not being changed
def graph_static(file):
    title = file.split("\\")[-1]
    plt.ylim(-40000, 40000)

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

    plt.show()


def main():
    file = "C:\\Users\\Eben\\SourceCode\\MAGICIAN\\Graph Program\\Test Data\\" \
           "DataStreamer-master\\local_file_monitor\\day.txt"
    graph_static(file)


if __name__ == "__main__":
    main()
