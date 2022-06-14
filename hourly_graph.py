import Graph
import datetime


def main():
    today = str(datetime.datetime.now()).split()[0]
    current_hour = str(datetime.datetime.now()).split()[1].split(":")[0]
    date_hour = input("What hourly file do you want to graph? Enter the date and hour with "
                      "a comma in between (yyyy-mm-dd, 24-hour time): ").split(",")
    file = "hourly_files/" + date_hour[0] + "/" + date_hour[1] + ".txt"
    
    if (date_hour[0] == today) and (date_hour[1] == current_hour):
        print("dynamic")
        Graph.graph_dynamic(file)
    else:
        print("static")
        Graph.graph_static(file)


if __name__ == "__main__":
    main()