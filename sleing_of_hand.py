#!\usr\bin\env python 3
# -- coding: utf-8 --

#Функция считает количество совпадений t в матрице s, если совпадений меньше или кавно k*2
def slright_of_hand(k,s):
    ball = 0
    for t in range(10): 		#Время t (0,1...9)
        count = s.count(f'{t}')	#Сумма всех цифр в матрице равная t (количество клавиш которое нужно нажать)
        if count > 0:			#Если количество клвиш не равно 0
            if count <= k*2:	#И Если количество клавиш меньше или равно k*2, то условие выполняется,
                ball += 1 	    #подсчитываем баллы
    return (ball)

#Гоша и Тимофей могут нажать в один момент времени на k клавиш каждый
#(можно сделать проверку k (1 ≤ k ≤ 5) если нужно
k = 5
#ввод 
s1 = '1931'
s2 = '9..9'
s3 = '9..9'
s4 = '9..9'
s=s1+s2+s3+s4
#Из заданных условий не совсем понятно как вводить данные, можно ввести списком [[],[],[],[]] или как то по другому, но думаю это не принципиально
print ('\n','Ввод: \n',k,'\n',s1,'\n',s2,'\n',s3,'\n',s4)#Вывод вводимых данных (нужно или нет, х.з., но так выглядит лучше)
print ('\n Вывод: ', '\n', slright_of_hand(k,s))#Вывод количества баллов = решения задачи
#Возможно условия поняты не совсем верно    
