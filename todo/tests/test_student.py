from todo.student import Student

class TestStudent:
    def test_name(self):
        s = Student('yjl')
        assert s.name == 'yjl'

