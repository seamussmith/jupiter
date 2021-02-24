from django.template.defaulttags import register

@register.inclusion_tag("components/button.html")
def Button(button):
    return {
        "button": button
    }
