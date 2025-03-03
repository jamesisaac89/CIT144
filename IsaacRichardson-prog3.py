# Isaac Richardson

def read_sales_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    return [line.strip().split(',') for line in lines]

def calculate_customer_total(price, quantity):
    return price * quantity

def main():
    filename = 'makewaves.txt'
    sales_data = read_sales_data(filename)
    
    grand_total = 0.0
    
    print(f"{'Customer Name':<20} {'Item':<25} {'Price':<10} {'Quantity':<10} {'Total':<10}")
    print("-" * 75)
    
    for record in sales_data:
        customer_name = record[0]
        item = record[1]
        price = float(record[2])
        quantity = int(record[3])
        
        order_total = calculate_customer_total(price, quantity)
        grand_total += order_total
        
        print(f"{customer_name:<20} {item:<25} ${price:<9.2f} {quantity:<10} ${order_total:<9.2f}")

    print("-" * 75)
    print(f"{'Grand Total:':<75} ${grand_total:.2f}")

if __name__ == "__main__":
    main()
