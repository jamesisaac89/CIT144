
temperature = float(input("Enter a temperature value to convert: "))

conversion_type = input("Convert to Fahrenheit or Celsius? Enter F or C: ").strip().lower()

if conversion_type == 'f':
    
    converted_temperature = 1.8 * temperature + 32
    print(f"{temperature} degrees C = {converted_temperature:.1f} degrees F")
    
elif conversion_type == 'c':

    converted_temperature = (temperature - 32) / 1.8
    print(f"{temperature} degrees F = {converted_temperature:.1f} degrees C")
    
else:

    print("You did not enter an F or C. Goodbye")
