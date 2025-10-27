#Hi were going to create CREATE A TEXT SUMMARIZER
from summarizer import summarize


print("welcome to TEXT SUMMARIZER!!")

while True:
    text_input=input("Enter you text to be summarized : \n")
    print('Choose your summary size:')
    print("1-small")
    print("2-medium")
    print("3-large")
    choice=input("Enter your choice :")


    if not choice.isdigit():
        print("Please choose between given option")
        continue
    choice=int(choice)
    if choice not in [1,2,3]:
        print("Please choose between given option")
        continue
    

    print("Generating your summary..")
    summary=summarize(text_input,choice)

    print("Here is your summary \n ")
    print(summary )

    signal=input('\n if you want stop, Type stop,exit,quit or press enter to continue \n')
    if signal.lower() in ["stop","exit","quit"]:
        print("Thank you and bye")
        break


