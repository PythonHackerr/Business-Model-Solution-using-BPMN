import random
import numpy as np
import math

vegetables = ['Ziemniaki', 'Kapusta', 'Buraki', 'Marchew']

skleps = ['UKermita', 'UAktora', 'UKarolci', 'Krzesak', 'Stoisko', 'VegitoWarzywa', 'UCHLOPAKOW', 'UPanaWojtka', 'DobryWarzywniak', 'ArabicGroceryShop']

total_produced = {'Ziemniaki' : 1170, 'Kapusta' : 670, 'Buraki' : 730, 'Marchew' : 760}

pojemnosci_magazynow = {'Pruszkow' : 800, 'Zielonka' : 1200, 'Piaseczno' : 750}

vegetable_wanted_factor = {'Ziemniaki' : 1.7, 'Kapusta' : 1, 'Buraki' : 1.1, 'Marchew' : 1.2}

pojemnosci_sklepow = {
  'UKermita' : 87.6, 
  'UAktora' : 7.5, 
  'UKarolci' : 14, 
  'Krzesak' : 15,
  'Stoisko' : 7, 
  'VegitoWarzywa' : 10, 
  'UCHLOPAKOW' : 9, 
  'UPanaWojtka' : 8, 
  'DobryWarzywniak' : 7, 
  'ArabicGroceryShop' : 8.2
}



avr_costumers_sklepow = {
  'UKermita' : 900,
  'UAktora' : 1150, 
  'UKarolci' : 2250, 
  'Krzesak' : 1900, 
  'Stoisko' : 1300, 
  'VegitoWarzywa' : 1650, 
  'UCHLOPAKOW' : 1350, 
  'UPanaWojtka' : 1575, 
  'DobryWarzywniak' : 1250, 
  'ArabicGroceryShop' : 1550
}


iii = 0
zapasy_sklepow = {
  'UKermita' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'UAktora' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'UKarolci' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'Krzesak' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'Stoisko' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'VegitoWarzywa' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'UCHLOPAKOW' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'UPanaWojtka' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'DobryWarzywniak' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}, 
  'ArabicGroceryShop' : {'Ziemniaki': 0, 'Kapusta':0, 'Buraki':0, 'Marchew':0}
}


def refuel_zapasy(sklep):
    for vegetable in vegetables:
        reducer = (pojemnosci_sklepow[sklep] * (vegetable_wanted_factor[vegetable] / 5) - zapasy_sklepow[sklep][vegetable])
        if (total_produced[vegetable] - reducer < 0):
            zapasy_sklepow[sklep][vegetable] += total_produced[vegetable]
            total_produced[vegetable] = 0
            print("\n\n\n HOLLY SHIT :( \n\n\n")
        else:
            zapasy_sklepow[sklep][vegetable] += reducer
            total_produced[vegetable] -= reducer


def generate_weekly_sales(week, sklep):
    refuel_zapasy(sklep);

    week_sales = {'Ziemniaki': 0, 'Kapusta': 0, 'Buraki': 0, 'Marchew': 0}
    customers_num = math.floor(max(avr_costumers_sklepow[sklep] / 2, np.random.normal(loc = avr_costumers_sklepow[sklep], scale=250)))
    # customers_num *= 1 + (summer_amplitude * math.sin((week / 13) * (2 * math.pi / (summer_end_week - summer_start_week + 1))))
    # in the peek season there is 1.5 as many costumers as in the low season
    customers_num *= (1 + (((1 + math.sin((((week - 26) * 2) / 52) * math.pi)) / 4))) / 1.25

    customers_num = int(customers_num)
    for i in range(customers_num):
        penalty = 0
        for vegetable in vegetables:
            vegetable_sale = (max(0, np.random.normal(loc = .5+penalty, scale=.75)) / 1000) * vegetable_wanted_factor[vegetable]

            # in the peek season there is 1.5 as many given type of vegetables sold as in the low season. If for ex potatos are at its peek season, 
            # everything else is at it's low or neither. Hope it makes sense. Trust me it works!
            vegetable_sale *= (1 + (((1 + math.sin(((vegetables.index(vegetable) - 1.5) / 1.5) * math.pi)) / 4))) / 1.25
            
            if (zapasy_sklepow[sklep][vegetable] - vegetable_sale < pojemnosci_sklepow[sklep] / 15):
                penalty += 0.1
                continue
            week_sales[vegetable] += vegetable_sale
            zapasy_sklepow[sklep][vegetable] -= vegetable_sale
    return week_sales


total_sales = {}
holly_var = []

bruh = False
file = open("file.txt", "w")
for sklep in skleps:
    bruh = True
    holly_var.append([])
    #print(f"\n---- Prognozowana sprzedaż warzyw w sklepie {sklep} ----\n ")
    yearly_sales = {}
    print("-------------------------")
    for week in range(52):
        sales = generate_weekly_sales(week, sklep)
        # print(f"sales in {i+1} week: {sales}")
        keys_arr = list(sales.keys())
        values_arr = list(sales.values())


        #if (bruh == True):
        for veg in vegetables:
            #print(f"{i} {veg} {sklep}    {round(sales[veg], 5)}")
            file.write(f"{week+1} {veg} {sklep}    {round(sales[veg], 5)}\n")
            #print(f"{sklep} {i}      {round(sales['Ziemniaki'], 5)}  {round(sales['Kapusta'], 5)}  {round(sales['Buraki'], 5)}  {round(sales['Marchew'], 5)}")
        #bruh = False
        #else:
            #print(f"        {i}      {round(sales['Ziemniaki'], 5)}  {round(sales['Kapusta'], 5)}  {round(sales['Buraki'], 5)}  {round(sales['Marchew'], 5)}")
        iii += 1

        for key, value in sales.items():
            if key in yearly_sales:
                yearly_sales[key] += value 
            else:
                yearly_sales[key] = value

    for key, value in yearly_sales.items():
        if key in total_sales:
            total_sales[key] += value
        else:
            total_sales[key] = value
    print("-------------------------")
    #print(f"Yearly sales for shop {sklep} is: {yearly_sales}")

print(f"\n\nTotal sales in a year is: {total_sales}")
print(f"\nTotal sales in a year (all vegetables) is: {sum(total_sales.values())}") # must be less than 2750 and 3330
print(f"\nZostalo warzyw: {total_produced}")
#print(f"\nZapasy sklepow: {zapasy_sklepow}")