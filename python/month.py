from datetime import datetime, timedelta
import calendar


def fibonacci_up_to(n):
  """
  Calculates Fibonacci numbers up to a given maximum value (n).

  Args:
      n: The maximum value (inclusive).

  Returns:
      A list of Fibonacci numbers up to n.
  """
  a, b = 0, 1
  fibonacci_sequence = []
  while a <= n:
    fibonacci_sequence.append(a)
    a, b = b, a + b
  return fibonacci_sequence


def count_months(start_date, end_date):
  """
  This function calculates the number of months between two given dates, iterates
  through each month, and displays the month along with its corresponding Fibonacci sequence number in the desired format.

  Args:
      start_date: The start date in YYYY-MM-DD format (inclusive).
      end_date: The end date in YYYY-MM-DD format (inclusive).

  Returns:
      None
  """

  # Convert strings to datetime objects
  start_date = datetime.strptime(start_date, "%d-%m-%Y")
  end_date = datetime.strptime(end_date, "%d-%m-%Y")

  # Iterate through each month until reaching the end date
  current_date = start_date
  month_count = 1
  while current_date <= end_date:
    # Check if the current month is in the Fibonacci sequence
    if month_count in fibonacci_up_to(month_count):
      fibonacci_number = fibonacci_up_to(month_count)[-1]  # Get the last element (current fibonacci number)
      month_str = f"Month {month_count:02d}"  # Format month with leading zero
      print(f"{month_str}: {current_date.strftime('%d-%m-%Y')}")

    # Move to the next month
    days_in_current_month = calendar.monthrange(current_date.year, current_date.month)[1]
    current_date += timedelta(days = (days_in_current_month - current_date.day) + 1)
    month_count += 1

# Example usage (assuming today's date is 14-05-2024)
start_date = "11-09-2001"
end_date = "19-01-2090"

count_months(start_date, end_date)

