import structlog
from django.contrib.auth import authenticate
from django.urls import path

from tastypie.authorization import Authorization
from tastypie.exceptions import BadRequest
from tastypie.http import HttpUnauthorized
from tastypie.models import ApiKey
from tastypie.resources import ModelResource

from customers.models import Customer

logging = structlog.getLogger(__name__)


class CustomerResource(ModelResource):
    """Customer Resource for CRUD operations."""
    required_fields = ("username", "first_name", "email", "password")

    class Meta:
        queryset = Customer.objects.all()
        resource_name = "customer"
        authorization = Authorization()

    def prepend_urls(self):
        """Added customized views for login and signup."""
        return [
            path("customer/signup/", self.wrap_view('signup'), name='user_signup'),
            path("customer/login/", self.wrap_view('login'), name='api_login'),
        ]

    @staticmethod
    def get_token(customer_id):
        """Gets the APIKey for a given customer ID."""
        return ApiKey.objects.get(user__id=customer_id).key

    def signup(self, request, **kwargs):
        """Creates new user and return the APIKey, id, status."""
        data = self.deserialize(request, request.body, format=request.META.get(
            'CONTENT_TYPE', 'application/json'))  # Got json data convert to dict
        missing_fields = set(self.required_fields).difference(set(data.keys()))
        if missing_fields:
            raise BadRequest(f"Bad Request: Missing fields {missing_fields}")
        username = data['username']
        password = data['password']
        email = data['email']
        first_name = data["first_name"]
        customer, create = Customer.objects.get_or_create(username=username, defaults={"first_name": first_name,
                                                                                       "password": password,
                                                                                       "email": email})
        if not create:
            raise BadRequest("Bad Request: Customer already exists.")
        customer.set_password(password)
        customer.save()
        api_key = self.get_token(customer.id)
        logging.info("successfully_registered")
        return self.create_response(request, {
            'api_key': api_key,
            'id': customer.id,
            'success': True
        })

    def login(self, request, **kwargs):
        """Login Endpoint - On successful login, username, APIKey are provided in response."""
        self.method_check(request, allowed=['post'])
        data = self.deserialize(request, request.body, format=request.META.get(
            'CONTENT_TYPE', 'application/json'))  # Got serialised data convert to dict
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user:
            token = self.get_token(user.id)
            # custom_user_obj = Customer.objects.get(user__username=user)
            logging.info("logged_in")
            return self.create_response(request, {
                'access_token': token,
                'username': username,
                'success': True
            })
        else:
            return self.create_response(
                request,
                {'success': False, 'message': 'User is not registered or user is inactive state'},
                HttpUnauthorized
            )
