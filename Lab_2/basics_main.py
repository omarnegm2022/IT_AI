from Basics import (
    length_conversion,
    tmpr_conversion                
    )

print(f"""{
    length_conversion.convert(
        float(input("Eneter your length in inches: ")))
        :.2f} \n
""",)

print(f"""{
    tmpr_conversion.convert(
        float(input("Enter the temprature in Celsius: "))
    )
}\n
""")
