from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flash messages to work
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bmicare.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
admin = Admin(app, name='BMICare Admin', template_mode='bootstrap3')

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)  # Admin field added
    bmi_history = db.relationship('BMIHistory', backref='user', lazy=True)
    contact_messages = db.relationship('ContactMessage', backref='user', lazy=True)

# BMIHistory model
class BMIHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bmi = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# ContactMessage model
class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Admin views
class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

# Register admin views
admin.add_view(AdminModelView(User, db.session))
admin.add_view(AdminModelView(BMIHistory, db.session))
admin.add_view(AdminModelView(ContactMessage, db.session))

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

    if current_user.is_authenticated:
        bmi_record = BMIHistory(bmi=bmi, user_id=current_user.id)
        db.session.add(bmi_record)
        db.session.commit()

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
        message = request.form['message']
        if current_user.is_authenticated:
            contact_message = ContactMessage(message=message, user_id=current_user.id)
            db.session.add(contact_message)
            db.session.commit()
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Wrong credentials! Please try again.', 'error')
    
    return render_template('login.html')

# Route for register page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        is_admin = request.form.get('is_admin') == 'on'  # Check if checkbox is checked

        existing_user = User.query.filter_by(username=username).first()
        if existing_user is None:
            user = User(username=username, email=email, password=password, is_admin=is_admin)
            db.session.add(user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
    
    return render_template('register.html')

# Route for user dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    bmi_history = BMIHistory.query.filter_by(user_id=current_user.id).all()
    contact_messages = ContactMessage.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard.html', bmi_history=bmi_history, contact_messages=contact_messages)

# Route for logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
