from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages to work

# Dummy users for login (replace with actual authentication logic)
users = {
    'user1': {'username': 'user1', 'password': 'password1'},
    'user2': {'username': 'user2', 'password': 'password2'}
}

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for BMI calculation
@app.route('/calculate_bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = 'Underweight'
        recommendation = 'It is important to eat a balanced diet and maintain a healthy weight.'
    elif 18.5 <= bmi < 25:
        category = 'Normal weight'
        recommendation = 'Great job! Keep maintaining your current lifestyle to stay healthy.'
    elif 25 <= bmi < 30:
        category = 'Overweight'
        recommendation = 'Consider a balanced diet and regular exercise to manage your weight.'
    else:
        category = 'Obese'
        recommendation = 'It is advisable to consult a healthcare provider for guidance on achieving a healthier weight.'

    return render_template('index.html', bmi_result=bmi, bmi_category=category, bmi_recommendation=recommendation)

# Route for health & fitness blogs page
@app.route('/health_fitness_blogs')
def health_fitness_blogs():
    # Dummy blog post data
    blog_posts = [
        {
            'title': 'Understanding the Body Mass Index (BMI): A Tool for Assessing Health',
            'date': 'July 3, 2024',
            'author': 'By Dr. Sam H. Adams, Medical Expert at HealthCheck Insights',
            'content': """
                <p>Many people are aware of their Body Mass Index (BMI), similar to knowing their cholesterol level. If you're unsure of your BMI, numerous online calculators can assist you, including the one on HealthCheck Insights. Simply input your height and weight to determine your BMI, or you can calculate it manually with the formula:</p>
                <p><strong>BMI = (weight in pounds x 703) / (height in inches x height in inches)</strong></p>
                
                <h4>The Significance of BMI</h4>
                <p>Understanding what BMI represents and why it's measured is crucial. BMI calculates your body size by considering your height and weight. Historically, ideal weight charts from actuarial data were used, categorizing weights into small, medium, or large frames, which were often confusing and imprecise. BMI simplifies this by offering a single number to express the relationship between height and weight, independent of frame size. Despite its origins dating back over 200 years, BMI is a relatively recent metric in health assessment.</p>
                
                <h4>Interpreting BMI</h4>
                <p>Normal BMI: 18.5 to 24.9<br>
                Overweight: 25 to 29.9<br>
                Obese: 30 or higher<br>
                Underweight: Below 18.5</p>
                <p>BMI, while helpful, is not flawless. Factors like pregnancy, high muscle mass, and age can affect its accuracy. Nevertheless, BMI is significant as a high BMI is linked to increased risks of various health conditions, including:</p>
                <ul>
                    <li>Diabetes</li>
                    <li>Arthritis</li>
                    <li>Liver disease</li>
                    <li>Certain cancers (breast, colon, prostate)</li>
                    <li>Hypertension</li>
                    <li>High cholesterol</li>
                    <li>Sleep apnea</li>
                </ul>
                <p>According to the World Health Organization (WHO), nearly three million deaths annually are attributed to being overweight or obese. Additionally, many individuals with high BMIs report improved physical and psychological well-being after losing excess weight.</p>
                
                <h4>Limitations of BMI</h4>
                <p>Despite its usefulness, BMI can sometimes misclassify metabolic health, particularly in athletes, pregnant individuals, and the elderly. It’s essential to recognize that BMI, as a standalone measure, doesn't account for cardiovascular health or other specific conditions. For instance, research has shown that while a person might have a high BMI, their metabolic health could be normal, and vice versa.</p>
                
                <h4>BMI and Ethnic Diversity</h4>
                <p>BMI definitions based on predominantly white populations may not accurately reflect the health risks for people from other racial and ethnic backgrounds. For example:</p>
                <ul>
                    <li>Black individuals: Standard BMI measurements may overestimate health risks.</li>
                    <li>Asian individuals: Standard BMI measurements may underestimate health risks.</li>
                </ul>
                <p>Recognizing these discrepancies, the WHO and National Institutes of Health (NIH) recommend different BMI cutoffs for overweight and obesity among people of Asian descent, and adjustments are suggested for other ethnic groups as well.</p>
                
                <h4>Conclusion</h4>
                <p>BMI is not a perfect health measure but serves as a valuable starting point for identifying potential health issues related to weight. Knowing your BMI is beneficial, but it's important to understand its limitations and consider other health factors and individual differences.</p>
                <p>By acknowledging BMI's limitations and considering other health measures, you can make more informed decisions about your health and wellness journey.</p>
            """
        }
    ]
    return render_template('health_fitness_blogs.html', posts=blog_posts)

# Route for contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process form data (you can add more here if needed)
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username]['password'] == password:
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong credentials! Please try again.', 'error')
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
