class Vector:

    '''
    Conversion of oject to list
    '''
    def __init__(self, vals: list):
        if isinstance(vals, list):
            self.vals = vals
        else:
            self.vals = list(vals)


    def multiply_with_scalar(self, mul_scalar: float):
        
        # self.vals = [mul_scalar * x for x in self.vals]
        return [mul_scalar * x for x in self.vals]
        # multiplied_vector = [mul_scalar * x for x in self.vals]
        # return multiplied_vector


    def add_vectors(self, other):
        other_vector = other.vals if isinstance(other, Vector) else other
        return [x+y for x, y in zip(self.vals, other_vector)]

v = Vector([1, 2, 3])
multiplied_vector = v.multiply_with_scalar(5)
print('Vector after multiplication: ', multiplied_vector)
added_vector = v.add_vectors(multiplied_vector)
print('Vector after addition: ', added_vector)


# [1, 2, 3] -> *5 ==> [5, 10, 15] -> + [1, 2, 3] => [6, 12, 18]





    # def scalar_multiply(self, mul_scalar: float):
    #     self.vals = [mul_scalar * x for x in self.vals]

    # def add(self, add_scalar: flot):
    #     self.vals = [add_scalar + x for x in self.vals]

    # def add(self, sub_scalar: flot):
    #     self.vals = [sub_scalar + x for x in self.vals]

    # def add(self, div_scalar: flot):
    #     self.vals = [div_scalar + x for x in self.vals]










    # def test_non_empty_vector_contents():
    #     v = Vector([1, 2, 3])
    #     assert v.vals == [1, 2, 3]

    # def test_empty_vector_contents
    #     v = Vector([])
    #     assert len(v.vals) == [1, 2, 3]

    # def test_vector_constructor():
    #     v = Vector(())
    #     assert v.vals == []









    








