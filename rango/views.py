from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect, HttpResponse

from rango.forms import UserForm, UserProfileForm
from rango.forms import CategoryForm, PageForm

from rango.bing_search import run_query

from rango.models import Category, Page, UserProfile

from django.shortcuts import render, redirect

from datetime import datetime

def about(request):
    # If the visits session varible exists,
    # take it and use it.
    # If it doesn't, we haven't visited the site
    # so set the count to zero.
    if request.session.get('visits'):
        count = request.session.get('visits')
    else:
        count = 0
    
    context_dict = {
    	'boldmessage': "You've reached the about page",
        'visits': count
    }

    return render(
        request,
        'rango/about.html',
        context_dict
    )



@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        # provided a valid form? saving form data
        # provided by the user to the associated
        # model, and rendering the homepage
        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            # supplied form contained errors
            # just print them to the terminal
            # if there are errors, redisplay the 
            # form with error messages
            print form.errors
    else:
        # If request was not a POST (e.g GET), 
        # display the form to enter details.
        form = CategoryForm()
    # Bad form (or form details), no form supplied
    # Render the form with error messages (if any).
    return render(
        request, 
        'rango/add_category.html', 
        {
            'form': form, 
        }
    )


@login_required
def add_page(request, category_name_slug):
    # allow users to add pages to a given category.

    try:
        cat = Category.objects.get(slug=category_name_slug)

    except Category.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()

                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {
        'form': form, 
        'category': cat,
        'category_name_slug': category_name_slug,
    }

    return render(request, 'rango/add_page.html', context_dict)


# all view functions defined as part of a Django 
# project must take at least one parameter. This is 
# typically called request - and provides access to 
# information related to the given HTTP request made 
# by the user. When parameterising URLs, you supply 
# additional named parameters to the signature for 
# the given view. It's not the position of the 
# additional parameters that matters, it's the name 
# that must match anything defined within the URL
# pattern. Note how category_name_slug defined in the
# URL pattern matches the category_name_slug parameter
# defined for our view. Using category_name_slug in 
# our view will give python-books, or whatever value 
# was supplied as that part of the URL.

# Update the category view to handle a HTTP POST request.
#  The view must then include any search results in the
#   context dictionary for the template to render.

def category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}
    context_dict['result_list'] = None
    context_dict['query'] = None
    
    try:
       # Can we find a category name slug with the 
        # given name? If we can't, the .get() method 
        # raises a DoesNotExist exception. So the 
        # .get() method returns one model instance 
        # or raises an exception.  
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model instance.
        # order by views
        pages = Page.objects.filter(category=category).order_by('-views')
        context_dict['pages'] = pages
       # We also add the category object from the 
        # database to the context dictionary.
        # We'll use this in the template to verify 
        # that the category exists.
        # this category view passes reference to category
        # object, "like" can be accsed with { { category.likes } }
        # in the template.

        context_dict['category'] = category
        # category slug for adding pages gets passed
        # to context
        context_dict['category_name_slug'] = category.slug

        if request.method=='POST':
            result_list = []

            query = request.POST.get('query').strip()
            if query:
                result_list = pages.filter(title__icontains=query)
                result_list = [{
                    'title': page.title,
                    'summary': unicode('None'), 
                    'link': page.url
                } for page in result_list]

                result_list += run_query(query)

                context_dict['result_list'] = result_list

    except Category.DoesNotExist:
          # We get here if we didn't find the specified 
        # category. Don't do anything - the template 
        # displays the "no category" message for us.
        pass

    return render(request, 'rango/category.html', context_dict)


@login_required
def edit_profile(request):
     # first calling GET profile.html
    # then post after submitting from edit_profile.html
    if request.method == 'POST':
        current_profile = UserProfile.objects.get(user=request.user)
        # 
        current_form = UserProfileForm(request.POST, instance=current_profile)
        
        if current_form.is_valid():
            updated_profile = current_form.save(commit=False)
            try:
                updated_profile.picture = request.FILES['picture']
            except:
                pass
        updated_profile.save()
        return profile(request)
    else:
        current_form = UserProfileForm(request.GET)
        return render(request, 'rango/edit_profile.html', {'current_form': current_form})


