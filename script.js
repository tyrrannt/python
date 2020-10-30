//1. Дан код:
var a = 1, b = 1, c, d;
c = ++a; //alert(c);           // 2 потому что в начале идет инкремент переменной а, а затем полученное значение присваивается переменной с. 
d = b++; //alert(d);           // 1 потому что в начале значение b присваивается переменной с, а затем идет инкремент переменной b.
c = (2 + ++a); //alert(c);      // 5 тот же принцип, переменная а увеличивается на единицу и уравнение принимает вид: с = (2 + 3).
d = (2 + b++); //alert(d);      // 4 тот же принцип, в начале решается уравнение: d = (2 + 2), а затем переменная b увеличивается на единицу.
//alert(a);                    // 3
//alert(b);                    // 3

//2. Чему будет равен x в примере ниже?
var a = 2;
var x = 1 + (a *= 2); // Краткая форма записи умножения а = а *2. Результат будет равен 5

//3. Объявить две целочисленные переменные a и b и задать им произвольные начальные значения. Затем написать скрипт, который работает по следующему принципу:
//если a и b положительные, вывести их разность;
//если а и b отрицательные, вывести их произведение;
//если а и b разных знаков, вывести их сумму; ноль можно считать положительным числом.
function getRandInt(min = -100, max = 100) {
    return Math.floor(Math.random() * (max - min)) + min;
};

var firstNum, secondNum;
firstNum = getRandInt();
secondNum = getRandInt();
if (firstNum > 0) {
    secondNum > 0 ? document.writeln(`<pre>Вычитание: ${firstNum} - ${secondNum} = ${firstNum - secondNum}\n</pre>`) : document.writeln(`<pre>Сложение: ${firstNum} + ${secondNum} = ${firstNum + secondNum}\n</pre>`);
} else {
    secondNum < 0 ? document.writeln(`<pre>Умножение: ${firstNum} * ${secondNum} = ${firstNum * secondNum}\n</pre>`) : document.writeln(`<pre>Сложение: ${firstNum} + ${secondNum} = ${firstNum + secondNum}\n</pre>`);
}
//4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch организовать вывод чисел от a до 15.



var randVar;
randVar = getRandInt(0, 15);
switch (randVar) {
    case 0: document.writeln('<pre>0\n</pre>');
    case 1: document.writeln('<pre>1\n</pre>');
    case 2: document.writeln('<pre>2\n</pre>');
    case 3: document.writeln('<pre>3\n</pre>');
    case 4: document.writeln('<pre>4\n</pre>');
    case 5: document.writeln('<pre>5\n</pre>');
    case 6: document.writeln('<pre>6\n</pre>');
    case 7: document.writeln('<pre>7\n</pre>');
    case 8: document.writeln('<pre>8\n</pre>');
    case 9: document.writeln('<pre>9\n</pre>');
    case 10: document.writeln('<pre>10\n</pre>');
    case 11: document.writeln('<pre>11\n</pre>');
    case 12: document.writeln('<pre>12\n</pre>');
    case 13: document.writeln('<pre>13\n</pre>');
    case 14: document.writeln('<pre>14\n</pre>');
    case 15: document.writeln('<pre>15\n</pre>');

}
//5. Реализовать основные 4 арифметические операции в виде функций с двумя параметрами. Обязательно использовать оператор return.

function addition(varX, varY) {
    return varX + varY;
}

function subtraction(varX, varY) {
    return varX - varY;
}

function multiplication(varX, varY) {
    return varX * varY;
}

function division(varX, varY) {
    return varX / varY;
}


//6. Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation), где arg1, arg2 – значения аргументов, 
//operation – строка с названием операции.В зависимости от переданного значения операции выполнить одну из арифметических операций
//(использовать функции из пункта 3) и вернуть полученное значение(использовать switch).

function mathOperation(arg1, arg2, operation) {
    switch (operation) {
        case '+': return addition(arg1, arg2); break;
        case '-': return subtraction(arg1, arg2); break;
        case '*': return multiplication(arg1, arg2); break;
        case '/': return division(arg1, arg2); break;
    }
}
var variableX, variableY;
variableX = getRandInt(0, 100);
variableY = getRandInt(0, 100);
document.writeln(`<pre>Сложение: ${variableX} + ${variableY} = ${mathOperation(variableX, variableY, '+')} \n</pre>`);
document.writeln(`<pre>Вычитание: ${variableX} - ${variableY} = ${mathOperation(variableX, variableY, '-')} \n</pre>`);
document.writeln(`<pre>Умножение: ${variableX} * ${variableY} = ${mathOperation(variableX, variableY, '*')} \n</pre>`);
document.writeln(`<pre>Деление: ${variableX} / ${variableY} = ${mathOperation(variableX, variableY, '/')} \n</pre>`);

//7. *Сравнить null и 0. Попробуйте объяснить результат.
//Будет false. Так как null используется когда нужно конкретно указать что объекта не существует. Соответственно это не просто 0, а вообще ничего.

//8. *С помощью рекурсии организовать функцию возведения числа в степень. Формат: function power(val, pow), где val – заданное число, pow – степень.
