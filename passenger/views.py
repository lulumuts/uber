from django.shortcuts import render

# Create your views here.
def passenger_home(request):
    return render(request, 'passenger/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            print(user)
            current_site = get_current_site(request)
            subject = 'Activate your Uber Account'
            message = render_to_string('passenger/account_activation_email.html',{
                'user' : user,
                'domain' : current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.driver.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'passenger/account_activation_invalid.html')

def account_activation_sent(request):
    current_user = request.user
    if current_user.is_authenticated():
        return redirect('account_activation_sent')
    return render(request, 'passenger/account_activation_sent.html')
