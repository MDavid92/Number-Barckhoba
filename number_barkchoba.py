import os
import sys

print("""Number Barkchoba
""")
print("""
Think of a whole integer between 1 and 100!
""")

numbers = list(range(1, 102))


def even_loop(numbers):
    for number in numbers:
        if number % 2 == 0:
            numbers.remove(number)
    return


def odd_loop(numbers):
    for number in numbers:
        if number % 2 != 0:
            numbers.remove(number)
    return


def odd_or_even():
    new_list1 = []
    ans1 = input("Is your number odd? y/n? ")
    if ans1 == "y":
        even_loop(numbers)
        new_list1 = numbers
    elif ans1 == "n":
        odd_loop(numbers)
        new_list1 = numbers
    return new_list1


def prime_number(numbers):
    lst1 = []
    for num in numbers[0:]:
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                lst1.append(num)
    return lst1


def qst_prime():
    ans2 = input("Did you think of a prime number? y/n")
    new_list1 = []
    if ans2 == "y":
        return pr_nmb
    elif ans2 == "n":
        for item in first_qst:
            if item not in pr_nmb:
                new_list1.append(item)
    return new_list1


def halving_up(second_qst):
    middle = int((len(second_qst) / 2))
    up_half = second_qst[middle:]
    return up_half


def halving_down(second_qst):
    middle = int((len(second_qst) / 2))
    down_half = second_qst[:middle]
    return down_half


def halving(second_qst):
    middle = int((len(second_qst) / 2))
    ans = input("Is your number greater than/equal to " + str(second_qst[middle]) + " ? y/n")
    if ans == "y":
        third_qst = halving_up(second_qst)
    elif ans == "n":
        third_qst = halving_down(second_qst)
    return list(third_qst)


def final_guess(B):
    final = halving(B)
    while len(final) > 3:
        final = halving(final)
    if len(final) <= 3:
        return final


def guesser(final):
    x = 1
    ans = input("is your number " + str(final[0]) + " ?")
    while ans == "n":
        ans = input("is your number " + str(final[x]) + " ?")
        x += 1
    if ans == "y":
        print("I've won!")
    else:
        print("Please answer with y or n!")
        guesser(final)


def anothergame():
    ans = input("Do you want to play again? y or n?")
    if ans == "y":
        os.startfile(sys.argv[0])
    elif ans == "n":
        sys.exit
    else:
        print("Please answer with a y or n !")
        anothergame()




first_qst = odd_or_even()
pr_nmb = prime_number(numbers)
second_qst = qst_prime()
c = halving_down(second_qst)
x = halving_up(second_qst)
B = halving(second_qst)
v = final_guess(B)
guesser(v)
anothergame()