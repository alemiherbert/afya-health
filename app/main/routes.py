from . import main

@main.route("/")
def index():
    return "Hi there too"

@main.route("/appointments/")
@main.route("/appointments/all")
def appointments():
    return "Here is a list of all your appointments"


@main.route("/appointments/<appointment>")
def single_appointment(appointment):
    return f"This is a single appointment: {appointment}"


@main.route("/appointments/new")
def new_appointment():
    return "Make a new appointment"


@main.route("/appointments/<appointment>/reschedule")
def reschedule_appointment(appointment):
    return f"The appointment {appointment} has been reschduled"


@main.route("/appointments/<appointment>/delete")
def delete_appointment():
    return "Delete this appointment"
