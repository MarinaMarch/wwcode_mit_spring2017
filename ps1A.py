# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 09:08:14 2017

@author: marina
"""
def get_annual_salary ():
    instr = input("Enter your annual salary: ")
    if (len (instr) == 0):
        print ("Please, enter your annual salary. ")
        return None
    return float(instr)

def get_percent_of_salary ():
    instr = input("Enter the percent of your salary to save, as a decimal: ")
    if (len (instr) == 0):
        print ("Please, enter the percent of your salary to save, as a decimal. ")
        return None

    if float(instr) > 0.99 :
        print('please enter number from 0.1 to 0.99')
        return None
    elif float(instr) < 0.1:
        print ('It is should be at least 10%')
        return None

    return float(instr)

def get_cost_of_dream ():
    instr = input("Enter the cost of your dream home: ")
    if (len (instr) == 0):
        print ("Please, enter the cost of your dream home. ")
        return None
    return float(instr)

def calc_month_amount (portion_down_payment, portion_saved_percent, annual_salary, portion_saved, total_cost):
    months = 0
    current_savings = float(0)
    r = portion_saved_percent
    downpayment = total_cost * portion_down_payment
    while (current_savings < downpayment):
        current_savings = current_savings + (current_savings * r / 12) + (
        annual_salary / 12 * portion_saved)
        months += 1
    return months

def main ():
    portion_down_payment = 0.25
    portion_saved_percent = 0.04

    annual_salary = get_annual_salary ()
    while (annual_salary == None):
        annual_salary = get_annual_salary ()

    portion_saved = get_percent_of_salary ()
    while (portion_saved == None):
        portion_saved = get_percent_of_salary ()

    total_cost = get_cost_of_dream ()
    while (total_cost == None):
        total_cost = get_cost_of_dream ()

    month_amount = calc_month_amount (portion_down_payment, portion_saved_percent, annual_salary, portion_saved, total_cost)
    print("Number of months:", month_amount)

main ()


