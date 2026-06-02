from tabulate import tabulate


class Converter:

    def c_to_f(self, c):
        return (c * 9/5) + 32

    def c_to_k(self, c):
        return c + 273.15

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def f_to_k(self, f):
        return (f - 32) * 5/9 + 273.15

    def k_to_c(self, k):
        return k - 273.15

    def k_to_f(self, k):
        return (k - 273.15) * 9/5 + 32


converter = Converter()

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter Choice: "))
temp = float(input("Enter Temperature: "))

if choice == 1:
    result = converter.c_to_f(temp)
    conversion = "C → F"

elif choice == 2:
    result = converter.c_to_k(temp)
    conversion = "C → K"

elif choice == 3:
    result = converter.f_to_c(temp)
    conversion = "F → C"

elif choice == 4:
    result = converter.f_to_k(temp)
    conversion = "F → K"

elif choice == 5:
    result = converter.k_to_c(temp)
    conversion = "K → C"

elif choice == 6:
    result = converter.k_to_f(temp)
    conversion = "K → F"

else:
    print("Invalid Choice")
    exit()

table = [
    [conversion, f"{temp:.2f}", f"{result:.2f}"]
]

print(tabulate(
    table,
    headers=["Conversion", "Input", "Output"],
    tablefmt="grid"
))