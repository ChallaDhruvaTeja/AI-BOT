import pyttsx4
import speech_recognition as sr
import datetime
import wikipedia
import wolframalpha
import webbrowser
import os
from tkinter import *

import Training

# Initialization
r = sr.Recognizer()
machine = pyttsx4.init()
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)
machine.setProperty('rate', 185)


def talk(text):
    machine.say(text)
    machine.runAndWait()


def get_time_greeting():
    current_time = datetime.datetime.now().hour

    if 5 <= current_time < 12:
        greeting = "Good morning!"
    elif 12 <= current_time < 17:
        greeting = "Good afternoon!"
    elif 17 <= current_time < 24:
        greeting = "Good evening!"
    else:
        greeting = "Go to sleep!"

    return greeting


def open_website(instruction):
    websites = {
        'google': "https://www.google.com",
        'youtube': "https://www.youtube.com",
        'geek for geeks': "https://www.geeksforgeeks.org/",
        'anime': "https://yugenanime.tv/",
        'netflix': "https://www.netflix.com/in/",
        'amazon': "https://www.amazon.com/",
        'chat': "https://chat.openai.com/"
    }

    for keyword, url in websites.items():
        if keyword in instruction:
            talk(f"opening {keyword}")
            webbrowser.open(url)
            return

    print("Website not found for the given instruction.")


def take_command():
    try:
        with sr.Microphone(device_index=0) as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            speech = r.listen(source, timeout=5)  # Increase timeout to allow more time for speaking
            instruction = r.recognize_google(speech).lower()
            if "lily" in instruction:
                return instruction.replace('lily', "")
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"Could not request results from Google; {e}")
    return None


