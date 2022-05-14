class chain_sum(int):
    def __call__(self, value=0):
        return chain_sum(self + value)