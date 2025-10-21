from src.category import Category


def test_category_init(category, first_product, second_product, third_product):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category.category_count == 1
    assert Category.product_count == 3