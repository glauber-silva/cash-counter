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
            "output: Notas necessarias para compor o valor de 134:",
            "2 notas de 50",
            "1 notas de 30",
            "4 notas de 1",
            "input: ",
            "output: Notas necessarias para compor o valor de 10:",
            "10 notas de 1",
            "input: "
        ], output)