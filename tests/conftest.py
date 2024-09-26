from pytest import fixture

@fixture
def owner(accounts):
    return accounts[0]

@fixture
def another(accounts):
    return accounts[1]

@fixture
def flipper(project, owner):
    return owner.deploy(project.Flipper)