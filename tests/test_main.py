import allure

@allure.feature("Math Module")
@allure.story("Basic arithmetic")
def test_addition():
    with allure.step("Check addition logic"):
        assert 2 + 2 == 4