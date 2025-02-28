import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    d = float(sys.argv[4])
    e = float(sys.argv[5])

    values = [a,b,c,d,e]

    if any(x < 0 for x in values):
        print("<p>Warning: Some values are negative.</p>")
        
    avg = sum(values)/len(values)

    if avg > 50:
        avg_msg = f"<p>Average value is over 50. Value is: {avg}</p>"
    else: 
        avg_msg = f"<p>Average value is equal or above 50. Value is: {avg}</p>"

    count = len([x for x in values if x > 0])
    if count & 1:
        bitwise = f"<p>The count of positive numbers is odd. Value is: {count}</p>"
    else:
        bitwise = f"<p>The count of positive numbers is even. Value is: {count}</p>"

    
    new_values = sorted([x for x in values if x > 10])

    print(avg_msg)
    print(bitwise)
    print(f"<p>Sorted numbers greater than 10: {new_values}</p>")
    
    
except ValueError:
    print("<h3>Error: Invalid input. Please enter a valid number.</h3>")
