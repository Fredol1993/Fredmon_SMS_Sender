from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from plyer import sms

class SMSApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        self.phone_label = Label(text="Phone Number:")
        self.phone_input = TextInput(hint_text="e.g. 08123456789", multiline=False)

        self.message_label = Label(text="Message:")
        self.message_input = TextInput(hint_text="Enter your message here...", multiline=True)

        self.send_button = Button(text="Send SMS", on_press=self.send_sms)

        self.status_label = Label(text="")

        self.layout.add_widget(self.phone_label)
        self.layout.add_widget(self.phone_input)
        self.layout.add_widget(self.message_label)
        self.layout.add_widget(self.message_input)
        self.layout.add_widget(self.send_button)
        self.layout.add_widget(self.status_label)

        return self.layout

    def send_sms(self, instance):
        recipient = self.phone_input.text.strip()
        message = self.message_input.text.strip()

        if recipient and message:
            try:
                sms.send(recipient=recipient, message=message)
                self.status_label.text = f"Message sent to {recipient}"
            except Exception as e:
                self.status_label.text = f"Error: {str(e)}"
        else:
            self.status_label.text = "Please enter phone number and message."

if __name__ == "__main__":
    SMSApp().run()
