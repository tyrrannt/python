'use strict';
// // 1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999, мы должны получить на выходе объект,
// в котором в соответствующих свойствах описаны единицы, десятки и сотни. Например, для числа 245 мы должны получить следующий объект: 
// {‘единицы’: 5, ‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо выдать соответствующее сообщение с помощью console.log 
// и вернуть пустой объект.
function createObj(count) {
    let result = {
        единицы: 0,
        десятки: 0,
        сотни: 0,
    };
    if (count > 999) {
        console.log('Achtung! Число превышает допустимое значение!');
        return result;
    }

    result.единицы = count % 10;
    result.десятки = (count / 10 | 0) % 10
    result.сотни = (count / 100 | 0) % 10
    return result;
}

let userInput = 0;
let userObj;

userInput = prompt('Введите число от 0 до 999: ');
userObj = createObj(userInput);
alert(`{‘единицы’: ${userObj.единицы}, ‘десятки’: ${userObj.десятки}, ‘сотни’: ${userObj.сотни}}`)

// // 2. Для игры, реализованной на уроке, добавить возможность вывода хода номер n (номер задается пользователем)

// // 3.Продолжить работу с интернет-магазином:

// // 3.1. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими объектами можно заменить их элементы?

// // 3.2. Реализуйте такие объекты.
let BasketObject = {
    products: [
        {
            productName: 'Apple',
            productPrice: 120.00,
            productQuantity: 10
        },
        {
            productName: 'Meat',
            productPrice: 390.00,
            productQuantity: 5
        },
        {
            productName: 'Orange',
            productPrice: 80.00,
            productQuantity: 2
        },
    ],
    // // 3.3. Перенести функционал подсчета корзины на объектно-ориентированную базу.
    basketCost() {
        return this.products.reduce((totalCost, productItem) => totalCost += (productItem.productPrice * productItem.productQuantity), 0);
    }
}

console.log(`Товаров в корзине на сумму: ${BasketObject.basketCost()}`);