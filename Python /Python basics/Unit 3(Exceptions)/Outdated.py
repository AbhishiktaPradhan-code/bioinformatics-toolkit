def main():
    # List of valid month names
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        try:
            date = input("Date: ").strip()

            # Handle format like MM/DD/YYYY
            if "/" in date:
                month, day, year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

            # Handle format like Month Day, Year
            elif "," in date:
                month_day, year = date.split(",")
                year = int(year.strip())
                month_str, day = month_day.strip().split()
                day = int(day)
                if month_str in months and 1 <= day <= 31:
                    month = months.index(month_str) + 1
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

        except (ValueError, IndexError):
            pass  # Invalid input, will prompt again

        # If parsing fails, ask again
        continue


if __name__ == "__main__":
    main()