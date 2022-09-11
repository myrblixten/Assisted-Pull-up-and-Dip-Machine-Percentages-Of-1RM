WeightOnMachine = int(input("What weight did you put on the assist machine? "))
Repetitions = int(input("How many reps did you do? "))
BW = int(input("What is your bodyweight? "))
what_percent = float(input("What percent do you want of your 1RM or TM? (in decimal so 10% is 0.1) "))
RMorTM = input("Do you want % of 1RM or TM? (rm or tm all lower) ")
real_percent = what_percent*100
WeightLifted = (BW - WeightOnMachine)
Estimated1RM = WeightLifted*Repetitions*0.0333+WeightLifted
TrainingMax = Estimated1RM * 0.9

print("Estimated 1 Rep Max: " + str(Estimated1RM))
print("Training Max (90% of 1RM): " + str(TrainingMax))

if RMorTM == "rm":
    rm_percent = Estimated1RM*what_percent
    print(rm_percent)
    WeightToPutOn = BW - rm_percent
if RMorTM == "tm":
    tm_percent = TrainingMax*what_percent
    print(str(real_percent) + "% of your Training Max: " + str(TrainingMax*what_percent))
    WeightToPutOn = BW - tm_percent


print("You should put the machine on " + str(WeightToPutOn))
