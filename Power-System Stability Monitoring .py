## Power-System Stability Monitoring 

This program checks the **frequency and voltage** of a power system and gives a basic stability status.

```
# Power-System Stability Monitoring

frequency = float(input("Enter System Frequency (Hz): "))
voltage = float(input("Enter System Voltage (V): "))

print("\n--- Power System Monitoring ---")
print("Frequency =", frequency, "Hz")
print("Voltage =", voltage, "V")

if frequency < 49 or frequency > 51:
    print("WARNING: Frequency is unstable!")

elif voltage < 210 or voltage > 250:
    print("WARNING: Voltage is unstable!")

else:
    print("Power System Status: STABLE")
```

### Example Output — Stable

```
Enter System Frequency (Hz): 50
Enter System Voltage (V): 230

--- Power System Monitoring ---
Frequency = 50.0 Hz
Voltage = 230.0 V
Power System Status: STABLE
```

### Example Output — Unstable

```
Enter System Frequency (Hz): 47
Enter System Voltage (V): 230

--- Power System Monitoring ---
Frequency = 47.0 Hz
Voltage = 230.0 V
WARNING: Frequency is unstable!
```

### Slightly Better Version

```
frequency = float(input("Enter Frequency (Hz): "))
voltage = float(input("Enter Voltage (V): "))

if 49 <= frequency <= 51 and 210 <= voltage <= 250:
    print("SYSTEM STABLE")
elif frequency < 49 or frequency > 51:
    print("SYSTEM UNSTABLE - Frequency Problem")
else:
    print("SYSTEM UNSTABLE - Voltage Problem")
```

**Project name:** Power-System Stability Monitoring System

**Parameters:** Frequency, voltage, and system stability.

**Note:** This is a simplified educational model. Actual power-system stability involves rotor-angle, transient, small-signal, and voltage-stability analysis.
