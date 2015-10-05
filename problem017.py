letters = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety','hundred','and']
summa = 0

for i in range(1,1000):
    if i % 100 < 20:
        summa += len(letters[i % 100])
    else:
        summa += len(letters[i % 10])
        summa += len(letters[(i % 100) // 10 + 18])
    if i >= 100:
        if i % 100 != 0:
            summa += len(letters[-1])
        summa += len(letters[-2])
        summa += len(letters[i // 100])


print summa + len('onethousand')

