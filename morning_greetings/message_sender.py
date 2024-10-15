def send_message(email, message):
    '''Sends a greeting to a specific email address'''
    if not email:
        raise ValueError("Email address is missing")
    print(f"Sending message to {email}: {message}")
