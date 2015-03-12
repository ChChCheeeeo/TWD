from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User
from django import forms


# While this step is not absolutely necessary, as you 
# could put the forms in the models.py, this makes the 
# codebase a lot cleaner and clearer to understand.
# Within Rango's forms.py module, we will be creating 
# a number of classes that inherit from Django's 
# ModelForm. In essence, a ModelForm is a helper class 
# that allows you to create a Django Form from a 
# pre-existing model. As we've already got two models 
# defined for Rango (Category and Page), we'kl create 
# ModelForms for both.

class CategoryForm(forms.ModelForm):
    # specified the widgets to use for each field to 
    # be displayed.
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
        # lengths that we specify are identical to the
        # maximum length of each field we specified in 
        # the underlying data models
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
# notice that we have included several IntegerField
    # entries for the views and likes fields in each 
    # form. Note that we have set the widget to be 
    #hidden with the parameter setting 
    # widget=forms.HiddenInput(), and then set the value
    # to zero with initial=0. This is one way to set the 
    # field to zero without giving the control to the 
    # user as the field will be hidden, yet the form 
    # will provide the value to the model. 
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information 
    # on the form. define which model we're wanting 
    # to provide a form for.
    class Meta:
        # Provide an association between the ModelForm 
        # and a model.  This is a crucial step 
        # enabling Django to take care of creating a 
        # form in the image of the specified model. It 
        # will also help in handling flagging up any 
        # errors along with saving and displaying the 
        # data in the form.
        model = Category

        # use the Meta class to specify which fields 
        # that we wish to include in our form through
        # the fields tuple. Use a tuple of field names
        #  to specify the fields you wish to include.
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

# clean/fix user url inputs . override ModelForm
    # 's clean() method. method is called upon before 
    # saving form data to a new model instance, and 
    # thus provides us with a logical place to insert 
    # code which can verify - and even fix - any form 
    # data the user inputs.     
    def clean(self):
    # Form data is obtained from the ModelForm 
        # dictionary attribute cleaned_data.
        cleaned_data = self.cleaned_data
    # Form fields that you wish to check can then 
        # be taken from the cleaned_data dictionary. 
        # Use the .get() method provided by the 
        # dictionary object to obtain the form's values. 
        # If a user does not enter a value into a form 
        # field, its entry will not exist in the 
        # cleaned_data dictionary. In this instance, 
        # .get() would return None rather than raise a 
        # KeyError exception.
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 
        # 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
        # For each form field that you wish to
            # process, check that a value was 
            # retrieved. If something was entered,
            # check what the value was. If it isn't 
            # what you expect, you can then add some
            #  logic to fix this issue before 
            # reassigning the value in the
            #  cleaned_data dictionary for the given
            # field.
            cleaned_data['url'] = url
# always end the clean() method by returning
        # the reference to the cleaned_data
        # dictionary. If you don't, you'll get some
        # really frustrating errors!
        return cleaned_data

    class Meta:
        # Provide an association between the ModelForm 
        # and a model
        model = Page

        # What fields do we want to include in our form?
        # This way we don't need every field in the 
        # model present.
        # Some fields may allow NULL values, so we may
        # not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field 
        # from the form,

        #despite the fact that we have a hidden field, 
        # we still need to include the field in the form.
        # If in fields we excluded views, then the form 
        # would not contain that field (despite it being 
        # specified) and so the form would not return 
        # the value zero for that field. 
        exclude = ('category',)
        # or specify the fields to include (i.e. not 
        # include the category field)
        #fields = ('title', 'url', 'views')


# The two ModelForm inheriting classes allow us to 
# display a HTML form displaying the necessary form
#  fields for a particular model, taking away a
# significant amount of work for us. 
class UserForm(forms.ModelForm):
    #  notice that UserForm includes a definition of
    # the password attribute. While a User model
    # instance contains a password attribute by
    # default, the rendered HTML form element will
    # not hide the password. If a user types a
    # password, the password will be visible. By
    # updating the password attribute, we can then
    # specify that the CharField instance should
    # hide a user's input from prying eyes through
    # use of the PasswordInput() widget.
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # nested Meta class describes additional
        # properties about the particular ModelForm
        # class it belongs to. Each Meta class must
        # at a bare minimum supply a model field,
        # which references back to the model the
        # ModelForm inheriting class should relate
        # to
        model = User
        # only display these fields
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        #  For the user field within UserProfile we
        # will need to make this association when we
        # register the user. (which fields to show)
        fields = ('website', 'picture')