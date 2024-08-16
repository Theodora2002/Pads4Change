from kybra import query, update, Principal, stable

class User(stable):
    principal_id: Principal
    role: str  # 'admin' or 'school'

users: dict[Principal, User] = {}

@update
def register_user(principal_id: Principal, role: str) -> bool:
    if role not in ['admin', 'school']:
        return False
    users[principal_id] = User(principal_id=principal_id, role=role)
    return True

@query
def get_user(principal_id: Principal) -> User:
    return users.get(principal_id, None)

