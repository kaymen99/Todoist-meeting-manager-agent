import os, requests, time

def send_message(text):
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    CHAT_ID = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"
    response = requests.get(url).json()
    if not response["ok"]:
        return "Failed to send message"

    # Get the timestamp right after sending the message
    message_sent_timestamp = response["result"]["date"]
    print(f"Sent: {text}")

    start_time = time.time()
    timeout = 120  # 2 minutes in seconds

    while True:
        if time.time() - start_time > timeout:
            return "No response received within the timeout period"

        response = receive_message(message_sent_timestamp)
        if response == "No message received":
            time.sleep(2)  # Wait for 2 seconds before checking again
            continue

        print(f"Received: {response}")
        return response

def receive_message(after_timestamp):
    TOKEN = os.getenv("TELEGRAM_TOKEN")
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    response = requests.get(url).json()
    if not response["result"]:
        return "No message received"

    for update in response["result"]:
        message = update["message"]
        if message["date"] > after_timestamp:
            return message["text"]

    return "No message received"