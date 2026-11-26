"""
CP1404/CP5632 Practical
Hexadecimal Colour Lookup
"""

COLOUR_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "black": "#000000",
    "blue": "#0000ff",
    "coral": "#ff7f50",
    "darkgreen": "#006400",
    "gold": "#ffd700",
    "hotpink": "#ff69b4",
    "indigo": "#4b0082",
    "white": "#ffffff"
}

colour_name = input("Enter a colour name (or blank to quit): ").strip().lower()

while colour_name != "":
    hex_code = COLOUR_TO_HEX.get(colour_name)
    if hex_code:
        print(f"The hex code for {colour_name} is {hex_code}")
    else:
        print(f"Invalid colour name: {colour_name}")

    colour_name = input("Enter a colour name (or blank to quit): ").strip().lower()

print("Goodbye!")