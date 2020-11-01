//1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
var i = 2;
var simpleValue = new Array();
simpleValue[0] = 1;
let countItem = 0;
while (i <= 100) {
    let count = 0;
    for (let j = 0; j < simpleValue.length; j++) {

        if ((i % simpleValue[j]) == 0) {
            count += 1;
        }

    }
    if (count == 1) {
        simpleValue[++countItem] = i;
    }
    count = 0
    ++i;
}
for (let i = 0; i < simpleValue.length; i++) {
    console.log(i + 1, simpleValue[i]);
}

//2. С этого урока начинаем работать с функционалом интернет-магазина. Предположим, есть сущность корзины.
//Нужно реализовать функционал подсчета стоимости корзины в зависимости от находящихся в ней товаров. 
//Товары в корзине хранятся в массиве. Задачи:
//a) Организовать такой массив для хранения товаров в корзине;
let basketArray = new Array();
basketArray[0] = ['Apple', 120.00, 10];
basketArray[1] = ['Meat', 390.00, 5];
basketArray[2] = ['Orange', 80.00, 2];

//b) Организовать функцию countBasketPrice, которая будет считать стоимость корзины.
function countBasketPrice(arr) {
    summBasket = 0;
    for (let count = 0; count < arr.length; count++) {
        summBasket += arr[count][1] * arr[count][2];
    }
    return summBasket
}
console.log(`Товаров в корзине на сумму: ${countBasketPrice(basketArray)}`)
//3.*Вывести с помощью цикла for числа от 0 до 9, не используя тело цикла. Выглядеть это должно так:
//for(…){// здесь пусто}

for (let countItems = 0; countItems <= 9; countItems++, console.log(countItems - 1)) { }
// 4. *Нарисовать пирамиду с помощью console.log, как показано на рисунке, только у вашей пирамиды должно быть 20 рядов, а не 5:
// x
// xx
// xxx
// xxxx
// xxxxx
i = 1;
let consoleString = '';
while (i <= 20) {
    consoleString += 'x';
    console.log(consoleString)
    i++;
}