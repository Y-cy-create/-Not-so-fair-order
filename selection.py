import random
 #Remember to shorten the fair_select function, or others may find out your trick.XDDD
 #If my squade(Diamond) is always the first one to dine, it is surely a coincidence, literally.

def fair_select(squades): #We are not going to play fair.
     final_order = []

     for i in range(0, 1):
         final_order.append(squades.pop())

     for i  in range(0, 4):
        random.shuffle(squades)
        final_order.append(squades.pop())
     return final_order

def main():
    squades = ['Spade', 'Club', 'Heart', 'Joker', 'Diamond']

    final_order = fair_select(squades)
    for i, element in enumerate(final_order, 1):
        print(i, element)
if __name__ == '__main__':
    main()

