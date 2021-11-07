# Define functions
def CelToFahCon():
	celsiusInput = float(input("Enter the temperature in Celsius to convert to Fahrenheit: "))
	Fahrenheit = (celsiusInput * 9/5) + 32
	print(str(celsiusInput) + " degrees Celsius is equivalent to " + str(Fahrenheit) + " degrees Fahrenheit.")
def FahToCelCon():
	fahrenheitInput = float(input("Enter the temperature in Fahrenheit to convert to Celsius: "))
	Celsius = (fahrenheitInput - 32) * 5/9
	print(str(fahrenheitInput) + " degrees Fahrenheit is equivalent to " + str(Celsius) + " degrees Celsius.")

# Output conversion options to the user. 
Welcome = "Welcome to MeasurementConverter!\n" + "Enter the corresponding number to select what you want to convert:"
CelToFah = "1 - Celsius to Fahrenheit"
FahToCel = "2 - Fahrenheit to Celsius"
WelcomeStatement = Welcome + "\n" + CelToFah + "\n" + FahToCel
print(WelcomeStatement)

# Get selection from user
userSelect = int(input("Enter your selection: "))
print(userSelect)

# Output corresponding function to user input
if userSelect  == 1:
	CelToFahCon()
elif userSelect == 2: 
	FahToCelCon()
else:
	print("That is not a valid selection.")