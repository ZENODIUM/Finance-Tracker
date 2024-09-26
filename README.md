# Gamified Finance Tracker with Prophet Prediction

## Overview
The Gamified Finance Tracker is a web application built with Django that allows users to track their financial items, set budgets, and analyze spending habits using predictive analytics with the Prophet library. Users can enjoy a gamified experience while managing their finances and predicting future expenses based on their historical data.

## Features
- **User Registration & Authentication**: Secure registration, login, and logout functionalities.
- **Financial Item Management**: Users can add, remove, and categorize financial items.
- **Budget Setting**: Set a monthly budget and track expenses against it.
- **Gamification**: Progress tracking with lives based on budget adherence.
- **Expense Summary**: Visual representation of expenses through line graphs and pie charts.
- **Expense Prediction**: Forecast future expenses using the Prophet model.
- **CSV Export**: Download financial items as a CSV file for offline analysis.

## Screenshots
![WhatsApp Image 2024-09-24 at 13 57 14_773f1884](https://github.com/user-attachments/assets/aca04e9c-5fe6-4eb7-8fa0-97068780ee48)
![WhatsApp Image 2024-09-24 at 19 10 56_3d9a86dd](https://github.com/user-attachments/assets/59b93d01-5a40-43fe-b537-c15b19740eae)
![WhatsApp Image 2024-09-24 at 19 11 15_abb1841a](https://github.com/user-attachments/assets/4cc2c3ff-28cb-4beb-a4f4-a19c2e36745a)
![WhatsApp Image 2024-09-24 at 19 12 00_d672e2a6](https://github.com/user-attachments/assets/0f925ddd-b51d-4564-a76e-9e5675366942)


![WhatsApp Image 2024-09-24 at 19 10 35_1a1e9909](https://github.com/user-attachments/assets/c6735bfe-53a9-42cf-8c11-764217a1ecea)

## Requirements

- Python 3.x
- Django
- Pandas
- Matplotlib
- Prophet

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/gamified-finance-tracker.git
   cd gamified-finance-tracker
# Gamified Finance Tracker with Prophet Prediction

## Overview
The Gamified Finance Tracker is a web application built with Django that allows users to track their financial items, set budgets, and analyze spending habits using predictive analytics with the Prophet library. Users can enjoy a gamified experience while managing their finances and predicting future expenses based on their historical data.

## Features
- **User Registration & Authentication**: Secure registration, login, and logout functionalities.
- **Financial Item Management**: Users can add, remove, and categorize financial items.
- **Budget Setting**: Set a monthly budget and track expenses against it.
- **Gamification**: Progress tracking with lives based on budget adherence.
- **Expense Summary**: Visual representation of expenses through line graphs and pie charts.
- **Expense Prediction**: Forecast future expenses using the Prophet model.
- **CSV Export**: Download financial items as a CSV file for offline analysis.

## Requirements
- Python 3.x
- Django
- Pandas
- Matplotlib
- Prophet

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/gamified-finance-tracker.git
   cd gamified-finance-tracker
2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
## Usage

1. **Register**: Create a new account.
2. **Login**: Log into your account.
3. **Dashboard**: View, add, or remove financial items and set your budget.
4. **Summary**: Visualize your expenses through line and pie charts.
5. **Prediction**: Get predictions for your next month's expenses.
6. **Download**: Export your financial items to a CSV file.

## Code Structure

### Views

The application has several views handling different functionalities:

```python
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from collections import defaultdict
from django.contrib import messages
import pandas as pd
import os
import matplotlib.pyplot as plt
from prophet import Prophet
import csv
from .models import FinancialItem, UserProfile

# Authentication Views
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    # Registration logic here

def user_login(request):
    # Login logic here

def user_logout(request):
    # Logout logic here

@login_required
def welcome(request):
    # Dashboard logic here

@login_required
def summary(request):
    # Summary logic here

@login_required
def predict(request):
    # Prediction logic here

@login_required
def download_items_csv(request):
    # CSV download logic here

```

The application uses the following models:

```python
from django.db import models
from django.contrib.auth.models import User

class FinancialItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    tag = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.IntegerField()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    monthly_budget = models.FloatField(default=0)
    progress_bar = models.IntegerField(default=0)
    level_number = models.IntegerField(default=1)

    def update_progress_and_level(self, latest_item):
        # Update progress logic here
```
## Requirements

- Python 3.x
- Django
- Prophet
- Matplotlib
- Other dependencies as listed in `requirements.txt`

## Future Improvements

- Add user roles (e.g., admin)
- Implement notifications for budget exceedance
- Improve UI/UX with frontend frameworks (e.g., React, Bootstrap)

## License

This project is licensed under the MIT License.
