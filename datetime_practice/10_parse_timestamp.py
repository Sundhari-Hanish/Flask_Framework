from datetime import datetime

log_time = "2026-04-09 10:30:45"

parsed = datetime.strptime(log_time, "%Y-%m-%d %H:%M:%S")

print("Parsed:", parsed)