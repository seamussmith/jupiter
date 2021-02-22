from django.template.defaulttags import register

@register.inclusion_tag("components/button.html")
def Button(button_uuid, button_text):
    return {
        "button_uuid": button_uuid,
        "button_text": button_text
    }