def index(request):
    #for testing cookies
    #request.session.set_test_cookie()

    # # Query the database for a list of ALL categories 
    # currently stored. Order the categories by no. 
    # likes in descending order. Retrieve the top 5 
    # only - or all if less than 5. sort by the number 
    # of likes in descending order - hence the inclusion 
    # of the -
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by(
        '-views')[:5]

    context_dict = {
        'categories': category_list,
        'pages' : page_list,
    }

    # Now instead of storing the cookies directly in
    # the request (and thus on the client's machine),
    # you can access the server side cookies via the
    # method call request.session.get() and store
    # them with request.session[]. Note that a session
    # ID cookie is still used to remember the client's
    # machine (so technically a browser side cookie
    # exists), however all the data is stored serve side.
    visits = request.session.get('visits')
    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')
    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 0:
            # ...reassign the value of the cookie to +1 of
            # what it was before...
            visits = visits + 1
            # ...and update the last visit cookie, too.
            reset_last_visit_time = True
    else:
        # Cookie last_visit doesn't exist, so create it to
        # the current date/time.
        reset_last_visit_time = True

    if reset_last_visit_time:
        request.session['last_visit'] = str(datetime.now())
        request.session['visits'] = visits
    context_dict['visits'] = visits


    response = render(request,'rango/index.html', context_dict)

    return response

@login_required
def like_category(request):
    # assumes category_id has been passed
    # via a GET so that the we can identify 
    #the category to update.
    # TODO: track and record that a particular 
    #user has "liked" this category
    cat_id = None
    if request.method == 'GET':
        cat_id = request.GET['category_id']

    likes = 0
    if cat_id:
        cat = Category.objects.get(id=int(cat_id))
    if cat:
        likes = cat.likes + 1
        cat.likes =  likes
        cat.save()

    return HttpResponse(likes)




def list_profiles(request):
    current_user = request.user
    users = User.objects.all()
    try:
        profiles = UserProfile.objects.all()
    except:
        profiles = None

    context_dict = {
        'users': users,
        'profiles': profiles,
        'current_user': current_user,

    }

    # user.id corresponds to profiles[#].user_id
    return render(request, 'rango/list_profiles.html', context_dict)


@login_required
def profile(request):

    user = User.objects.get(id=request.user.id)
    
    # did user have a website/picture?
    try:
        profile = UserProfile.objects.get(user=user)
    except:
        profile = None

    context_dict = {
        'user': user,
        'profile': profile
    }

    return render(request, 'rango/profile.html', context_dict)

def register_profile(request):
    if request.method=='POST':
        profile_form = UserProfileForm(data=request.POST)
        if profile_form.is_valid():
            if request.user.is_authenticated():
                profile = profile_form.save(commit=False)
                user = User.objects.get(id=request.user.id)
                profile.user = user

                if 'picture' in request.FILES:
                    profile.picture = request.FILES['picture']
                
                profile.save()
                
                return index(request)
    else:
        form = UserProfileForm(request.GET)

    return render(request, 'rango/profile_registration.html', {'profile_form': form})

### function taken over by redux ###
# def register(request):
#     # for testing cookies
#     # if request.session.test_cookie_worked():
#     #     print ">>>> TEST COOKIE WORKED!"
#     #     request.session.delete_test_cookie()

