def environment_check(results_only: bool = True):
    """
    Checks whether the host system is compatible with the applications requirements and dependencies.
    :param results_only: check only? or attempt to resolve compatibility issues?
    :return: dictionary breakdown OR boolean if 'results_only' is true
    """
    paths = {

    }
    if results_only:
        return True


class Installer(object):
    def __init__(self):
        self.results = environment_check()

    def run_install(self):
        pass


if __name__ == '__main__':
    pass
