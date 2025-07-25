import time
from collections import defaultdict
from fastapi import HTTPException, status

# --constants--
# for authenticated users
AUTH_RATE_LIMIT = 5
AUTH_TIME_WINDOW = 60

# for unauthenticated global users
GLOBAL_RATE_LIMIT = 3
GLOBAL_TIME_WINDOW_SECONDS = 60

# --In-memory storage for user requests--
user_requests = defaultdict(list)

# --throttling dependency--
def apply_rate_limit(user_id: str):
    current_time = time.time()

    if user_id == "global_unauthenticated_user":
        rate_limit = GLOBAL_RATE_LIMIT
        time_window = GLOBAL_TIME_WINDOW_SECONDS

    else:
        rate_limit = AUTH_RATE_LIMIT
        time_window = AUTH_TIME_WINDOW

    # filter out requests older than time window
    user_requests[user_id] = [
        t for t in user_requests[user_id] if t > current_time - time_window
    ]

    if len(user_requests[user_id]) >= rate_limit:
        raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                            detail="Too many requests. Please try again later.")
    else:
        # for debugging: print current usage
        current_usage = len(user_requests[user_id])
        print(f"User {user_id}: {current_usage+1}/{rate_limit} requests used.")

    user_requests[user_id].append(current_time)
    return True

