# --- Define your functions below! ---
def introduction():
    print("Hello") 
def greeting():
    print("Good! I am Chatbot") 
def defaultresp():
    print("That's too bad :(")
def poem():
    print("I'm a computer. I'm a computery guy. Everything made out of buttons and wires. I'd like to show you, inside my digital life, inside my mind there is a digital mind.")
def vaild_resp(answer):
    the_list = ["bad", "horrible", "really bad", "not good"]
    good_list = ["good", "great", "wonderful"]
    if answer in the_list:
        print("I'm sorry")
    elif answer in good_list:
        print("Yay!")
# --- Put your main program below! ---
def main():
    introduction()
    while True:
        answer = input("(Do you like computers?)")
        if answer == "yes":
           greeting()
        elif answer == "no":
            defaultresp()
        answer = input("(Would you like to read a poem?)")
        if answer == "yes":
            poem()
        elif answer == "no":
            introduction()
        answer = input(("(How is you day going?)"))
        vaild_resp(answer)
        answer = input (("Would you like to say goodbye to Chatbot?"))
        if answer == "yes":
            print("goodbye!")
            quit()
        if answer == "no":
            introduction()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()