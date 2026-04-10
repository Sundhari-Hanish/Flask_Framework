from datetime import datetime, timedelta

today = datetime.now()

days_ahead = 0 - today.weekday() + 7
next_monday = today + timedelta(days=days_ahead)

print("Next Monday:", next_monday.date())