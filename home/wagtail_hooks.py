from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.models import Page

@hooks.register('register_admin_menu_item')
def register_page_menu_item():
    return MenuItem('Pages', '/admin/pages/', classnames='icon icon-folder-open-inverse', order=200)
