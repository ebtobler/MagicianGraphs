# This program writes to a file to simulate a whole day of measurements


def write_to_file(file):
    handle = open(file, "w")
    hour = 00
    minute = 00
    sec = 00
    while hour <= 23:
        handle.writelines("1582350050,2020,25.66,23.02.20 "
                          + str(hour) + ":" + str(minute) + ":" + str(sec)
                          + ": X,-16871,46,Y,-33974,-44,Z,32913,-24,3" + "\n")

        sec += 2
        if sec == 60:
            sec = 0
            minute += 1
            if minute == 60:
                minute = 0
                hour += 1


# Time must be a string in format hh:mm:ss:
def data_lines(file, time, lines):
    handle = open(file, "a")

    time = time.split(":")
    hour = time[0]
    minute = time[1]
    second = time[2]

    for i in range(lines):
        handle.write("1582350050,1582451171,2020,25.66,23.02.20 " + hour + ":" + minute + ":" + second +
                     ": X,-16871,46,Y,-33974,-44,Z,32913,-24,3\n")

        int_hour = int(hour)
        int_minute = int(minute)
        int_second = int(second)

        int_second += 2
        if int_second == 60:
            int_second = 0
            int_minute += 1
            if int_minute == 60:
                int_minute = 0
                int_hour += 1
                if int_hour == 24:
                    int_hour = 0

        if len(str(int_hour)) == 1:
            hour = "0" + str(int_hour)
        else:
            hour = str(int_hour)
        if len(str(int_minute)) == 1:
            minute = "0" + str(int_minute)
        else:
            minute = str(int_minute)
        if len(str(int_second)) == 1:
            second = "0" + str(int_second)
        else:
            second = str(int_second)


def main():
    file = "Test Data\\DataStreamer-master\\local_file_monitor\\day.txt"

    write_to_file(file)
    # data_lines(file, "01:20:19:", 58)
    """
    t = "00:01:02:"
    t = t.split(":")
    print(t)
    """
    print("done")


if __name__ == "__main__":
    main()
