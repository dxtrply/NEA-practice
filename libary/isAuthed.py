from flask import session


def usAuthed():
    return session.get("currentUser") != None
