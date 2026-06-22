from flask import session


def isAuthed():
    return session.get("currentUser") != None
