def attempt_task():
    for attempt in range(1, 4):
        result = input(f"attempt {attempt} - enter 'success' or 'fail': ")

        try:
            if result.strip().lower() not in ["success", "fail"]:
                raise ValueError("Invalid input. Please enter 'success' or 'fail'.")
        except ValueError as e:
            print(e)
            continue
        if result.strip().lower() == "success":
            return f"Task completed "
    return "task failed."

print(attempt_task())