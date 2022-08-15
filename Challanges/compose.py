"""С точки зрения математики, композиция функций f и g — новая функция z(x) = f(g(x)).

Реализуйте функцию compose(), которая принимает на вход две других одноаргументных функции и возвращает новую функцию. Эта новая функция также должна принимать один аргумент и применять к нему исходные функции в нужном порядке: для функций f и g порядок применения должен выглядеть, как f(g(x))."""

# BEGIN
def compose(f, g):
    return lambda x: f(g(x))
# END