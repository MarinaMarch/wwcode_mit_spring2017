# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:32:24 2017

@author: marina
"""
'''
You have a particular goal to be able to afford the down payment in three years.
This program calculates how much should you save each month to achieve this.

'''
semi_annual_raise = float(0.07)
r = float(0.04)
portion_down_payment = float(0.25)
total_cost = float(1000000)
total_months = int(36)
current_savings = float(0)
saving_rate = int(5000)
saving_rate_max = int(10000)
saving_rate_min = int(0)
steps = int(0)
annual_salary_input = float(input("Enter the starting salary: "))
total_savings = float(0)

downpayment = total_cost * portion_down_payment

for current_month in range(1, total_months + 1):
    annual_salary = annual_salary_input
    current_savings += (current_savings * r / 12) + (annual_salary / 12)
    if current_month % 6 == 0:
        annual_salary = annual_salary * (
        1 + semi_annual_raise)
    if (current_month == total_months):
        total_savings = current_savings

if total_savings < (downpayment - 100):
    print("It is not possible to pay the down payment in three years.")

else:
    while (current_savings < (downpayment - 100) or current_savings > (downpayment + 100)):
        current_savings = 0
        annual_salary = annual_salary_input

        for current_month in range(1, total_months + 1):
            current_savings += (current_savings * r / 12) + (annual_salary * (saving_rate / 10000) / 12)
            if current_month % 6 == 0:
                annual_salary = annual_salary * (1 + semi_annual_raise)

        if current_savings > (downpayment - 100) and current_savings < (
            downpayment + 100):
            steps += 1
            print("Best savings rate: ", saving_rate / 10000)
            print("Steps in bisection search: ", steps)
            break

        elif current_savings > downpayment:
            saving_rate_max = saving_rate
            saving_rate = int((saving_rate_max + saving_rate_min) / 2)
            steps += 1

        else:
            saving_rate_min = saving_rate
            saving_rate = int((saving_rate_max + saving_rate_min) / 2)
            steps += 1
