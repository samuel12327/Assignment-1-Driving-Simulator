print("Welcome to Driving Simulator")
a = int(input("Acceleration (m/s2): "))
t = int(input("Duration (s): "))
s = int(input("Distance (m): "))
speedlimit = "Speed limit is 60 m/s"
maxspeed = a * t #runs formula : v = u + at
for dur in range(0, t + 1): #dur represents duration of trip
    answer = (0.5 * a * (dur * dur)) #runs formula : S = (0.5)at2
    distance = int(answer) #converts answer from FLOAT to INTEGER, since in line 13 we are comparing with an INTEGER
    starreddistance = int(distance/20) #scales distance to be represented by stars
    print("Duration", dur, "second(s)", end="") #prints duration gradually
    print(" ", "Distance", "*" * starreddistance)
if distance>=s: #compares set distance with actual distance travelled
    print("The person reached the destination.", "(Reached ", distance, "m)")
else:
    print("The person did not reach the destination.", "(Reached ", distance, "m)")
print("Set distance was", s, "m .")
if maxspeed > 60: #compares ,maxspeed with speed limit, in this case it is 60 m/s
    print("The person went over the speed limit.", "(Max speed was ", maxspeed, "m/s)")
else:
    print("The person did not go over the speed limit.", "(Max speed was ", maxspeed, "m/s)")
print(speedlimit, ".")
print("Average Speed was", int(distance/t), "m/s .")
