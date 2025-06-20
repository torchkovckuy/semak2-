from enum import Enum

class MathOperation(Enum):
    ADD = "+"
    SUBTRACT = "-"
    MULTIPLY = "*"
    DIVIDE = "/"

def calculate() -> tuple:
    try:
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        op = input("Выберите операцию (+, -, *, /): ").strip()

        operation = None
        for math_op in MathOperation:
            if math_op.value == op:
                operation = math_op
                break
        if not operation:
            raise ValueError("Недопустимая операция")
        match operation:
            case MathOperation.ADD:
                res = a + b
            case MathOperation.SUBTRACT:
                res = a - b
            case MathOperation.MULTIPLY:
                res = a * b
            case MathOperation.DIVIDE:
                res = a / b if b != 0 else float('nan')
        return (a, b, op, res)
    except ValueError as e:
        return (f"Ошибка: {e}",)


result = calculate()
print("Результат:", result)