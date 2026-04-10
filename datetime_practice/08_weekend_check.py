from datetime import datetime
today = datetime.now()
if today.weekday() >= 5:
    print("Weekend")
else:
    print("Weekday")