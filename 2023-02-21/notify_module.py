from plyer import notification

def notify(numb: int) -> None:
    if numb >= 100:
        print("You should see a congratulation notification")
        notification.notify(
            title = "Hello, Laimonas",
            message = "You entered a large number",
            timeout = 10,
        )
    else:
        print("Small number, no notificationfor You")