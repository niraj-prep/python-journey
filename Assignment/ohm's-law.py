# Ohm's Law Calculator

V = float(input("Enter Voltage (V): "))
R = float(input("Enter Resistance (Ohms): "))

I = V / R

print(f"\nCurrent (I) = {I:.4f} A")

if I < 0.5:
    print("Nature: Low current")
elif 0.5 <= I <= 2:
    print("Nature: Normal current")
else:
    print("Nature: High current")