from django import template

register = template.Library()

@register.filter
def get_cv_url(etudiant):
    if etudiant.cv:
        return etudiant.cv.url
    else:
        return None