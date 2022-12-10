import model_sum
import view


def button_click():
    a = view.get_value('a')
    b = view.get_value('b')
    model_sum.init(a, b)

    result = model_sum.sum()
    view.view_result(result)
