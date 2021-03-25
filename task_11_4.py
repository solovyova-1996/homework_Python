# __author__Соловьева Дарья Викторовна
# 4. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real, self.imag * other.imag)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f'{complex(f"{self.real}{self.imag}j")}'


complex_number1 = ComplexNumber(3, 2)
complex_number2 = ComplexNumber(4, -9)
print(complex_number1 + complex_number2)
print(complex_number2 - complex_number1)
print(complex_number1 * complex_number2)
