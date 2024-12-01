__pragma__('alias', 'S', '$')

from const import BASE_URL

class Model:
    # コンストラクタ
    def __init__(self):
        self._todos = []

    # 1 指定された ID の ToDo を取得する
    def get_todo(self, todo_id):
        for todo in self._todos:
            if todo['id'] == todo_id:
                return todo
        return None

    # 2 すべてのToDo を取得する
    def get_all_todos(self):
        return self._todos

    # 3 全件取得の API を呼び出す
    def load_all_todos(self):
        S.ajax({
            'url': f"{BASE_URL}todos",
            'type': 'GET',
        }).done(
            self._success_load_all_todos
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )

    # 4 load_all_todos()成功時の処理
    def _success_load_all_todos(self, data):
        self._todos = data
        S('body').trigger('todos-updated')
        
    
    # 1 ToDo 登録の API を呼び出す
    def create_todo(self, data):
        S.ajax({
            'url': f"{BASE_URL}todos",
            'type': 'POST',
            'contentType': 'application/json',
            'data': JSON.stringify(data),
        }).done(
            self._success_create_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )
    # 2 create_todo()成功時の処理
    def _success_create_todo(self, data):
        self._todos.append(data)
        S('body').trigger('todos-updated')
        
    #　Todo更新のAPIを呼び出す    
    def update_todo(self, todo_id, data):
        send_data = {}
        for key in ['title', 'memo', 'priority','completed']:
            if key in data:
                send_data[key] = data[key]
        S.ajax({
            'url': f"{BASE_URL}todos/{todo_id}",
            'type': 'PUT','contentType': 'application/json','data': JSON.stringify(send_data),
        }).done(
            self._success_update_todo
        ).fail(
            lambda d: alert('サーバーとの通信に失敗しました。')
        )
    
    # 2 update_todo()成功時の処理
    def _success_update_todo(self, data) :
        for i, todo in enumerate(self._todos):
            if todo['id'] == data['id']:
                self._todos[i] = data
        S('body').trigger('todos-updated')
        
    
    #1完了状態を反転する

    def toggle_todo(self, todo_id):
        todo = self.get_todo(todo_id)
        self.update_todo(todo_id, {'completed':not todo['completed']})