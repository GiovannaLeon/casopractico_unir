import pytest
import unittest

from app.calc import Calculator


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_add_method_returns_correct_result1(self):
        self.assertEqual(6, self.calc.add(3, 3))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))      
        
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
  
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
    
    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertRaises(TypeError, self.calc.multiply, "0", 0)
        
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        self.assertEqual(1, self.calc.power(-1, 0))
        self.assertEqual(-27, self.calc.power(-3, 3))
        self.assertRaises(TypeError, self.calc.power, "0", 0)
        
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.substract(10, 6))
        self.assertEqual(-2, self.calc.substract(256, 258))
        self.assertEqual(-1, self.calc.substract(-1, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertEqual(0, self.calc.substract(0, 0))
        self.assertRaises(TypeError, self.calc.substract, "0", 0)

def test_multiply_method_returns_correct_result(self):
    # Verificar multiplicación de números positivos
    self.assertEqual(50, self.calc.multiply(10, 5))  # 10 * 5 = 50
    
    # Verificar multiplicación de números negativos
    self.assertEqual(-2560, self.calc.multiply(256, -10))  # 256 * -10 = -2560
    
    # Verificar multiplicación con cero
    self.assertEqual(0, self.calc.multiply(0, 5))  # 0 * 5 = 0
    self.assertEqual(0, self.calc.multiply(100, 0))  # 100 * 0 = 0
    self.assertEqual(0, self.calc.multiply(0, 0))  # 0 * 0 = 0

    # Verificar multiplicación con un número negativo y cero
    self.assertEqual(0, self.calc.multiply(0, -5))  # 0 * -5 = 0
    
    # Verificar que se lanza un error si los argumentos no son numéricos
    self.assertRaises(TypeError, self.calc.multiply, "a", 5)  # "a" * 5 debe lanzar TypeError
    self.assertRaises(TypeError, self.calc.multiply, 5, "b")  # 5 * "b" debe lanzar TypeError

def test_divide_method_returns_correct_result(self):
    # Verificar división de números positivos
    self.assertEqual(2, self.calc.divide(10, 5))  # 10 / 5 = 2
    
    # Verificar división de números negativos
    self.assertEqual(-25.6, self.calc.divide(256, -10))  # 256 / -10 = -25.6
    
    # Verificar división con resultado decimal
    self.assertEqual(5.0, self.calc.divide(10, 2))  # 10 / 2 = 5.0
    
    # Verificar división de número positivo por cero (debe lanzar un error)
    self.assertRaises(ZeroDivisionError, self.calc.divide, 10, 0)  # 10 / 0 debe lanzar ZeroDivisionError
    
    # Verificar división de cero por número (debe dar 0)
    self.assertEqual(0, self.calc.divide(0, 5))  # 0 / 5 = 0
    
    # Verificar que se lanza un error si los argumentos no son numéricos
    self.assertRaises(TypeError, self.calc.divide, "a", 5)  # "a" / 5 debe lanzar TypeError
    self.assertRaises(TypeError, self.calc.divide, 5, "b")  # 5 / "b" debe lanzar TypeError
if __name__ == "__main__":  # pragma: no cover
    unittest.main()
