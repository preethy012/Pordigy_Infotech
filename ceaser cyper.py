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







alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
choice=input("Type your choice 'encode' or 'decode'")
message=input("Type your message").lower()
shift=int(input("how many number to shift"))
encode(original_message=message,shift_number=shift)
should_continue=input("Type 'yes' to continue 'no' to exit")
should_continue==True
should_continue


