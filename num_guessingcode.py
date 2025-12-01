print("Testing program...")

attempt += 5

secret = 50
print("Secret =", secret)   # This will show the value of secret

guess = int(input("Enter your guess: "))

if guess == secret:
    print("MATCH ✓")
else:
    print("NO MATCH ✗")
