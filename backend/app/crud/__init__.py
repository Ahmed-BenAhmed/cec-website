from .crud_member import CRUDMember, member
from .crud_project import CRUDProject, project
from .crud_event import CRUDEvent, event
from .crud_blog import CRUDBlog, blog

__all__ = [
    'member', 'CRUDMember',
    'project', 'CRUDProject',
    'event', 'CRUDEvent',
    'blog', 'CRUDBlog'
]