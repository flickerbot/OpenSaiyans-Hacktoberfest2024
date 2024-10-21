# Print Hello, World!
print("Hello, World!")

from datetime import datetime
import pytz
import tzlocal

# Get the current UTC time
utctime = datetime.now(pytz.utc)

# Get the local time zone
local_timezone = tzlocal.get_localzone()

# Get the current time in the local time zones
localtime = datetime.now(local_timezone)

print("UTC Time:", utctime)
print("Local Time:", localtime)
