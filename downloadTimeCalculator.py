# Author: Mustafa Osman Dilmaç
# Date: 14.05.2023

# A program made by me to calculate how long will it take to download some apps/games/files etc.
# Because I have 5mpbs download and 0.2 mbps upload and it's important for me to know how long will it take to download a large files.
# Yeah, year is 2023 and this is my internet speed unfortunately.

print("""

Download Time Calculator v0.1

Made with love and hate :D

I'm so bored

""")
while True:
    while True:
        try:
            speed = float(input("Current internet speed (mpbs): ")) # 1 Mbps = 0.125 MB/s
            if speed < 0:
                speed = speed * -1
            break
        except ValueError:
            print("You must provide an acceptable value!")

    while True:
        try:
            file_size = float(input("MB of data/file that will be downloaded: "))
            if file_size < 0:
                file_size = file_size * -1
            break
        except ValueError:
            print("You must provide an acceptable value!")

    speed_mb = speed * 0.125
    time = file_size / speed_mb
    time_min = time/60
    time_hour = time_min/60

    time, time_min, time_hour = [round(num, 2) for num in [time, time_min, time_hour]] # list comprehension waoww xd

    print("It'll approximately take {} seconds, {} minutes or {} hours to download this data/file.".format(time,time_min,time_hour))

    breaker = input("If you want to calculate again type 'Y'. Else the program will terminate itself. >> ")
    if breaker == "Y" or breaker == "y":
        continue
    else:
        break