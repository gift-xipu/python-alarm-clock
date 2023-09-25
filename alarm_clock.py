#playsound allows us to play audio files
from playsound import playsound
import time
#this function allows us to manipulate the terminal
#in this case CLEAR will cleat the terminal when we run the command
CLEAR = "\033[2J"
#clear and return will update the terminal on the same line while the code is running instead of a new line
CLEAR_AND_RETURN = "\033[H"
#passes in the variable of seconds
def alarm(seconds):
    time_elapsed = 0;

    print(CLEAR)
    while time_elapsed < seconds:
        #tells the code to wait for one second, this is to make the code more realistic as otherwise it will just run as quickly as possible
        time.sleep(1)
        time_elapsed += 1
        #these next lines calculate the remaining time by subtracting the "time_elapsed" from the "seconds" parameter
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        #02d is to ensure minutes_left and seconds_left are displayed as two-digit numbers
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    
    playsound("alarm.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)


#playsound("alarm.mp3")