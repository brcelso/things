from datetime import datetime

def count_days(start_date, end_date):
  """
  This function calculates the number of days between two given dates.

  Args:
      start_date: The start date in YYYY-MM-DD format (inclusive).
      end_date: The end date in YYYY-MM-DD format (inclusive).

  Returns:
      The number of days between the start and end date (inclusive).
  """

  # Convert strings to datetime objects
  start_date = datetime.strptime(start_date, "%Y-%m-%d")
  end_date = datetime.strptime(end_date, "%Y-%m-%d")

  # Calculate the difference in days
  delta = end_date - start_date
  return delta.days + 1  # Add 1 to include the start and end date

# Example usage (assuming today's date is 2023-11-21)
start_date = "2023-11-10"
end_date = "2023-11-21"

number_of_days = count_days(start_date, end_date)
print(f"There are {number_of_days} days between {start_date} and {end_date}.")
