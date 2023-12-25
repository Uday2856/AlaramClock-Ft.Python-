# Import the modules
import tkinter as tk
import time
import datetime
import winsound

# Create the main window
window = tk.Tk()
window.title("Alarm Clock")
window.geometry("300x200")

# Create a label to display the current time
time_label = tk.Label(window, font=("Arial", 20))
time_label.pack()

# Create a function to update the current time
def update_time():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    # Display the current time on the label
    time_label.config(text=current_time)
    # Call the function again after 1 second
    window.after(1000, update_time)

# Create a label to display the instruction
instruction_label = tk.Label(window, text="Enter the alarm time in 24-hour format (HH:MM:SS)")
instruction_label.pack()

# Create an entry to get the user input
alarm_entry = tk.Entry(window)
alarm_entry.pack()

# Create a function to set the alarm
def set_alarm():
    # Get the user input
    alarm_time = alarm_entry.get()
    # Validate the user input
    try:
        # Convert the user input to a datetime object
        alarm_time = datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        # Display a confirmation message
        confirmation_label.config(text=f"Alarm set for {alarm_time.strftime('%H:%M:%S')}")
        # Call the check_alarm function
        check_alarm(alarm_time)
    except ValueError:
        # Display an error message
        confirmation_label.config(text="Invalid time format")

# Create a function to check the alarm
def check_alarm(alarm_time):
    # Get the current time
    current_time = datetime.datetime.now()
    # Compare the current time and the alarm time
    if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute and current_time.second == alarm_time.second:
        # Play a sound
        winsound.PlaySound("alarm.wav", winsound.SND_ASYNC)
    else:
        # Call the function again after 1 second
        window.after(1000, check_alarm, alarm_time)

# Create a button to set the alarm
set_button = tk.Button(window, text="Set Alarm", command=set_alarm)
set_button.pack()

# Create a label to display the confirmation or error message
confirmation_label = tk.Label(window)
confirmation_label.pack()

# Call the update_time function
update_time()

# Start the main loop
window.mainloop()
