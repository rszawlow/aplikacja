from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import MealChoice
from .forms import CustomUserCreationForm
from django.urls import reverse

class MealChoiceModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
    
    def test_meal_choice_creation(self):
        meal_choice = MealChoice.objects.create(
            user=self.user,
            want_obiad=True,
            want_sniadanie=True,
            want_kolacja=False,
            date='2023-09-01',
            last_choice_date='2023-09-01',
            num_want_sniadanie=1,
            num_want_obiad=1,
            num_want_kolacja=0
        )
        self.assertEqual(meal_choice.user.username, 'testuser')
        self.assertEqual(meal_choice.want_obiad, True)
        self.assertEqual(meal_choice.want_sniadanie, True)
        self.assertEqual(meal_choice.want_kolacja, False)
        self.assertEqual(meal_choice.date, '2023-09-01')
        self.assertEqual(meal_choice.last_choice_date, '2023-09-01')
        self.assertEqual(meal_choice.num_want_sniadanie, 1)
        self.assertEqual(meal_choice.num_want_obiad, 1)
        self.assertEqual(meal_choice.num_want_kolacja, 0)

    def test_meal_choice_str(self):
        meal_choice = MealChoice.objects.create(user=self.user, date='2023-09-01')
        self.assertEqual(str(meal_choice), 'testuser - 2023-09-01')

class CustomUserCreationFormTest(TestCase):
    def test_custom_user_creation_form_valid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123',
            'first_name': 'John',
            'surname': 'Doe',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_custom_user_creation_form_invalid(self):
        form_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass',
            'first_name': 'John',
            'surname': 'Doe',
        }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

class MealChoiceViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

    def test_meal_choice_view_get(self):
        response = self.client.get('/obiad_choice/')  # Użyj pełnej ścieżki do widoku
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'obiad/obiad_choice.html')

class YourAppViewTests(TestCase):
    def setUp(self):
        # Utwórz użytkownika do testów
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_register_view(self):
        response = self.client.get(reverse('obiad:register'))
        self.assertEqual(response.status_code, 200)

    def test_user_login_view(self):
        response = self.client.get(reverse('obiad:user_login'))
        self.assertEqual(response.status_code, 200)

    def test_index_view(self):
        response = self.client.get(reverse('obiad:index'))
        self.assertEqual(response.status_code, 200)

    def test_meal_choice_view(self):
        # Zaloguj użytkownika
        self.client.login(username='testuser', password='testpass')
        
        response = self.client.get(reverse('obiad:obiad_choice'))
        self.assertEqual(response.status_code, 200)
        
    def test_kucharz_dashboard_view(self):
        # Zaloguj użytkownika
        self.client.login(username='testuser', password='testpass')
        
        response = self.client.get(reverse('obiad:kucharz_dashboard'))
        self.assertEqual(response.status_code, 302)