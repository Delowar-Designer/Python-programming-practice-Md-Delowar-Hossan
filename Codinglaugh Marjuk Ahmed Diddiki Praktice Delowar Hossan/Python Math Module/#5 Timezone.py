# Timezone

import pytz

print(pytz.all_timezones)

print(pytz.common_timezones)

print(len(pytz.all_timezones))

print(len(pytz.common_timezones))

t = []
for i in pytz.all_timezones:
    for j in pytz.common_timezones:
        if i == j:
            t.append(i)

print(len(t))


print(pytz.country_names["bd"])


from datetime import datetime

t = pytz.timezone("Asia/Dhaka")

print(datetime.now(t))
print(t)

print(datetime.now())

h = datetime.now(t)

print(h.astimezone(pytz.utc))

print(datetime(2024, 1, 2))