#     # A boolean value for telling the template
#     # whether the registration was successful.
#     # Set to False initially. Code changes value to
#     # True when registration succeeds.
#     registered = False
#      # If it's a HTTP POST, we're interested in
#     # processing form data.
#     if request.method == 'POST':
#     # Attempt to grab information from the raw
#         # form information.
#         # Note that we make use of both UserForm and
#         # UserProfileForm.
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileForm(
#             data=request.POST
#         )

#         if user_form.is_valid() and profile_form.is_valid():
#             # Save the user's form data to the database.

#             user = user_form.save()
#             # Now we hash the password with the
#             # set_password method.
#             # Once hashed, we can update the user
#             # object.
#             user.set_password(user.password)
#             user.save()
#             # Now sort out the UserProfile instance.
#             # Since we need to set the user attribute
#             # ourselves, we set commit=False.
#             # This delays saving the model until
#             # we're ready to avoid integrity problems.
#             profile = profile_form.save(commit=False)
#       #  establish a link between the two model
#             # instances created. After creating a new
#             # User model instance, reference it in the
#             # UserProfile. populate the user
#             # attribute of the UserProfileForm
#             # form       
#             profile.user = user
#             # Did the user provide a profile picture?
#             # If so, we need to get it from the input
#             # form and put it in the UserProfile model.
#             if 'picture' in request.FILES:
#                 profile.picture = request.FILES['picture']
#             # Now we save the UserProfile model
#             # instance.
#             profile.save()
#                 # Update our variable to tell the
#             # template registration was successful.
#             registered = True

#         else:
#         # Invalid form or forms - mistakes or
#         # something else?
#         # Print problems to the terminal.
#         # They'll also be shown to the user.
#             print user_form.errors, profile_form.errors

#     # Not a HTTP POST, so we render our form using
#     # two ModelForm instances.
#     # These forms will be blank, ready for user
#     # input.
#     else:
#         user_form = UserForm()
#         profile_form = UserProfileForm()

#     return render(
#         request,
#         'rango/register.html',
#         {
#             'user_form': user_form, 
#             'profile_form': profile_form, 
#             'registered': registered
#             }
#     )


# Use the login_required() decorator to ensure only
# those logged in can access the view.
@login_required
def restricted(request):
    #return HttpResponse("hola")
    loggedIn = True
    return render(
        request,
        'rango/restricted.html',
        {
            'loggedIn': loggedIn
        }
    )


### function taken over by redux ###
# def user_login(request):
#     # If the request is a HTTP POST, try to pull out the relevant information.

#     if request.method == 'POST':
#      # Gather the username and password provided
#         # by the user. This information is obtained
#         # from the login form. We use
#         # request.POST.get('<variable>') as opposed
#         # to request.POST['<variable>'], because the
#         # request.POST.get('<variable>') returns
#         # None, if the value does not exist,
#         # while the request.POST['<variable>'] will
#         # raise key error exception
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#     # Use Django's machinery to attempt to see if
#         # the username/password
#         # combination is valid - a User object is
#         # returned if it is.
#         user = authenticate(username=username, password=password)

#         if user:
#          # Is the account active? It could have been
#             # disabled.   
#             if user.is_active:
#      # If the account is valid and active, we
#                 # can log the user in.
#                 # We'll send the user back to the
#                 # homepage.
#                 login(request, user)
                
#                 return HttpResponseRedirect('/rango/')
#             else:
#              # An inactive account was used - no
#                 # logging in!
#                 # return simple message to login after bad
#                 # login
#                 return render(
#                     request,
#                     'rango/login.html',
#                     {
#                         'loginError', 'Disabled account'
#                     }
#                 )
#                 # return HttpResponse(
#                 #     "Your Rango account is disabled."
#                 # )
#         else:
#         # Bad login details were provided. So we can't
#             # log the user in.
#             print "Invalid login details: {0}, {1}".format(
#                 username, password
#             )

#             return render(
#                 request, 
#                 'rango/login.html', 
#                 {
#                     'loginError': 'Invalid login details'
#                 }
#             )
#             # return HttpResponse(
#             #     "Invalid login details supplied."
#             # )
#  # The request is not a HTTP POST, so display the
#     # login form.
#     # This scenario would most likely be a HTTP GET.
#     else:
#        # No context variables to pass to the template
#         # system, hence the
#         # blank dictionary object...
#         #return render(request, 'rango/login.html', {})
#         # return when a GET 
#          return render(
#             request, 
#             'rango/login.html', 
#             {
#                 'loginError': None
#             }
#         )

### function taken over by redux ###
# @login_required
# def user_logout(request):
#     logout(request)

#     return HttpResponseRedirect('/rango/')


def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run Bing function to get results list
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})

def view_profile(request):
    # rewrite this
    # this is ugly :( 
    # merge with profile
    url = '/rango/'
    
    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']
            print page_id , "is what i got", request.user.id
            user = User.objects.get(id=page_id)
    
            # did user have a website/picture?
            try:
                profile = UserProfile.objects.get(user=user)
            except:
                profile = None

    context_dict = {
        'user': user,
        'profile': profile
    }

    return render(request, 'rango/profile.html', context_dict)

def track_url(request):
    # TODO: create url patter to go with this
    # why not.
    url = '/rango/'
    page_id = None
    
    if request.method == 'GET':
        if 'page_id' in request.GET:

            page_id = request.GET['page_id']
            
            try:
                page = Page.objects.get(id=int(page_id))
                page.views = page.views + 1
                page.save()
                url = page.url
            except:
                pass

    return redirect(url)