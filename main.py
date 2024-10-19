import random


def customers_in_one_day():
    probabilities = [0.35, 0.30, 0.25, 0.10]
    customers = [8, 10, 12, 14]
    return random.choices(customers, probabilities)[0]


def amount_a_customer_wants_to_buy():
    probabilities = [0.40, 0.30, 0.20, 0.10]
    dozens = [1, 2, 3, 4]
    return random.choices(dozens, probabilities)[0]


def total_amount_customers_want_to_buy_today(customers_in_one_day):
    total = 0
    for i in range(customers_in_one_day):
        total += amount_a_customer_wants_to_buy()
    return total


def main():
    sim_count = 100000

    for donuts_made in range(5, 51, 5):
        total_income = 0
        total_customers = 0
        total_customers_unable_to_buy = 0

        for i in range(sim_count):
            for day in range(5):
                customers_today = customers_in_one_day()
                remaining_donuts_today = donuts_made

                there_is_customers_unable_to_buy = False
                for i in range(customers_today):
                    amount = amount_a_customer_wants_to_buy()

                    if remaining_donuts_today < amount:
                        there_is_customers_unable_to_buy = True
                        break
                    else:
                        remaining_donuts_today -= amount
                
                donuts_sold_today = donuts_made - remaining_donuts_today

                production_cost_today = donuts_made * 55
                revenue_today = donuts_sold_today*80 + remaining_donuts_today*40
                income_today = revenue_today - production_cost_today
                total_income += income_today

                total_customers += customers_today
                if there_is_customers_unable_to_buy:
                    total_customers_unable_to_buy += (customers_today - i)
        
        print('Donuts made per day:', donuts_made)
        print('Average total income for five days:', total_income/sim_count)
        print('Average total customers that are unable to buy donuts for five days:', total_customers_unable_to_buy/total_customers)
        print()

    return


if __name__ == '__main__':
    main()
