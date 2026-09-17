from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_add_backpack_to_cart(driver):
    """验证添加 Backpack 并检查购物车商品信息"""

    # 1. 登录
    login_page = LoginPage(driver)

    login_page.open_page()

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    # 2. 商品页面
    inventory_page = InventoryPage(driver)

    title = inventory_page.get_product_title()

    print("\n商品页面标题：", title)

    assert title == "Products"

    # 3. 添加商品
    inventory_page.add_backpack_to_cart()

    cart_count = inventory_page.get_cart_count()

    print("购物车角标数量：", cart_count)

    assert cart_count == "1"

    # 4. 进入购物车
    inventory_page.open_cart()

    # 5. 创建购物车页面对象
    cart_page = CartPage(driver)

    cart_title = cart_page.get_page_title()

    print("购物车页面标题：", cart_title)

    assert cart_title == "Your Cart"

    # 6. 验证购物车商品
    item_name = cart_page.get_item_name()
    item_price = cart_page.get_item_price()
    item_quantity = cart_page.get_item_quantity()

    print("商品名称：", item_name)
    print("商品价格：", item_price)
    print("商品数量：", item_quantity)

    assert item_name == "Sauce Labs Backpack"
    assert item_price == "$29.99"
    assert item_quantity == "1"

    print("购物车商品信息验证通过")