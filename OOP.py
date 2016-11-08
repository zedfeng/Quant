class ECDF:
    def __init__(self, observations):
        self.observations = observations

    def __call__(self, x):
        return sum(1 for obs in self.observations if obs <= x) / len(self.observations)

    class Polynomial:
        def __init__(self, coefficients):
            self.coefficients = coefficients

        def __call__(self, x):
            return sum(c * x ** i for i, c in enumerate(self.coefficients)

        def differentiate(self):
            diff_coefficients = []
            for i, c in enumerate(self.coefficients):
                diff_coefficients.append(i * c)
            diff_coefficients.remove(0)
            self.coefficients = diff_coefficients
