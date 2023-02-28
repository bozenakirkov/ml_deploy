import nox


@nox.session
def tests(session):
    session.install("coverage", "pytest", "tensorflow", "numpy", "flask", "flasgger")
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report", "-m")

