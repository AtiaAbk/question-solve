def attempt_task():
    for attempt in range(1, 4):
        result = input(f"attempt {attempt} - enter 'success' or 'fail': ")
        if result.strip().lower() == "success":
            return f"Task completed "
    return "task failed."

print(attempt_task())