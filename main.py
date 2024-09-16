import fastf1
import pandas as pd
from icecream import ic

# Get the date of the next race.
fastf1.Cache.enable_cache('.cache')
year = pd.Timestamp.now().year
schedule = fastf1.get_event_schedule(year)

# Get the next race
next_race = schedule[schedule['Session5DateUtc'] > pd.Timestamp.now()].iloc[0]

ic(next_race)