print("1. 20 MB")
print("2. 30 MB")
print("3. 40 MB")

choice=int(input("Enter a selection : "))

print(type(choice))

if choice==1:
    print("You have purchased 20 MB worth of data")
elif choice==2:
        print("You have purchased 30 MB worth of data")
elif choice==3:
    print("You have purchased 40 MB worth of data")
else:
    print("Invalid choice !")

