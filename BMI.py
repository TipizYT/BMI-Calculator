title = '''
██████╗░███╗░░░███╗██╗  ███████╗██╗███╗░░██╗██████╗░███████╗██████╗
██╔══██╗████╗░████║██║  ██╔════╝██║████╗░██║██╔══██╗██╔════╝██╔══██╗
██████╦╝██╔████╔██║██║  █████╗░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
██╔══██╗██║╚██╔╝██║██║  ██╔══╝░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██████╦╝██║░╚═╝░██║██║  ██║░░░░░██║██║░╚███║██████╔╝███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝ |______By Rovindu Thamuditha______|'''

print (title)
print ()
print ()
print ()
print ()
height = float (input ('Please enter your height in Meters: '))
print ()
print ()
print ()
weight = float (input ('Please enter your weight in Kilo Grams: '))
print ()
print ()
print ()
print ()
print ()
answer = weight / (height * height)
print (f'Your BMI is {answer}' )
print ()
print ()
print ()
if answer <= 18.4:
    print("You are underweight. Do not miss meals!!")
elif answer <= 24.9:
    print("Congratulations!!You are healthy.Keep it up")
elif answer <= 29.9:
    print("OOO...You are over weight.Do some exercise..")
elif answer <= 34.9:
    print("You are severely over weight. Do some diet")
elif answer <= 39.9:
    print("You are obese.Ohh Man!!")
else:
    print("You are severely obese.Stop eating fast food just now!!")

print()
print()
print("_______________________Thank You For Using My BMI Finder_______________________")
exitcode = input("Press Enter to exit: ")