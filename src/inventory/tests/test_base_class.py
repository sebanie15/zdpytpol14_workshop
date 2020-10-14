from src.inventory.product import BaseProduct


def test_is_base_exists():
	assert BaseProduct

def test_is_base_class_has_name_attr():
	assert hasattr(BaseProduct('ala', 2.3, 10), 'name')

def test_base_class_repr():
	x = BaseProduct('ala', 2.3, 10)
	assert repr(x) == 'ala'