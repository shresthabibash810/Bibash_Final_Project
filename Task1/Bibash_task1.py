#making function to find the price of pizza after the given discount
def calculator_pizza(no_of_pizza, delivery_cost, on_tuesday, used_app):
    pizza_price = 12
    total_price = pizza_price * no_of_pizza
    if on_tuesday:
        total_price = 0.5 * total_price

    if delivery_cost and no_of_pizza <= 5:
        total_price = 2.5 + total_price

    if used_app:
        total_price = 0.75 * total_price

    return total_price

print("BPP Pizza Price Calculator")
print("===========================")

#checking no_of_pizza is whether positive or not and also integer or not
while True:
    try:
        no_of_pizza = int(input("How many pizzas ordered? "))
        if no_of_pizza <= 0:
            print("Please enter a positive number")
        else:    
            break
    except:
        print("PLease enter a number")

#making function to check yes or no
def get_yes_or_no(message):
    while True:
        answer = input(message).lower()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False
        else:
            print('Please answer "Y" or "N".')

#calling function in their resepctive variables
delivery_cost= get_yes_or_no("Is delivery required? (Y/N) ")
on_tuesday = get_yes_or_no("Is it Tuesday? (Y/N) ")
used_app = get_yes_or_no("Did the customer use the app? (Y/N) ")



total_price = calculator_pizza(no_of_pizza, delivery_cost, on_tuesday, used_app)

print(f"Total Price: £{total_price:.2f}")





