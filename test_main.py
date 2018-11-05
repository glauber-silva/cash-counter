import main
import unittest

class TestCashCounter(unittest.TestCase):
    def test_main(self):
        """
        This will do a basic test with the examples of exercise
        """
        input_values = [50, 30, 1, -1, 134, 10, -1]
        output = []

        def mock_inputs(s):
            output.append(s)
            return input_values.pop(0)

        main.input = mock_inputs
        main.print = lambda s : output.append(s)

        main.main()

        self.assertEqual([
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "output: Notas necessarias para compor o valor de 134:",
            "2 notas de 50",
            "1 notas de 30",
            "4 notas de 1",
            "input: ",
            "output: Notas necessarias para compor o valor de 10:",
            "10 notas de 1",
            "input: "
        ], output)

    
    def test_when_invalid_cash(self):
        """
        This will test if a cash typed is valid
        """
        input_values = [50, 30, -10, 1, -1, 81, -1]
        output = []
        def mock_inputs(s):
            output.append(s)
            return input_values.pop(0)
        
        main.input = mock_inputs
        main.print = lambda s : output.append(s)
        main.main()

        self.assertEqual([
            "input: ",
            "input: ",
            "input: ",
            "output: invalido",
            "input: ",
            "input: ",
            "input: ",
            "output: Notas necessarias para compor o valor de 81:",
            "1 notas de 50",
            "1 notas de 30",
            "1 notas de 1",
            "input: ",
        ], output)

    def test_when_invalid_amount(self):
        """
        This will test if the total value is valid
        """
        input_values = [50, 10, 1, -1, 120, 20000, -1]
        output = []
        def mock_inputs(s):
            output.append(s)
            return input_values.pop(0)
        
        main.input = mock_inputs
        main.print = lambda s : output.append(s)
        main.main()

        self.assertEqual([
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "output: Notas necessarias para compor o valor de 120:",
            "2 notas de 50",
            "2 notas de 10",
            "input: ",
            "output: invalido",
            "input: "
        ], output)

    
    def test_two_out_three_cash(self):
        """
        This will test when use just 2 out 4 cash
        """
        input_values = [50, 30, 10, 1, -1, 120, -1]
        output = []
        def mock_inputs(s):
            output.append(s)
            return input_values.pop(0)
        
        main.input = mock_inputs
        main.print = lambda s : output.append(s)
        main.main()

        self.assertEqual([
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "output: Notas necessarias para compor o valor de 120:",
            "2 notas de 50",
            "2 notas de 10",
            "input: ",
        ], output)

    def test_when_amount_is_zero(self):
        """
        This will test when amount is zero
        """
        input_values = [50, 30, 10, 1, -1, 0, -1]
        output = []
        def mock_inputs(s):
            output.append(s)
            return input_values.pop(0)
        
        main.input = mock_inputs
        main.print = lambda s : output.append(s)
        main.main()

        self.assertEqual([
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "input: ",
            "output : nenhuma nota necessaria",
            "input: ",
        ], output)