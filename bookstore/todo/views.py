from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    # print(request.body)
    # print(request.method)
    # print(request.path)
    # print(request.GET)
    # print(request.POST)
    # print(request.COOKIES)
    # print(request.FILES)
    # print(request.META)
    # render (requst, template name, context=None, content_type=None)
    # redirect (to, *args, **kwargs)
    # redirect('/profile' , {'nick_name': 'iti'})
    #localhost:8000/profile 
    # res = HttpResponse("hello world")
    # res.write("<p> Hello OS </>")
    # res['content-type'] = 'text/plain'
    # return res
    # # return JsonResponse({'Track': 'OS'})
    # return HttpResponseRedirect('/')
    return render(request, 'main/base_layout.html')


task_list = [
    {
        'index': 0,
        'id': 1,
        'name': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'priority': 1,
        'description': "Set in a dystopian society, this classic novel portrays a totalitarian regime where Big Brother watches over every aspect of people's lives, and individualism is suppressed. Orwell's chilling portrayal of a future dominated by surveillance and manipulation remains a thought-provoking and timeless masterpiece.",
    },
    {
        'index': 1,
        'id': 2,
        'name': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'priority': 4,
        'description': " Austen's beloved novel revolves around the spirited Elizabeth Bennet and her complicated relationship with the proud Mr. Darcy. Set in the Regency era, it offers a witty commentary on social norms, marriage, and the importance of overcoming one's prejudices. With its memorable characters and sharp social observations, it remains a timeless work of literature.",
    },
    {
        'index': 2,
        'id': 3,
        'name': 'The Catcher in the Rye',
         'author': 'J.D. Salinger',
        'priority': 2,
        'description': " Narrated by the disillusioned teenager Holden Caulfield, this influential coming-of-age novel captures the angst and alienation of youth. As Holden navigates through various encounters in New York City, Salinger explores themes of identity, alienation, and the loss of innocence in a society he perceives as phony.",
    },
]


def _get_task(task_id):
    for task in task_list:
        if 'id' in task and task['id'] == task_id:
            return task
    return None
    
def todo_list(request):
    my_context = {'taks_list': task_list}
    # template_loader > todo/templates/
    return render(request, 'book_store/book_list.html', context=my_context)

def todo_detail(request, *args, **kwrgs):
    task_id = kwrgs.get('task_id')
    task_object = _get_task(task_id)
    my_context = {
        'task_id': task_object.get('id'),
        'task_name': task_object.get('name'),
         'task_author': task_object.get('author'),
        'task_priority': task_object.get('priority'),
        'task_description': task_object.get('description')
    }

    return render(request, 'book_store/book_details.html', context=my_context)


def todo_delete(request, **kwargs):
    task_id = kwargs.get('task_id')
    task_object = _get_task(task_id)
    if task_list:
        task_list.remove(task_object)
    return redirect('todo:todo-list')   

# def todo_update(request, **kwargs):
#     task_id = kwargs.get('task_id')
#     task_object = _get_task(task_id)
#     for task in task_list:
#         if task == task_object:
#             task['name'] = f"Update {task_object['name']}"
            
#     return redirect('todo:todo-list') 
def todo_update(request, **kwargs):
    if request.method == 'POST':
        task_id = kwargs.get('task_id')
        task_object = _get_task(task_id)

        # Update the task with the new data from the request
        task_object['name'] = request.POST.get('name')
        task_object['author'] = request.POST.get('author')
        task_object['priority'] = request.POST.get('priority')
        task_object['description'] = request.POST.get('description')

        return redirect('todo:todo-list')

    else:
        task_id = kwargs.get('task_id')
        task_object = _get_task(task_id)
        my_context = {
            'task_id': task_object.get('id'),
            'task_name': task_object.get('name'),
              'task_author': task_object.get('author'),
            'task_priority': task_object.get('priority'),
            'task_description': task_object.get('description')
        }

        return render(request, 'book_store/book_update.html', context=my_context)

