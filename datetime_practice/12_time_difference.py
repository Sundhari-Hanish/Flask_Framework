from datetime import datetime

t1 = datetime(2026, 4, 9, 10, 0, 0)
t2 = datetime(2026, 4, 9, 15, 30, 0)

diff = t2 - t1

hours = diff.total_seconds() / 3600

print("Hours difference:", hours)