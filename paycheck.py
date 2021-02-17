# We need two inputs from the user, their income and marital status MS(marital Status) IN(income)
MS = str(input("Type S if single or M if married\n"))
IN = float(input("\nPlease enter your salary\n$"))
# these are variables that well use for grosspay (GP) deductions (DE) and final Paycheck(FP)
GP = float(IN/26)
DE = 0
FP = 0
# Now I'm using the if/else to separate married from single
if MS == "S":
#You are good at math so this should be pretty self explanatory
    if IN <= 100000:
        DE = float(((IN*.05)+800)/26)
        FP = GP-DE
    elif IN <= 500000:
        DE = float((((IN-100000)*.105)+5000+800)/26)
        FP = GP-DE
    elif IN > 500000:
        DE = float((((IN-500000)*.2025)+47000+800)/26)
        FP = GP-DE
#Same thing with the married tax rates and insurance swapped
elif MS == "M":
    if IN <= 250000:
        DE = float(((IN*.0625)+1000)/26)
        FP = GP-DE
    elif IN <= 900000:
        DE = float((((IN-250000)*.1075)+1562.50+1000)/26)
        FP = GP-DE
    elif IN > 900000:
        DE = float((((IN-900000)*.225)+8550+1000)/26)
        FP = GP-DE
# Let's show what we've got from our calculations
print("\nFor this pay period:\n   The grosspay is $"+ str(round(GP,2))+"\n   Total dedcutions are $"+str(round(DE,2))+"\n   The payment is $"+ str(round(FP,2)) )
