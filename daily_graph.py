import Graph
import datetime


def main():
    today = str(datetime.datetime.now()).split()[0]
    date = input("What daily file do you want to graph? Enter the date (yyyy-mm-dd): ")
    file = "daily_files/" + date + ".txt"
    
    if date == today:
        print("dynamic")
        Graph.graph_dynamic(file)
    else:
        print("static")
        Graph.graph_static(file)


if __name__ == "__main__":
    main()