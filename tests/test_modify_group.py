from model.group import Group


def test_modify_group_name(app):
    app.session.login(user="admin", password="secret")
    app.group.modify_first(Group(name="New group"))
    app.session.logout()

# def test_modify_group_header(app):
#     app.session.login(user="admin", password="secret")
#     app.group.modify_first(Group(header="New header"))
#     app.session.logout()
#
