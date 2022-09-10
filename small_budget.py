# from getBudget import *

def main():
    endProgram = 'no'
    totalBudget = 0
    while endProgram == 'no':
        print('---Welcome to your Budget---')
        print("")
        print('Menu Selections: ')
        print('1-Add Income')
        print('2-Add an Expense')
        print('3-Check Budget Balance')
        print('4-Save progress-working on this feature')
        print('5-Load saved budget-working on this feature')
        print('6-Exit without saving')

        print("")
        choice = int(input('Enter your selection: '))
        if choice == 1:
            totalBudget = addIncome(totalBudget)
        elif choice == 2:
            totalBudget = addExpense(totalBudget)
        elif choice == 3:
            print("")
            print('Your Monthly budget balance is ${0}'.format(totalBudget))
        # elif choice == 4:
        #     saveBudget(totalBudget)
        #     print("")
        #     print('Saving your progress')
        # elif choice == 5:
        #     print("")
        #     loadBudget = input('Load your budget from file: ')
        #     loadBudget(totalBudget)
        #     print("")
        #     print("Your budget is loaded")
        elif choice == 6:
            endProgram = 'yes'
            print("")
            print('Goodbye')
        else:
            print("")
            print('Invalid selection, please try again')

def addIncome(totalBudget):
    print("")
    income = float(input('Enter new monthly income: $'))
    totalBudget = totalBudget + income
    print("")
    print('Your new Monthly budget is: ${0}'.format(totalBudget))
    return totalBudget

def addExpense(totalBudget):
    print("")
    expense = float(input('Enter your expense amount: $'))
    print("")
    timesPerMonth = int(input('How many times per month: '))
    totalExpense = expense * timesPerMonth
    if totalBudget - totalExpense >= 0:
        totalBudget = totalBudget - totalExpense
        print("")
        print ('The expenses was accepted, your remaining budget is: ${0}'.format(totalBudget))
        return totalBudget
    else:
        print("")
        print ('The expenses was rejected because the budget exceeded.')
        return totalBudget

main()