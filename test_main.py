import main
import unittest

class TestCashCounter(unittest.TestCase):
    def test_main(self):
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
            "output: Notas necessarias para compor o valor de 134: \n"
            "2 notas de 50 \n"
            "1 nota de 30 \n"
            "4 notas de 1",
            "input: ",
            "output: Notas necessarias para compor o valor de 10: \n"
            "2 notas de 50 \n"
            "1 nota de 30 \n"
            "4 notas de 1",
            "input: "
        ], output)