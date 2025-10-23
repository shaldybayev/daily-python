from datetime import datetime

def main():
    today = datetime.now().strftime("%Y-%m-%d %H:%M%S")
    message = f"Today's Python session started at {today}!"
    print(message)

if __name__ == "__main__":
    main()
