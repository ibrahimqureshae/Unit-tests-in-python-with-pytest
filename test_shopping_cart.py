from unittest.mock import Mock
import pytest
from item_database import ItemDatabase
from shoppingcart import ShoppingCart

#setup the duplicate code in your tests
#called fixtures



@pytest.fixture
def cart():
     #All setup for the cart here..
     return ShoppingCart(5)

# unit test is a function in pytest 
# ,functions have naming conventions.
def test_can_add_item_to_cart(cart): 
    cart.add("apple")
    assert cart.size() == 1

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("apple")
    assert "apple" in cart.get_items()

def test_when_add_more_items_than_max_items_should_fail(cart):
    for i in range(5):
        cart.add("apple")

    with pytest.raises(OverflowError):
        cart.add("apple")
        
def test_can_get_total_price(cart):
    cart.add("apple")
    cart.add("orange")
    item_database = ItemDatabase()
    
    def mock_get_item(item: str):
        if item == "apple":
            return 1.0
        if item == "orange":
            return 2.0
        
    item_database.get = Mock(side_effect = mock_get_item)
    assert cart.get_total_price(item_database) == 3.0

    