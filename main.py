import csv

def find_change(money, price):
    if money < price:
        print("Insufficient money inserted")
        return
    change = money - price
    print("Total change: RM " + str(change))
    notes = [100, 50, 20, 10, 5, 1]
    note_count = 0
    for note in notes:
        if change >= note:
            count = change // note
            change = change % note
            print(str(count) + " x RM " + str(note) + " notes")
            note_count += count
    return note_count

def main():
    drinks = {}
    try:
        with open('drinks.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            if header != "Drinks,Price".split(","):
                raise FileNotFoundError
            print("Welcome to ABC Vending Machine. Please select an item:")
            for idx, row in enumerate(csv_reader, start=1):
                print(str(idx) + '. ' + row[0] + " - RM " + row[1])
                drinks[idx] = row
    except FileNotFoundError:
        print("Error: File error. Please check that file exists and is in correct format")
        return
    try:
        index = int(input("Order: "))
        if index not in drinks:
            raise ValueError
    except ValueError:
        print("Item not found. Please enter a valid selection based on index")
        return
    print("SELECTED: " + drinks[index][0])
    print("PRICE: RM " + drinks[index][1])
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