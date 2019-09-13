class Creator(site):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()

        result = f"Creator: The same creator's code has just worked with {product.operation()}"

        return result
