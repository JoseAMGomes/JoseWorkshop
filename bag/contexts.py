from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0
    project_count = 0
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'project_count': project_count,
    }

    return context