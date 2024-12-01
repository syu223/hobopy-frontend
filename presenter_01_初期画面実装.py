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

    # 2 初期表示処理
    def start(self):
        self._model.load_all_todos()

    # 3 todos-updated 受信時の処理
    def _on_todos_updated(self, event):
        self._view.render_todo_list(self._model.get_all_todos())
        