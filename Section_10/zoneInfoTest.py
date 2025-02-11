from datetime import datetime, timezone
try: # Importing conditionally
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)
print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
print(ny_now)


print()
print("Available timezone keys: ")
print('-' * 23)

for zoneKey in sorted(zoneinfo.available_timezones()):
    print(zoneKey)