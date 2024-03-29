def calculate_discount(price, discount_percent):
    price = float(price)
    discount_percent = float(discount_percent)/ 100

    # Checks if discount is higher that 20%
    if(discount_percent >= 0.2):
        discount_amount = price * discount_percent
        final_price = price - discount_amount
        return final_price
    else:
        return price

input_price= input('Please  enter the original price: ')
input_discount = input('Please  enter the discount percent: ')

print('The final price is: ', calculate_discount(input_price, input_discount))