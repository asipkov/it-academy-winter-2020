# 1. Напишите программу, которая считает общую цену. Вводится M рублей и N копеек цена,
# а также количество S товара Посчитайте общую цену в рублях и копейках за L товаров.
rubl = int(input('Введите стоимость в рублях: '))
cent = int(input('Введите стоимость в копейках: '))
count = int(input('Введите количество товаров: '))
all_rubl = rubl * count
all_cent = cent * count
ost_cent = all_cent % 100
integer_cent = all_cent // 100

"100 коппек конвертируется в 1 рубль в финальном результате"

if all_cent > 99:
    all_rubl = all_rubl + integer_cent

if all_cent > 99:
    print("Общая стоимость товаров " + str(all_rubl) + " руб " + str(ost_cent) + " центов")
else:
    print("Общая стоимость товаров " + str(all_rubl) + " руб " + str(all_cent) + " центов")