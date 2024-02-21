def main():
    print("Welcome to tip calculator\n")
    totalbill = float(input("What was the total bill?\n"))
    noofpeople = int(input("How many people to split the bill?\n"))
    percentageoftip = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))

    eachpersonpay = (totalbill + totalbill * percentageoftip / 100) / noofpeople

    print(f"Each person should pay {eachpersonpay}")


if __name__ == "__main__":
    main()
