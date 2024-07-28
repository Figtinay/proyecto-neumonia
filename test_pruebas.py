import csv
from tkinter import Tk
from tkinter.messagebox import showinfo
import unittest
import tensorflow as tf
from load_model import model_fun
from unittest.mock import patch, MagicMock


#def test_model_fun():
#    assert True is True

#def test_grad_cam():
#    assert True is True

class TestModelFun(unittest.TestCase):
    def test_model_load(self):
        model = model_fun()
        self.assertIsInstance(model, tf.keras.Model)

#if __name__ == '__main__':
#    unittest.main()
class SaveResultsCsv:
    def __init__(self, root):
        self.root = root
        self.text1 = MagicMock()
        self.label = "Etiqueta de prueba"
        self.proba = 0.75

    def save_results_csv(self):
        with open("historial.csv", "a") as csvfile:
            w = csv.writer(csvfile, delimiter="-")
            w.writerow(
                [self.text1.get(), self.label, "{:.2f}".format(self.proba) + "%"]
            )
            showinfo(title="Guardar", message="Los datos se guardaron con éxito.")
            
class TestSaveResultsCsv(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.text1 = MagicMock()
        self.text1.get.return_value = "Texto de prueba"
        self.label = "Etiqueta de prueba"
        self.proba = 0.75
        self.save_results_csv_method = SaveResultsCsv(self.root)

    @patch('builtins.open')
    def test_save_results_csv_error(self, mock_open):
        # Configuramos el mock para que devuelva un error
        mock_open.side_effect = IOError("Error al abrir el archivo")

        # Llamamos al método save_results_csv
        with self.assertRaises(IOError):
            self.save_results_csv_method.save_results_csv()

if __name__ == '__main__':
    unittest.main()