import zoneinfo
from datetime import datetime, timezone

# parisTime = zoneinfo.ZoneInfo('Europe/Paris')
# parisNow = datetime.now(tz= parisTime)
#
# print(f'The time in Paris is: {parisNow}')
#
# londonTime = zoneinfo.ZoneInfo('Europe/London')
# londonNow = datetime.now(tz= londonTime)
#
# print(f'The time in London is: {londonNow}')
#
# hongKongTime = zoneinfo.ZoneInfo('Asia/Hong_Kong')
# hongKongNow = datetime.now(tz= hongKongTime)
#
# print(f'The time in Hong Kong is: {hongKongNow}')
#
# nairobiTime = zoneinfo.ZoneInfo('Africa/Nairobi')
# nairobiNow = datetime.now(tz= nairobiTime)
#
# print(f'The time in Nairobi is: {nairobiNow}')

zones = (
    'Europe/Paris',
    'Europe/London',
    'Asia/Hong_Kong',
    'Africa/Nairobi'
)

utcNow = datetime.now(tz=timezone.utc)
utcNow = utcNow.replace(microsecond=0)

for zone in zones:
    tz = zoneinfo.ZoneInfo(zone)
    requiredTime = utcNow.astimezone(tz)

    city = zone.split('/')[-1]
    print(f'The time in {city} is {requiredTime}')