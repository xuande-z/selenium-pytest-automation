from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_checkout_flow(driver):
    """验证 SauceDemo 完整购买流程"""

    # =========================
    # 1. 登录
    # =========================

    login_page = LoginPage(driver)

    login_page.open_page()

    login_page.login(
        username="standard_user",
        password="secret_sauce"
    )

    inventory_page = InventoryPage(driver)

    assert (
        inventory_page.get_product_title()
        == "Products"
    )

    print("\n登录成功")

    # =========================
    # 2. 添加商品
    # =========================

    inventory_page.add_backpack_to_cart()

    cart_count = (
        inventory_page.get_cart_count()
    )

    print("购物车数量：", cart_count)

    assert cart_count == "1"

    # =========================
    # 3. 进入购物车
    # =========================

    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert (
        cart_page.get_page_title()
        == "Your Cart"
    )

    assert (
        cart_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    assert (
        cart_page.get_item_price()
        == "$29.99"
    )

    assert (
        cart_page.get_item_quantity()
        == "1"
    )

    print("购物车验证通过")

    # =========================
    # 4. Checkout
    # =========================

    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)

    checkout_page.input_customer_information(
        first_name="Test",
        last_name="User",
        postal_code="518000"
    )

    checkout_page.click_continue()

    print("Checkout 信息填写完成")

    # =========================
    # 5. Checkout Overview
    # =========================

    overview_page = CheckoutOverviewPage(
        driver
    )

    overview_title = (
        overview_page.get_page_title()
    )

    print(
        "订单确认页面：",
        overview_title
    )

    assert (
        overview_title
        == "Checkout: Overview"
    )

    assert (
        overview_page.get_item_name()
        == "Sauce Labs Backpack"
    )

    assert (
        overview_page.get_item_price()
        == "$29.99"
    )

    print("订单商品验证通过")

    # =========================
    # 6. Finish
    # =========================

    overview_page.click_finish()

    complete_page = CheckoutCompletePage(
        driver
    )

    complete_title = (
        complete_page.get_page_title()
    )

    complete_message = (
        complete_page.get_complete_message()
    )

    print(
        "完成页面标题：",
        complete_title
    )

    print(
        "订单完成提示：",
        complete_message
    )

    assert (
        complete_title
        == "Checkout: Complete!"
    )

    assert (
        complete_message
        == "Thank you for your order!"
    )

    print(
        "完整购买流程验证通过"
    )