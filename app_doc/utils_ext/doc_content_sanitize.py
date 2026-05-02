# coding:utf-8

ALLOWED_TAGS = [
    'p', 'br',
    'strong', 'b', 'em', 'i', 'u',
    'ul', 'ol', 'li',
    'a',
    'img',
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'blockquote',
    'code', 'pre'
]

ALLOWED_ATTRIBUTES = {
    "*":['style'],
    'a': ['href', 'title', 'target', 'rel'],
    'img': ['src', 'alt', 'title'],
}

ALLOWED_PROTOCOLS = ['http', 'https', 'mailto']

def sanitize_html(html):
    import bleach
    return bleach.clean(
        html,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRIBUTES,
        protocols=ALLOWED_PROTOCOLS,
        strip=True
    )