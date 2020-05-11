import abc


class Exceptions:
    @abc.abstractmethod
    def test_throw_invalid_ip(self):
        pass

    @abc.abstractmethod
    def test_no_arg_passed(self):
        pass

    @abc.abstractmethod
    def test_too_many_arguments(self):
        pass

    @abc.abstractmethod
    def test_add_cidr_exceptions(self):
        pass

    @abc.abstractmethod
    def test_remove_cidr_exceptions(self):
        pass
