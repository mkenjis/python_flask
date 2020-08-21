from flask_table import Table, Col, LinkCol
 
class Results(Table):
    user_id = Col('user_id', show=False)
    user_name = Col('user_name')
    user_email = Col('user_email')
    user_password = Col('user_password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))