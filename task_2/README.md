# Робота з алгеброю на еліптичних кривих

## Використані технології

В ході виконання завдання було використано функціонал *Python3.9*, а також вбудовані модулі *random* та *math*.
Використано клас із модульною аріфметикою **ModArith** (модуль *ModArith.py*).
Розроблено клас із структурою **ECPoint** (модуль *ECPoint.py*) для опису координат точки.
Розроблено клас **ECurve** (модуль *ECurve.py*) для роботи із алгеброю на еліптичних кривих.


## Виконання завдання

1. *func BasePointGGet() (point ECPoint)* - реалізовано метод *ECurve.BasePointGGet()* для отримання об'єкту точки *ECPoint*.

2. *func ECPointGen(x, y \*big.Int) (point ECPoint) {}* - реалізовано метод *ECurve.ECPointGen()* для створення об'єкту точки *ECPoint* за заданими координатами.

3. *func IsOnCurveCheck(a ECPoint) (c bool) {}* - реалізовано метод *ECurve.IsOnCurveCheck()* для перевірки чи точка *ECPoint* лежить на еліптичній кривій.

4. *func AddECPoints(a, b ECPoint) (c ECPoint) {}* - реалізовано метод *ECurve.AddECPoints()* для отримання суми двох точок *ECPoint*.

5. *func DoubleECPoints(a ECPoint) (c ECPoint) {}* - реалізовано метод *ECurve.DoubleECPoints()* для подвоєння точки *ECPoint*.

6. *func ScalarMult(a ECPoint, k big.Int) (c ECPoint) {}* - реалізовано метод *ECurve.ScalarMult()* для множення точки *ECPoint* на заданий коефіцієнт.

7. *func ECPointToString(point ECPoint) (s string) {}* - реалізовано метод *ECurve.ECPointToString()* для конвертування координат точки *ECPoint* у стрічку.

8. *func PrintECPoint(point ECPoint) {}* - реалізовано метод *ECurve.PrintECPoint()* для друку координат точки *ECPoint*.


## Запуск тестування

Перевірити роботу створенного модулю можливо за допомогою файлу *test.py* - в консолі треба виконати наступні команди:

- `cd <шлях до папки з проектом>`
- `python3 ./test.py`

Після виконання програми консоль має містити результати тестування по пунктах завдання.
