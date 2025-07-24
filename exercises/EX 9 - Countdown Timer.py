import time
my_time = int(input("Enter the time in seconds: "))


for i in range (my_time, 0, -1):
    secs = i % 60
    mins = int(i/60) % 60
    hours = int(i/3600)
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("TIME'S UP!")