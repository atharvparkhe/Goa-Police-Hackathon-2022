
## Drishti App

#### Non-Cognisible Offense Records System

#### An explanation of the problem statement
- We have identified in our societies that most of the people that go on to become greater miscreants start out young and often perform repeated crimes maybe on small scales
- These people are often known to the local police but due to small degree crimes they are often let go with warnings left with no paper trail to trace and keep track of their activity.
- If we manage to maintain a record of these people with the local police it will be as though that we have eyes on them all the while and record their activities and access their details in potential cases

#### Proposed solution to the problem statement

- App based solution such that whenever any person is brought into the police station for whatever reason like a fist fight, verbal abuse, potential theft suspision, rash driving etc.
- Police official shall record and store it on the data base local to area of activity of that person along with his/her details. -Even if there is no conclusion to the case or if there is common scenario of "compromise" in the parties the details wll be still be stored for future reference.
How will this help?
- It will create fear among youngsers of getting tagged in the society
- It will help carve an identity/personality of that person repeatedly brought in and it will serve as a rich storehouse to look into if a similar case is registered in an area with unidentified suspects

### 🔗 Content

- [Overview](#drishti-app)
- [Content](#-content)
- [Event Overview](#-event-overview)
- [Team](#-team)
- [Problem Statement](#-problem-statement)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [API Reference](#-api-reference)
- [Environment Variables](#-environment-variables)
- [Run Locally](#-run-locally)
- [Documentation](#-documentation)
- [Screen-Shots](#-screen-shots)
- [Author](#-author)


### 🧬 Event Overview

Me and my team participated in our first ever 48hrs Hackathon event at [Goa Police Hackathon](https://www.linkedin.com/feed/hashtag/?keywords=inspirus2k21) in September 2022 at [Goa College of Engineering, Goa](https://www.linkedin.com/school/don-bosco-college-of-engineering-fatorda-goa/). 
Me along with [Ruthveek Desai](https://www.linkedin.com/in/DessaiRuthveek/), [Aniket Mandrekar](https://www.linkedin.com/in/aniket-mandrekar-779880233/) and [Sachin Padwalkar](https://www.linkedin.com/in/sachin-padwalkar-a265291ba/) had participated as a team, where I was working on [Django application](https://github.com/atharvparkhe/Goa-Police-Hackathon-2022/server/) (Backend), Sachin was handling [React application](https://github.com/Sachin9822/restu) (Frontend) for the Administration Section and Akash was handling [Androind application](https://github.com/AkashCSanjeev/Be-Seated) (Frontend).


### 👨‍👦‍👦 Team

- `Atharva Parkhe` -  Django Developer (Backend)  -  *Python* -   [LinkedIn](https://www.linkedin.com/in/atharva-parkhe-3283b2202/), [GitHub](https://github.com/atharvparkhe)

- `Sachin Padwalkar` -  Android Developer (Frontend) *Java* - [LinkedIn](https://www.linkedin.com/in/sachin-padwalkar-a265291ba/), [GitHub](https://github.com/Sachin9822)

- `Ruthveek Desai` -  Android Developer (Frontend) *Java* - [LinkedIn](https://www.linkedin.com/in/ruthveekdessai/), [GitHub](https://github.com/DessaiRuthveek)

- `Aniket Mandrekar` - Facial Recognision and Data Scraping (Backend) *Python* - [LinkedIn](https://www.linkedin.com/in/aniket-mandrekar-779880233/)


### 📃 Problem Statement

![Problem Statement](PROBLEM_STATEMENT.png)

### 📋 Features

- **USER AUTHENTICATION :** Users can Signup for a new account, Verify thier email id, Login using email and password, make a Forgot request to reset thier password. 

- **RESTAURANTS :** Users can view all restaurants listed on the app.

- **BOOKING :** User can make booking by selecting time-slots for a perticular service as per users choice.

- **SELLER AUTHENTICATION :** Seller (Shop-keepers) can Signup for a new account, Verify thier email id, Login using email and password, make a Forgot request to reset thier password. 

- **SELLER CMS :** Seller can manage thier content on the site. They can add, modify, delete thier online shop and the products that they sell in thier shop.

- **SELLER ORDER MANAGEMENT :** Seller can manage thier orders through the dashboard.


### 🧰 Tech Stack

- **`BACKEND`** : Django *(Python)*

- **`DATABASE`** : MySQL

- **`FRONTEND`** : 
    - **Admin Panel :** Android App *(Java)*
    - **Poice Application :** Android App *(Java)*


### 🛠 API Reference

**Postman Endpoints** : https://www.getpostman.com/collections/62195bba49fa9ccd6312

![Endpoints](docs/admin-endpoints.png)
![Endpoints](docs/police-endpoints.png)

**API Endpoints JSON file** (for importing into thunderclient / postman) is available in the docs folder or click [here](docs/endpoints.json)


### 🔐 Environment Variables

To run this project, you will need to add the following environment variables to your **.env** file

- `EMAIL_ID`  -  Email ID (which would be used to send emails)

- `EMAIL_PW`  -  Email Password

![ENV file](docs/env.png)


### 💻 Run Locally

***Step#1 : Clone Project Repository***

```bash
git clone https://github.com/atharvparkhe/https://github.com/atharvparkhe/Goa-Police-Hackathon-2022.git && cd https://github.com/atharvparkhe/Goa-Police-Hackathon-2022/server/
```

***Step#2 : Create Virtual Environment***

- If *virtualenv* is not istalled :
```bash
pip install virtualenv && virtualenv env
```
- **In Windows :**
```bash
    env/Scripts/activate
```
- **In Linux or MacOS :**
```bash
    source env/bin/activate
```

***Step#3 : Install Dependencies***

```bash
pip install --upgrade pip -r requirements.txt
```

***Step#4 : Add .env file***

- ENV file contents
    - **In Windows :**
    ```bash
        copy .env.example .env
    ```
    - **In Linux or MacOS :**
    ```bash
        cp .env.example .env
    ```
- Enter Your Credentials in the *".env"* file. Refer [Environment Variables](#-environment-variables)

***Step#5 : Run Server***

```bash
python manage.py runserver
```

- Open `http://127.0.0.1:8000/` or `http://localhost:8000/` on your browser.

*Check the terminal if any error.*

***Step#6 : Run Android App***

*Step#6(i) : Police App*

```bash
    https://github.com/atharvparkhe/Goa-Police-Hackathon-2022/app/
```

  *Step#6(ii) : Police Admin App*

```bash
    https://github.com/atharvparkhe/Goa-Police-Hackathon-2022/admin/
```

***Step#7 : Open folder in Android Studio***

***Step#8 : Select any Pixel Device as simulator***

***Step#9 : Press Build/Run Project Button***


### 📄 Documentation

The docs folder contain all the project documentations and screenshots of the project.You can go through the presentation [here](presentaion.pptx)

- **Local Server Base Link :** http://localhost:8000/

- **Admin Pannel Access :**
    - ***Email :*** "admin@admin.com"
    - ***Password :*** "password"


### 🌄 Screen-Shots

- **Authentication**

![Signup](docs/project/account/signup.png)
![Login](docs/project/account/login.png)
![Forgot](docs/project/account/forgot.png)
![Forgot](docs/project/account/reset.png)

- **Main**

![All Restaurants](docs/project/main/all-restaurants.png)
![Single Restaurant](docs/project/main/single-restaurant.png)
![Book Seat](docs/project/main/book-seat.png)
![Past Bookings](docs/project/main/past-bookings.png)


### 🙋🏻‍♂️ Author

**🤝 Connect with Atharva Parkhe**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/atharva-parkhe-3283b2202/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://www.github.com/atharvparkhe/)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://www.twitter.com/atharvparkhe/)
[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/atharvparkhe/)
[![LeetCode](https://img.shields.io/badge/-LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/patharv777/)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UChimOJO64hOqtE7HCgtiIig)
[![Discord](https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/8WNC43Xsfc)