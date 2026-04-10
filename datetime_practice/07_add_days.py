from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=10)

print("Future date:", future)