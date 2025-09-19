import pandas as pd

## Given array of events with user_id and timestamp, compute per-user session count
# where session gap > 30 minutes

data = {
    "user_id": [1,1,1,2,2,3],
    "event": ["open","click","close","open","click","open"],
    "timestamp": [
        "2025-08-01 09:00:00",
        "2025-08-01 09:10:00",
        "2025-08-01 10:00:00",
        "2025-08-01 09:05:00",
        "2025-08-01 09:50:00",
        "2025-08-01 09:30:00",
    ],
    "value": [10, 0, 5, 7, 3, 8]
}
df = pd.DataFrame(data)
df['timestamp'] = pd.to_datetime(df['timestamp'])

# group by / aggregations
agg = df.groupby('user_id').agg(
    total_value = ('value', 'sum'),
    last_timestamp = ('timestamp', 'max'),
    event_count = ('event', 'size')
).reset_index()
print(agg)
print()
# join/merge
users = pd.DataFrame({"user_id":[1,2,3], "country":["US", "CA", "US"]})
df = df.merge(users, on='user_id', how='left')
print(df)
print()
# pivot
pivot = df.pivot_table(index='user_id', columns='event', values='value', \
                       aggfunc='count', fill_value=0).reset_index()
print(pivot)
print()

# session gap > 30 mins
df = df.sort_values(['user_id', 'timestamp'])
df['prev_timestamp'] = df.groupby('user_id')['timestamp'].shift(1)
df['gap_minutes'] = (df['timestamp'] - df['prev_timestamp']).dt.total_seconds() / 60
df['new_session'] = (df['gap_minutes'] > 30) | df['prev_timestamp'].isna()
df['session_id'] = df.groupby('user_id')['new_session'].cumsum()
print(df)
print()

# compute session durations:
session_stats = df.groupby(['user_id', 'session_id']).agg(
    session_start = ('timestamp', 'min'),
    session_end = ('timestamp', 'max'),
    events = ('event', 'count')
).reset_index()
session_stats['duration_min'] = (session_stats['session_end'] - session_stats['session_start']).dt.total_seconds() / 60
print(session_stats)
print()






