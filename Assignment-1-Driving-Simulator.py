print("Welcome to Driving Simulator")
t = int(input("Time Spent on the Road (s): "))
a = int(input("Acceleration (m/s2): "))
s = int(input("Target Distance (m): "))
speedlimit = 60
maxspeed = a * t #runs formula : v = u + at
for dur in range(0, t + 1): #dur represents duration of trip
    answer = (0.5 * a * (dur * dur)) #runs formula : S = (0.5)at2
    distance = int(answer) #converts answer from FLOAT to INTEGER, since in line 13 we are comparing with an INTEGER
    starreddistance = int(distance/10) #scales distance to be represented by stars
    print("Duration", dur, "second(s)", end="") #prints duration gradually
    print(" ", "Distance", "*" * starreddistance)
if distance>=s: #compares set distance with actual distance travelled
    print("The person reached the destination.", "(Reached ", distance, "m)")
else:
    print("The person did not reach the destination.", "(Reached", distance, "m)")
print("Target distance was", s, "m .")
if maxspeed > speedlimit: #compares ,maxspeed with speed limit, in this case it is 60 m/s
    print("The person went over the speed limit.", "(Max speed was", maxspeed, "m/s)")
else:
    print("The person did not go over the speed limit.", "(Max speed was ", maxspeed, "m/s)")
print("The Speed Limit was", speedlimit, "m/s.") #states the speed limit
print("Average Speed was", int(distance/t), "m/s.")
