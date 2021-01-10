'use strict';
const cartItem = {
    render(product) {
        return `<div class="product">
                    <div><b>Наименование</b>: ${product.productName}</div>
                    <div><b>Цена за шт.</b>: ${product.productPrice}</div>
                    <div><b>Количество</b>: ${product.productQuantity}</div>
                    <div><b>Стоимость</b>: ${product.productQuantity * product.productPrice}</div>
                </div>`;
    }
}

const goods = {
    goodsItemCard: null,
    cartItem,
    buttonRefresh: null,
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

    buttonCreate() {
        let elem = null;
        elem = document.querySelectorAll(".product");
        elem.forEach(nodes => { nodes.remove() });
        this.init();

    },

    basketFill() {
        for (let i = 0; i < this.products.length; i++) {
            this.products[i].productQuantity = parseInt(Math.random(100) * 10);
        }
    },

    basketCost() {
        return this.products.reduce((totalCost, productItem) => totalCost += (productItem.productPrice * productItem.productQuantity), 0);
    },

    init() {
        this.basketFill();
        this.buttonRefresh = document.querySelector('.refresh');
        this.buttonRefresh.addEventListener('click', this.buttonCreate.bind(this));
        this.goodsItemCard = document.querySelector('.products-div');

        this.render();
    },

    render() {
        if (this.products.length) {
            this.products.forEach(product => {
                this.goodsItemCard.insertAdjacentHTML('beforeend', this.cartItem.render(product));
            });
            this.goodsItemCard.insertAdjacentHTML('afterend', `<div class="product">В корзине ${this.products.length} позиций(а) стоимостью ${this.basketCost()}</div>`);
        } else {
            this.goodsItemCard.textContent = 'Корзина пуста';
        }
    },

}

goods.init()
