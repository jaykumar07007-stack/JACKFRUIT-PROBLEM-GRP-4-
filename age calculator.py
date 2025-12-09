from datetime import date

# --- INPUT ---
birth_str = input("Enter your birthdate (dd-mm-yyyy): ")

try:
    birth_day, birth_month, birth_year = map(int, birth_str.split("-"))
    # --- Birthdate object ---
    birth_date = date(birth_year, birth_month, birth_day)
except ValueError:
    print("Invalid date! Please enter a valid one (e.g., 24-09-2007).")
    exit()

# --- Today's date ---
today = date.today()

# --- Calculate difference ---
years = today.year - birth_date.year
months = today.month - birth_date.month
days = today.day - birth_date.day

# --- Adjust negatives ---
if days < 0:
    # borrow days from previous month
    months -= 1
    # find days in previous month
    prev_month = today.month - 1 or 12
    prev_year = today.year if today.month != 1 else today.year - 1
    days_in_prev_month = (date(prev_year, prev_month % 12 + 1, 1) - date(prev_year, prev_month, 1)).days
    days += days_in_prev_month

if months < 0:
    months += 12
    years -= 1

# --- Output ---
print(f"\nYou are {years} years, {months} months, {days} days old.")