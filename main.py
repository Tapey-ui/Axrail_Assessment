import csv

# calculate change and return total notes returned
def find_change(money, price):
    notes = [100, 50, 20, 10, 5, 1]

    # get total changes
    if money < price:
        print("Insufficient money inserted")
        return
    change = money - price
    print("Total change: RM " + str(change))
    note_count = 0

    # use for loop to iterate through notes list and get changes after iteration (change) and total notes returned (count)
    for note in notes:
        if change >= note:
            count = change // note
            change = change % note
            print(str(count) + " x RM " + str(note) + " notes")
            note_count += count
    return note_count

def main():
    drinks = {}

    # check if CSV file exists and has correct header and values
    try:
        with open('drinks.csv', mode='r') as file:
            csv_reader = csv.reader(file)

            # skip header line
            header = next(csv_reader)
            if header != "Drinks,Price".split(","):
                raise FileNotFoundError
            
            # save index and values in drink dict, return error if empty value in column/wrong amount of values
            for idx, row in enumerate(csv_reader, start=1):
                if len(row) != 2 or row[0] == '' or row[1] == '':
                    raise ValueError
                drinks[idx] = row
            print("Welcome to ABC Vending Machine. Please select an item:")
            for idx, row in drinks.items():
                print(str(idx) + '. ' + row[0] + " - RM " + row[1])
    except FileNotFoundError:
        print("Error: File error. Please check that file exists and is in correct format")
        return
    except ValueError:
        print("Error: Value Error. Please check that file contains required values")
        return
    
    # get index of order, throw error if order is not correct
    try:
        index = int(input("Order: "))
        if index not in drinks:
            raise ValueError
    except ValueError:
        print("Item not found. Please enter a valid selection based on index")
        return
    
    print("SELECTED: " + drinks[index][0])
    print("PRICE: RM " + drinks[index][1])

    # get input money, throw error if money is not in int form
    try:
        money = int(input("Please insert cash (notes only): "))
        if (money <= 0):
            raise ValueError
    except ValueError:
        print("Please enter only notes (no coins)")
        return
    
    print("Total notes returned: " + str(find_change(money, int(drinks[index][1]))))
    print("Thank you for your purchase! :)")


if __name__ == "__main__":
    main()