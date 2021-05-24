alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  end_text = ""

  if direction == "decode":
    shift *= -1

  for letter in text:
    if letter in alphabet:
      index = alphabet.index(letter)
      index += shift

      if(index > 26):
        index = index % 26

      end_text += alphabet[index]
    else:
      end_text += letter

  print(f"Here's the {direction}d result: {end_text}")

should_end = False

while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text, shift, direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

  if restart == "no":
    should_end = True
    print("Goodbye")
