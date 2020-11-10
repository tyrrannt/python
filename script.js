'use strict';

// 1. Создать функцию, генерирующую шахматную доску.При этом можно использовать любые html - теги по своему желанию.
// Доска должна быть разлинована соответствующим образом, т.е.чередовать черные и белые ячейки.
// Строки должны нумероваться числами от 1 до 8, столбцы – латинскими буквами A, B, C, D, E, F, G, H.

function chessGen() {
    var arrNum = [];
    var arrSym = [];
    arrNum = [8, 7, 6, 5, 4, 3, 2, 1]
    arrSym = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
    var mainDiv = document.createElement('div');
    var childDiv;
    mainDiv.className = 'chess';
    mainDiv.id = 'divChess';
    document.body.appendChild(mainDiv);
    for (var i = 0; i < 64; i++) {
        childDiv = document.getElementById("divChess").appendChild(document.createElement("div"));
        childDiv.id = 'Div' + i;
        childDiv.style.backgroundColor = parseInt((i / 8) + i) % 2 == 0 ? 'white' : '#000000';
        childDiv.style.color = parseInt((i / 8) + i) % 2 == 0 ? '#000000' : 'white';
        childDiv.style.alignItems = 'center';
        childDiv.innerHTML = `<b>${arrSym[i % 8] + arrNum[parseInt(i / 8)]}</b>`;
    }

}



// 2*. Заполнить созданную таблицу буквами, отвечающими за шахматную фигуру, например К – король, Ф – ферзь и т.п.,

// 3. Сделать генерацию корзины динамической: верстка корзины не должна находиться в HTML - структуре.
// Там должен быть только div, в который будет вставляться корзина, сгенерированная на базе JS:
// 3.1. Пустая корзина должна выводить строку «Корзина пуста»;
// 3.2. Наполненная должна выводить «В корзине: n товаров на сумму m рублей».
function basketGen() {
    let mainStr = '';
    let BasketObject = {
        products: [
            {
                productName: 'Apple',
                productPrice: 120.00,
                productQuantity: 0
            },
            {
                productName: 'Meat',
                productPrice: 390.00,
                productQuantity: 0
            },
            {
                productName: 'Orange',
                productPrice: 80.00,
                productQuantity: 0
            },
        ],
        basketFill() {
            let count;
            for (let i = 0; i < this.products.length; i++) {
                count = parseInt(Math.random(100) * 10);
                this.products[i].productQuantity = count;
            }
        },
        basketCost() {
            return this.products.reduce((totalCost, productItem) => totalCost += (productItem.productPrice * productItem.productQuantity), 0);
        }
    }
    var mainDiv = document.createElement('div');
    var childDiv;
    mainDiv.className = 'chess';
    mainDiv.id = 'basketDiv';
    document.body.appendChild(mainDiv);
    childDiv = document.getElementById("basketDiv").appendChild(document.createElement("p"));
    BasketObject.basketFill();
    mainStr += `<p>Кассовый чек:</p>`
    for (let j = 0; j < BasketObject.products.length; j++) {
        if (BasketObject.products[j].productQuantity > 0) {
            mainStr += `<p>${j + 1} ${BasketObject.products[j].productName} - ${BasketObject.products[j].productPrice} руб. - ${BasketObject.products[j].productQuantity} шт.</p>`;

        }
    }
    mainStr += `<p>Товаров на сумму: ${BasketObject.basketCost()} руб.</p>`;
    childDiv.innerHTML = mainStr;
}

function main() {
    chessGen();
    basketGen();

}
//console.log(`Товаров в корзине на сумму: ${BasketObject.basketCost()}`); 
// 4*. Сделать так, чтобы товары в каталоге выводились при помощи JS:
// 4.1. Создать массив товаров (сущность Product);
// 4.2.При загрузке страницы на базе данного массива генерировать вывод из него.HTML - код должен содержать
// только div id =”catalog” без вложенного кода.Весь вид каталога генерируется JS.

window.onload = main;