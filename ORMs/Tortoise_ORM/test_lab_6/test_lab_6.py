import pytest

from setup_db import fill_data
from soluciones import solucion_1, solucion_2, solucion_3
from tortoise.contrib import test
from tortoise.contrib.test import finalizer, initializer


@pytest.fixture(scope="session", autouse=True)
def initialize_tests(request):
    initializer(["modelos"], db_url="sqlite://:memory:", app_label="models")
    request.addfinalizer(finalizer)


class TestQueries(test.TestCase):
    async def test_query_1(self):
        expected = [
            ("Juan Pérez", 3),
            ("María López", 3),
            ("Carlos Gómez", 3),
            ("Laura Ramírez", 3),
            ("Andrés Torres", 3),
        ]
        
        await fill_data()
        actual = await solucion_1()
        
        assert expected == actual
        
    async def test_query_2(self):
        expected = [
            ("Camisa", 67.5),
            ("Pantalón", 66.0),
            ("Zapatos", 145.0),
            ("Bolso", 145.5),
            ("Reloj", 150.0),
            ("Bufanda", 33.0),
        ]
        
        await fill_data()
        actual = await solucion_2()
        
        assert expected == actual
        
    async def test_query_3(self):
        expected = [
            ("2023-06-01", 50.0),
            ("2023-06-02", 35.5),
            ("2023-06-03", 20.0),
            ("2023-06-04", 80.0),
            ("2023-06-05", 45.5),
            ("2023-06-06", 15.0),
            ("2023-06-07", 50.0),
            ("2023-06-08", 40.0),
            ("2023-06-09", 25.0),
            ("2023-06-10", 30.5),
            ("2023-06-11", 43.1),
        ]
        
        await fill_data()
        actual = await solucion_3()
        
        assert expected == actual
