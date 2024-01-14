from pint import UnitRegistry

def convert_temperature(value, input_scale, output_scale):
    ureg = UnitRegistry()
    input_temp = value * ureg(input_scale)
    output_temp = input_temp.to(output_scale)
    return output_temp.magnitude

choice = int(input("Enter the temperature value:  "))
initial = str(input("Enter the initial scale:  "))
final = str(input("Enter the final scale:  "))
result = convert_temperature(choice, initial, final)
print(result)  
