`notifications.py`
This module will handle alerts for stress.
class Notifications:
    def send_alert(self, employee_id, mood):
        if mood == 'stressed':
            print(f"Alert: Employee {employee_id} is stressed. Notify HR.")
