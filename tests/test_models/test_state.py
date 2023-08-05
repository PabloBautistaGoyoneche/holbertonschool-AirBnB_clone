#!/usr/bin/python3
"""We test te class State and all its functions"""
import unittest
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):

    def setUp(self):
        # Reiniciar el almacenamiento para cada prueba
        FileStorage.__objects = {}

    def test_instantiate(self):
        state = State()
        self.assertEqual(State, type(state))

    def test_attr_name(self):
        state = State()
        self.assertEqual(str, type(state.name))

    def test_cities_attribute(self):
        state = State()
        self.assertTrue(hasattr(state, "cities"))
        self.assertEqual(list, type(state.cities))
        self.assertEqual(0, len(state.cities))

    def test_add_city_to_state(self):
        state = State()
        city = City()
        state.cities.append(city)
        self.assertEqual(1, len(state.cities))
        self.assertIn(city, state.cities)

    def test_delete_method(self):
        state = State()
        state_id = state.id
        state_name = state.name
        state.save()

        # Verificar que el estado esté almacenado en el diccionario
        self.assertIn(state_id, FileStorage.__objects)
        self.assertIs(FileStorage.__objects[state_id], state)

        # Eliminar el estado y verificar que ya no esté en el diccionario
        state.delete()
        self.assertNotIn(state_id, FileStorage.__objects)

    def test_to_dict_method(self):
        state = State()
        state.name = "California"
        state_dict = state.to_dict()

        # Verificar que se haya agregado la clave 'name' al diccionario
        self.assertIn('name', state_dict)
        self.assertEqual("California", state_dict['name'])

        # Verificar que las claves '__class__', 'id', 'created_at' y \
        # 'updated_at' estén presentes
        self.assertIn('__class__', state_dict)
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)


if __name__ == "__main__":
    unittest.main()
