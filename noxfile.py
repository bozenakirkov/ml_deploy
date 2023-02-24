import nox

@nox.session
def tests(session):
    session.install("pytest", "tensorflow", "numpy")
    session.notify("coverage")

@nox.session
def coverage(session):
   session.install("coverage")
   session.run("coverage")
