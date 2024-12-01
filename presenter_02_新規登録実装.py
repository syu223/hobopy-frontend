__pragma__('alias', 'S', '$')

from model import Model
from view import View

class Presenter:
    # コンストラクタ
    def __init__(self):
        self._model = Model()
        self._view = View()
        self._bind()

    # 1 イベントをバインドする
    def _bind(self):
        S('body').on('todos-updated', self._on_todos_updated)
        S('#input-form').on('show.bs.modal', self._on_show_modal)
        S('#register-button').on('click', self._on_click_register)

    # 2 初期表示処理
    def start(self):
        self._model.load_all_todos()

    # 3 todos-updated 受信時の処理
    def _on_todos_updated(self, event):
        self._view.render_todo_list(self._model.get_all_todos())
        
        

    # 2 show.bs.modal 受信時の処理
    def _on_show_modal(self, event):
        self._view.show_new_modal()

    # 3 register-button の click 受信時の処理
    def _on_click_register(self, event):
        input_data = self._view.get_input_data()
        self._model.create_todo(input_data)
        self._view.close_modal()
    
    


        