def create_file():
    talk(f"creating your file...please enter your path")
    path = input("Enter your path:")

    try:
        dir_list = os.listdir(path)
        print("List of directories and files before creation:")
        print(dir_list)
        print()

        with open(input("Enter file name:"), 'w'):
            pass

        dir_list = os.listdir(path)
        print("List of directories and files after creation:")
        print(dir_list)

    except FileNotFoundError:
        print(f"The specified path '{path}' does not exist.")
    except PermissionError:
        print("Permission denied. Unable to create file.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_file():
    talk("Please enter your file name and path")
    file = input("Enter the file name:")
    location = input("Enter the path:")

    path = os.path.join(location, file)

    try:
        os.remove(path)
        talk("File deleted successfully")
        print("File deleted successfully")
    except FileNotFoundError:
        print(f"File '{file}' not found at location '{location}'.")
    except PermissionError:
        print(f"Permission denied. Unable to delete file '{file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def write_file():
    talk("Please enter your path")
    path = input("Enter the path:")

    try:
        with open(path, 'w') as file:
            talk("Now, please enter your data")
            s = input("Enter the input text:")
            file.write(s)
            talk(f"Text successfully written to '{path}'")
            print(f"Text successfully written to '{path}'")

    except FileNotFoundError:
        print(f"The specified path '{path}' does not exist.")
    except PermissionError:
        print(f"Permission denied. Unable to write to '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_file():
    talk("Please enter file name along with the path")
    file_path = input("Enter the file name along with the path:")

    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
            talk(content)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to read from '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def create_folder():
    talk("Please enter the path")
    path = input("Enter the path:")

    try:
        os.mkdir(path)
        talk(f"Folder '{path}' created successfully.")
        print(f"Folder '{path}' created successfully.")
    except FileExistsError:
        print(f"The folder '{path}' already exists.")
    except PermissionError:
        print(f"Permission denied. Unable to create folder '{path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_folder():
    talk("Please enter folder name as well as path")
    folder = input("Enter the folder name:")
    location = input("Enter the path:")

    path = os.path.join(location, folder)

    try:
        os.rmdir(path)
        talk(f"Folder '{path}' deleted successfully.")
        print(f"Folder '{path}' deleted successfully.")
    except FileNotFoundError:
        print(f"Folder '{path}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to delete folder '{path}'.")
    except OSError as error:
        print(f"An error occurred: {error}")


def rename():
    talk("Please enter existing file/directory name along with path")
    source = input("Enter the existing file/directory name with path:")

    dest = input("Enter the new file/directory name with path:")

    try:
        os.rename(source, dest)
        talk("Renaming Successfully done")
        print("Renaming Successfully done")

    except IsADirectoryError:
        print("You have entered one of the given values a file and the other as directory")

    except NotADirectoryError:
        print("You have entered one of the given values a file and the other as directory")

    except PermissionError:
        print("Operation not permitted.")

    except OSError as error:
        print(error)


def replace_text():
    talk("Please enter file name with path")
    file_path = input("Enter the file name with path:")

    try:
        with open(file_path, "r+") as file:
            text = input("Enter your new text:")
            file.truncate(0)
            file.write(text)
            talk("Text replaced successfully")
            print("Text replaced successfully")

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied. Unable to replace text in '{file_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def shutdown_system():
    try:
        shutdown = input("Do you wish to shutdown your system? (Yes/No):").lower()

        if shutdown == 'no':
            exit()
        elif shutdown == 'yes':
            os.system("shutdown /s /t 5")  # /t 5 sets a delay of 5 second before shutdown
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    except Exception as e:
        print(f"An error occurred during shutdown: {e}")


def restart_system():
    try:
        restart = input("Do you wish to restart your system? (Yes/No):").lower()

        if restart == 'no':
            exit()
        elif restart == 'yes':
            os.system("shutdown /r /t 5")  # /r for restart, /t 5 sets a delay of 5 second
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    except Exception as e:
        print(f"An error occurred during system restart: {e}")


def system_sleep():
    try:
        sleep = input("Do you wish to hibernate your system? (Yes/No):").lower()

        if sleep == 'no':
            exit()
        elif sleep == 'yes':
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")

    except Exception as e:
        print(f"An error occurred during system hibernation: {e}")


def find_location():
    import phonenumbers
    from phonenumbers import geocoder, carrier
    from opencage.geocoder import OpenCageGeocode
    import folium

    number = input("Enter your phone_no with country code:")
    pepnumber = phonenumbers.parse(number)
    location = geocoder.description_for_number(pepnumber, "en")
    print(location)

    service_pro = phonenumbers.parse(number)
    print(carrier.name_for_number(service_pro, "en"))

    key = "9a55700d7a4a4a36a3f26b0b4b2ecd08"

    geocoder = OpenCageGeocode(key)
    query = str(location)
    results = geocoder.geocode(query)

    lat = results[0]["geometry"]['lat']
    lng = results[0]["geometry"]['lng']

    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    html_file_path = "mylocation.html"
    myMap.save(html_file_path)

    webbrowser.open(html_file_path)
    

def notifier():
    from plyer import notification
    from tkinter import messagebox
    from PIL import Image, ImageTk
    import time

    t = Tk()
    t.title('Notifier')
    t.geometry("480x350")  # Increased height to accommodate date input
    img = Image.open("notify-label.png")
    tkimage = ImageTk.PhotoImage(img)

    # Validate time format
    def validate_time_format(input_time):
        if len(input_time) != 5:
            return False
        if not input_time[0:2].isdigit() or not input_time[3:5].isdigit():
            return False
        if input_time[2] != ':':
            return False
        hours = int(input_time[0:2])
        minutes = int(input_time[3:5])
        if hours < 0 or hours >= 24 or minutes < 0 or minutes >= 60:
            return False
        return True

    # Validate date format
    def validate_date_format(input_date):
        try:
            time.strptime(input_date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    # Get details
    def get_details():
        get_title = title.get()
        get_msg = msg.get()
        get_time = time_entry.get()
        get_date = date_entry.get()

        if get_title == "" or get_msg == "" or get_time == "" or get_date == "":
            messagebox.showerror("Alert", "All fields are required!")
        elif not validate_time_format(get_time):
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format")
        elif not validate_date_format(get_date):
            messagebox.showerror("Invalid Date", "Please enter a valid date in YYYY-MM-DD format")
        else:
            try:
                target_time = time.strptime(f"{get_date} {get_time}", "%Y-%m-%d %H:%M")
                current_time = time.localtime()

                # Calculating total seconds until target time
                total_seconds = time.mktime(target_time) - time.mktime(current_time)
                if total_seconds <= 0:
                    raise ValueError("Selected time has already passed")

                messagebox.showinfo("Notifier Set", "Notification Set Successfully!")
                t.destroy()
                time.sleep(total_seconds)

                notification.notify(title=get_title,
                                    message=get_msg,
                                    app_name="Notifier",
                                    app_icon="ico.ico",
                                    toast=True,
                                    timeout=10)
            except ValueError as ve:
                messagebox.showerror("Error", str(ve))

    Label(t, image=tkimage).grid()

    # Label - Title
    t_label = Label(t, text="Title to Notify", font=("poppins", 10))
    t_label.place(x=12, y=80)

    # ENTRY - Title
    title = Entry(t, width=25, font=("poppins", 13))
    title.place(x=123, y=80)

    # Label - Message
    m_label = Label(t, text="Display Message", font=("poppins", 10))
    m_label.place(x=12, y=125)

    # ENTRY - Message
    msg = Entry(t, width=35, font=("poppins", 12))
    msg.place(x=123, height=30, y=125)

    # Label - Date
    date_label = Label(t, text="Set Date (YYYY-MM-DD)", font=("poppins", 10))
    date_label.place(x=12, y=180)

    # ENTRY - Date
    date_entry = Entry(t, width=15, font=("poppins", 13))
    date_entry.place(x=180, y=180)

    # Label - Time
    time_label = Label(t, text="Set Time (HH:MM)", font=("poppins", 10))
    time_label.place(x=12, y=220)

    # ENTRY - Time
    time_entry = Entry(t, width=10, font=("poppins", 13))
    time_entry.place(x=135, y=220)

    # Button
    but = Button(t, text="SET NOTIFICATION", font=("poppins", 10, "bold"), fg="#ffffff", bg="#528DFF", width=20,
                 relief="raised",
                 command=get_details)
    but.place(x=160, y=280)

    t.resizable(False, False)
    t.mainloop()


def run_command():
    instruction = ''
    while instruction != 'exit':
        instruction = take_command()
        print(instruction)
        if instruction:
            if 'exit' in instruction:
                break

            if 'time' in instruction:
                time = datetime.datetime.now().strftime("%I:%M %p")
                greeting = get_time_greeting()
                talk(f"{greeting} The current time is: {time}")
                print(time)

            elif 'date' in instruction:
                date = datetime.datetime.now().strftime('%d /%m /%y')
                talk("Today's date is " + date)
                print(date)

            elif 'find my location' in instruction:
                find_location()

            elif any(keyword in instruction for keyword in
                     ['google', 'youtube', 'geek for geeks', 'anime', 'netflix', 'amazon', 'chat']):
                open_website(instruction)

            elif 'create file' in instruction:
                create_file()

            elif 'delete file' in instruction:
                delete_file()

            elif 'write file' in instruction:
                delete_file()

            elif 'read file' in instruction:
                read_file()

            elif 'create folder' in instruction:
                create_folder()

            elif 'delete folder' in instruction:
                delete_folder()

            elif 'rename' in instruction:
                rename()

            elif 'replace text' in instruction:
                replace_text()

            elif 'shutdown system' in instruction:
                shutdown_system()

            elif 'restart system' in instruction:
                restart_system()

            elif 'sleep' in instruction:
                system_sleep()

            elif 'notify me' in instruction:
                notifyy()

            elif 'who am i' in instruction:
                Training.recognize()

            elif ' ' in instruction:
                try:
                    app_id = '3TTWQK-VVRPYWPJQ3'
                    client = wolframalpha.Client(app_id)
                    res = client.query(instruction)
                    answer = next(res.results).text
                    print(answer)
                    talk("Your Answer is " + answer)

                finally:
                    instruction = " ".join(instruction.split(' ')[0:])
                    talk(f"I am Searching for {instruction}")
                    print(wikipedia.summary(instruction, sentences=3))
                    talk(wikipedia.summary(instruction, sentences=3))


if __name__ == '__main__':
    run_command()
