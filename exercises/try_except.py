# def div42by(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: You tried to divide by zero...that was dumb!')


# print(div42by(2))
# print(div42by(0))
# print(div42by(12))
# print(div42by(1))


print('How many catz? Youz have?')
numcatz = input()
try:
    if int(numcatz) >= 4:
        print('That is a lot of catz')
    else:
        print('That is not a lot of catz')
except ValueError:
    print('Ya shoulda typed something in?!')
