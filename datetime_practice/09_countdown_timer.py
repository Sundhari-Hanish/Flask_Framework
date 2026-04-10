from datetime import datetime

future_date = datetime(2026, 1, 1)
now = datetime.now()

remaining = future_date - now

print("Time left:", remaining)