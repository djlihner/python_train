def test_del_group(app):
    app.session.login(user="admin", password="secret")
    app.group.del_first()
    app.session.logout()
