import statistics

def analyze_sales():

    try:
        with open("sales.txt", "r") as file:

            sales = []

            for line in file:
                sales.append(float(line.strip()))

        mean_sales = statistics.mean(sales)
        median_sales = statistics.median(sales)

        print("Sales Statistics Summary")
        print(f"Sales Data: {sales}")
        print(f"Mean: {mean_sales:.2f}")
        print(f"Median: {median_sales:.2f}")

    except FileNotFoundError:
        print("File not found")

    except ValueError:
        print("Invalid data in file")


analyze_sales()