from art import logo
def encode(original_message,shift_number):
    ciper=""
    if choice=="encode":
      for i in original_message:
        shift_postion=alphabets.index(i) + shift_number
        shift_postion%=len(alphabets)
        ciper+=alphabets[shift_postion]

    elif choice=="decode":
        for i in original_message:
            shift_postion = alphabets.index(i) - shift_number
            shift_postion %= len(alphabets)
            ciper += alphabets[shift_postion]
    print(f"The encoded message: {ciper}")
print(logo)
should_continue=True
while should_continue:
    alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    choice=input("Type your choice 'encode' or 'decode': ")
    if choice not in["encode","decode"]:
        print("Invalid input please give a valid input")
        continue

    message=input("Type your message: ").lower()
    shift=int(input("How many number to shift: "))
    encode(original_message=message,shift_number=shift)
    restart=input("Type 'yes' to continue 'no' to exit: ").lower()
    if restart=="no":
        should_continue=False
        print("good bye")

