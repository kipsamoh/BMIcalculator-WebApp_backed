BMIcalculator-WebApp
========

BMIcalculator-WebApp is a simple Flask web application designed to calculate Body Mass Index (BMI) and provide health recommendations based on the BMI value. The application also includes informational pages about the service, a blog section, a contact page, and a user login feature.

Table of Contents
========

-   [Features](#features)

-   [Setup](#setup)

-   [Usage](#usage)

-   [File Structure](#file-structure)

-   [Screenshots](#screenshots)

-   [Contributing](#contributing)

-   [License](#license)

Features
========

-   **Home Page**: Calculate your BMI by entering your height and weight.

-   **About Page**: Learn more about BMI Care.

-   **Blog Page**: Read blog posts related to health and fitness.

-   **Contact Page**: Get in touch with the BMI Care team.

-   **Login Page**: Authenticate users to access protected content.

-   **BMI Calculation**: Provide health recommendations based on calculated BMI.

Setup
========

### Prerequisites

Ensure you have the following installed on your system:

-   Python 3.8 or higher

-   Flask

### Installation

1\.  **Clone the repository:**

`git clone https://github.com/kipsamoh/BMIcare.git

cd BMIcare`

1\.  **Create and activate a virtual environment:**

`python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate`

1\.  **Install dependencies:**

`pip install -r requirements.txt`

1\.  **Run the application:**

`python app.py`

1\.  **Access the application:**

Open your web browser and navigate to `http://localhost:5000`.

Usage
========

-   Navigate to the home page to calculate your BMI by entering your height and weight.

-   Explore the About page to learn more about BMI Care.

-   Visit the Blog page to read articles on health and fitness.

-   Use the Contact page to reach out to the BMI Care team.

-   Login using the Login page to access personalized content.

File Structure
========

`BMIcare/

├── static/

│   └── styles.css

├── templates/

│   ├── about.html

│   ├── blog.html

│   ├── contact.html

│   ├── home.html

│   ├── login.html

│   ├── result.html

├── app.py

├── bmi_calculator.py

├── requirements.txt

└── README.md

Contributing
========
We welcome contributions to enhance the BMI Care application. Please follow these steps to contribute:

1\.  Fork the repository.

2\.  Create a new feature branch: `git checkout -b feature/YourFeature`.

3\.  Commit your changes: `git commit -m 'Add YourFeature'`.

4\.  Push to the branch: `git push origin feature/YourFeature`.

5\.  Open a pull request.

License
========

This project is licensed under the MIT License. See the LICENSE file for details.
