def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()


test_function()
# inner_function() вне функции test_function() нельзя вызвать (выдает ошибку),
# т.к. она принадлежит к локальному пространству имен внутри области видимости test_function().
# при добавлении в test_function() команды global inner_function - её можно будет вызвать вне функции test_function.
