from stark.servers.site import site
from CRM import models
from stark.servers.site import ModelStark



site.register(models.User)
site.register(models.Role)
site.register(models.Permission)