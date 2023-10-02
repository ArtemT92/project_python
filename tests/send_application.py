from selene import browser
import pytest
import requests
import allure
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "artemtrunilin")
@allure.feature("Отправка заявки с одного адреса")
@allure.link("https://piter-online.net", name="Testing")

@pytest.mark.parametrize('execution_number', range(2))
def test_send_application(execution_number):
    with allure.step('Открываем главную страницу'):
        browser.open('/')

    # When
    with allure.step('Вводим в поле "Введите улицу" название улицы '):
        browser.element('input[class="app142 app149 app148 app144 app161 app143"]').type('Тестовая линия')
        browser.element('li[class="app154 app155"]').click()
    with allure.step('Вводим в поле "Дом" номер дома '):
        browser.element('input[class="app142 app149 app148 app144 app161"]').type('1')
        browser.element('li[class="app154 app155"]').click()
    with allure.step('Выбираем Тип подключения - В квартиру'):
        browser.element('//li[@class="app187"][1]').click()
    with allure.step('Кликаем на кнопку Показать тарифы'):
        browser.element('//div[@data-test="find_tohome_button"]').click()
    with allure.step('Закрываем всплывающее окно'):
        browser.element('//div[@datatest="close_popup1_from_quiz_input_tel"]').click()
    with allure.step('Нажимае кнопку Подключить/Подключить по акции в столбце СТОИМОСТЬ любого тарифа'):
        browser.element('//div[@datatest="providers_form_inspect_connect_tariff_button"]').click()
    with allure.step('Вводим номер телефона'):
        browser.element('input[datatest="popup_tariff_order_input_tel"]').type('1111111111')
    with allure.step('Нажимаем кнопку Оставить заявку'):
        browser.element('div[class="app206 app226 app235 app229 app207"]').click()

    # Then
@pytest.mark.parametrize('execution_number', range(2))
def test_check_status_code_200(execution_number):
    with allure.step('Проверяем у всех отправленных заявок статус 200'):
        response = requests.post('https://piter-online.net/api/orders?type=site101-callback')
        assert response.status_code == 200


