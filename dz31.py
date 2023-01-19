class Student:
    def __init__(self, name1):
        self.name1 = name1
        self.n = self.Nout()

    def show(self):
        print(self.name1, '=>', end=' ')
        self.n.show()

    class Nout:
        def __init__(self):
            self.name = 'HP'
            self.pr = 'i7'
            self.ddr = '16'

        def show(self):
            print(self.name, self.pr, self.ddr)


st = Student('Roman')
st.show()

st1 = Student('Vladimir')
st1.show()
