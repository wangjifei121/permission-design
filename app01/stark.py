from stark.servers.site import site

from app01 import models


site.register(models.School)
site.register(models.Order)
site.register(models.Department)
site.register(models.UserInfo)
site.register(models.Course)
site.register(models.ClassList)
site.register(models.Customer)
site.register(models.ConsultRecord)
site.register(models.Student)
site.register(models.ClassStudyRecord)
site.register(models.StudentStudyRecord)