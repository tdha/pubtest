from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def voted(context, article):
    user = context['user']
    if article.response_set.filter(user=user, answer='yes'):
        return '<p class="mt-2 response-message-yes">You have voted YES</p>'
    elif article.response_set.filter(user=user, answer='no'):
        return '<p class="mt-2 response-message-no">You have voted NO</p>'
    else:
        return f'<button class="btn btn-light me-3 bungee-regular response-no" data-article-id="{{ article.id }}">No</button> <button class="btn btn-light ms-2 bungee-regular response-yes" data-article-id="{{ article.id }}">Yes</button>'