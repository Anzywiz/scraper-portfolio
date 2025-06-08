import streamlit as st
import base64
import pandas as pd
import plotly.express as px
from st_social_media_links import SocialMediaIcons
import random


# Page configuration
st.set_page_config(
    page_title="Ifeanyi Muotoe - Web Scraping Expert",
    page_icon="🕷️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Function to convert image to base64 format
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string
    except FileNotFoundError:
        return None


# Apply CSS formatting
try:
    with open('style.css', 'r') as file:
        st.markdown(f'<style>{file.read()}</style>', unsafe_allow_html=True)
except FileNotFoundError:
    # Fallback CSS if style.css doesn't exist
    st.markdown("""
    <style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .project-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .nav-item {
        padding: 0.5rem 1rem;
        margin: 0.25rem 0;
        border-radius: 0.5rem;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .nav-item:hover {
        background-color: #e6e9ef;
    }
    .nav-item.active {
        background-color: #667eea;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("🕷️ Ifeanyi Muotoe")
st.sidebar.markdown("---")

# Navigation options
nav_options = {
    "🏠 Home": "home",
    "🚀 Portfolio": "portfolio",
    "💻 Code Examples": "code",
    "📊 Data Samples": "data",
    "📞 Contact": "contact"
}

# Create navigation
selected_page = st.sidebar.radio(
    "Navigate to:",
    list(nav_options.keys()),
    index=0
)

# Add some info in sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("""
**Quick Stats:**
- 3+ Years Experience
- 4M+ Records Scraped
- 500+ Websites Handled
- 98% Success Rate
""")

st.sidebar.markdown("---")
st.sidebar.markdown("**Contact Info:**")
st.sidebar.markdown("📧 ifeanyi.webapp@gmail.com")

# Main content based on selection
if selected_page == "🏠 Home":
    # Hero Section
    st.markdown("""
    <div class="main-header">
        <h1>🕷️ Ifeanyi Muotoe</h1>
        <h3>Expert Web Scraping & Automation Specialist</h3>
        <p>Transforming web data into business insights</p>
    </div>
    """, unsafe_allow_html=True)

    # Profile image
    image_base64 = get_base64_image("profile_pic-chopped.jpg")
    if image_base64:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.markdown(
                f"""
                <div style="text-align: center; margin: 2rem 0;">
                    <img src="data:image/png;base64,{image_base64}" 
                         alt="Profile Picture" 
                         style="border-radius: 50%; width: 200px; height: 200px; object-fit: cover; box-shadow: 0 4px 8px rgba(0,0,0,0.3);">
                </div>
                """,
                unsafe_allow_html=True
            )

    # Key Metrics Row
    st.subheader("📊 At a Glance")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Years of Experience", "3+", "Growing")
    with col2:
        st.metric("Records Scraped", "4M+", "High Volume")
    with col3:
        st.metric("Websites Handled", "500+", "Diverse")
    with col4:
        st.metric("Success Rate", "98%", "Reliable")

    st.markdown("---")

    # About Section
    st.subheader("🎯 About Me")

    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        I'm a passionate web scraping specialist with over three years of hands-on experience in extracting valuable data from both static and dynamic websites. I excel at overcoming complex challenges including:

        **🔧 Technical Expertise:**
        - Advanced anti-bot detection bypass (Cloudflare, reCAPTCHA)
        - Large-scale data extraction and processing
        - Dynamic content handling with JavaScript rendering
        - Proxy management and IP rotation
        - Data cleaning and validation

        **💼 Business Value:**
        In today's data-driven world, accurate and reliable data extraction is essential for informed decision-making. I provide comprehensive data solutions that empower businesses to gain competitive advantages through better data access.
        """)

    with col2:
        st.info(
            "💡 **What sets me apart:**\n\n- Overcome complex anti-bot systems\n- Handle high-volume extractions\n- Deliver clean, structured data\n- Ensure reliable, consistent results")
elif selected_page == "🚀 Portfolio":
    st.title("🚀 Portfolio & Projects")

    # Project showcase with better visual hierarchy
    projects = [
        {
            "title": "🇨🇳 Tieba Baidu Forum Scraper",
            "scale": "1M+ Posts Extracted",
            "description": "Large-scale forum data extraction across multiple Tieba Baidu Forums",
            "challenges": ["Multi-forum navigation", "Volume optimization", "Data consistency"],
            "tech": ["Python", "BeautifulSoup", "MySQL", "Proxy rotation"],
            "results": {
                "Posts Scraped": "1,000,000+",
                "Forums Covered": "50+",
                "Data Accuracy": "99.5%",
                "Processing Time": "72 hours"
            }
        },
        {
            "title": "🏛️ IMPI Registry Scraper",
            "scale": "400K+ Records",
            "description": "Comprehensive patent and trademark data extraction from official registry",
            "challenges": ["IP blocking mitigation", "JavaScript optimization", "Large dataset management"],
            "tech": ["Python", "Selenium", "DigitalOcean", "Linux", "Multi-Threading"],
            "results": {
                "Records Extracted": "400,000+",
                "Final Dataset Size": "600,000 rows",
                "Columns Captured": "56",
                "Uptime": "99.8%"
            }
        },
        {
            "title": "🏠 Sreality.cz Real Estate Scraper",
            "scale": "Complete Website Coverage",
            "description": "Comprehensive real estate listings extraction from Czech Republic's leading property portal",
            "challenges": ["Czech language encoding issues", "Complex pagination", "Rate limiting compliance"],
            "tech": ["Python", "Requests", "BeautifulSoup", "Pandas", "Multi-Threading"],
            "results": {
                "Listings Scraped": "100,000+",
                "Speed Improvement": "5x faster",
                "Compliance Rate": "100%",
                "Delivery": "Reusable bot"
            }
        },
        {
            "title": "⚡ Monad Testnet Automation Bot",
            "scale": "Multi-dApp Integration",
            "description": "Open-source automation bot for repeated blockchain tasks on Monad testnet, enabling users to focus on other activities while maintaining consistent protocol interactions",
            "challenges": ["Web3 API integration", "Multi-dApp coordination", "Proxy management", "Account balance monitoring"],
            "tech": ["Python", "Web3.py", "Requests", "DEX APIs", "Proxy Integration"],
            "results": {
                "dApps Integrated": "13+ protocols",
                "Daily Tasks": "Automated",
                "GitHub Stars": "11+",
                "Community": "Open Source"
            }
        }
    ]

    for i, project in enumerate(projects):
        with st.container():
            st.markdown(f"""
            <div class="project-card">
                <h3>{project['title']}</h3>
                <p><strong>Scale:</strong> {project['scale']}</p>
                <p>{project['description']}</p>
            </div>
            """, unsafe_allow_html=True)

            # Project details in expandable section
            with st.expander(f"View Details - {project['title']}"):
                col1, col2 = st.columns(2)

                with col1:
                    st.write("**Key Challenges Solved:**")
                    for challenge in project['challenges']:
                        st.write(f"✅ {challenge}")

                    st.write("**Technologies Used:**")
                    st.write(" • ".join(project['tech']))

                with col2:
                    st.write("**Project Results:**")
                    for metric, value in project['results'].items():
                        st.metric(metric, value)

            st.markdown("---")

elif selected_page == "💻 Code Examples":
    st.title("💻 Code Examples & Techniques")

    st.write("Here are some examples of my web scraping techniques and solutions:")

    # Improved code examples with better organization
    example_categories = {
        "🌐 Basic Web Scraping": {
            "description": "Foundation techniques for static content extraction",
            "code": '''
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

class BasicWebScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.session = requests.Session()

    def scrape_products(self, url, max_pages=5):
        """Scrape product listings with pagination support"""
        all_products = []

        for page in range(1, max_pages + 1):
            page_url = f"{url}?page={page}"

            try:
                response = self.session.get(page_url, headers=self.headers)
                soup = BeautifulSoup(response.text, 'html.parser')

                products = soup.find_all('div', class_='product-item')

                for product in products:
                    data = {
                        'name': self.safe_extract(product, 'h2', 'product-name'),
                        'price': self.safe_extract(product, 'span', 'price'),
                        'rating': self.safe_extract(product, 'div', 'rating', attr='data-rating'),
                        'availability': self.safe_extract(product, 'span', 'stock-status')
                    }
                    all_products.append(data)

                # Respectful delay between requests
                time.sleep(random.uniform(1, 3))

            except Exception as e:
                print(f"Error on page {page}: {e}")
                continue

        return pd.DataFrame(all_products)

    def safe_extract(self, container, tag, class_name, attr=None):
        """Safely extract data with error handling"""
        try:
            element = container.find(tag, class_=class_name)
            if element:
                return element.get(attr) if attr else element.text.strip()
        except:
            pass
        return 'N/A'
            '''
        },
        "🔐 Authentication Handling": {
            "description": "Techniques for accessing protected content",
            "code": '''
import requests
from bs4 import BeautifulSoup
import json

class AuthenticatedScraper:
    def __init__(self):
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json, text/html,application/xhtml+xml',
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    def login(self, login_url, username, password):
        """Handle login with CSRF token support"""
        # Get login page
        login_page = self.session.get(login_url, headers=self.headers)
        soup = BeautifulSoup(login_page.text, 'html.parser')

        # Extract CSRF token
        csrf_token = None
        csrf_input = soup.find('input', {'name': ['csrf_token', '_token', 'authenticity_token']})
        if csrf_input:
            csrf_token = csrf_input.get('value')

        # Prepare login data
        login_data = {
            'username': username,
            'password': password,
        }

        if csrf_token:
            login_data['csrf_token'] = csrf_token

        # Perform login
        response = self.session.post(login_url, data=login_data, headers=self.headers)

        # Verify login success
        if self.verify_login(response):
            print("✅ Login successful")
            return True
        else:
            print("❌ Login failed")
            return False

    def verify_login(self, response):
        """Verify if login was successful"""
        success_indicators = ['dashboard', 'welcome', 'profile', 'logout']
        return any(indicator in response.text.lower() for indicator in success_indicators)
            '''
        },
        "🛡️ Anti-Bot Bypass": {
            "description": "Advanced techniques for bypassing detection systems",
            "code": '''
import requests
import time
import random
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class AntiDetectionScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.session = self.create_session()
        self.proxies = self.load_proxy_list()
        self.current_proxy_index = 0

    def create_session(self):
        """Create session with retry strategy"""
        session = requests.Session()

        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )

        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)

        return session

    def get_random_headers(self):
        """Generate randomized headers"""
        return {
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': random.choice(['en-US,en;q=0.5', 'en-GB,en;q=0.9']),
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

    def scrape_with_protection(self, url, max_retries=3):
        """Scrape with full anti-detection measures"""
        for attempt in range(max_retries):
            try:
                headers = self.get_random_headers()
                response = self.session.get(url, headers=headers, timeout=30)

                if response.status_code == 200:
                    return response

                time.sleep(random.uniform(2, 5))

            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(random.uniform(1, 3))

        return None
            '''
        },
        "⚡ Dynamic Content": {
            "description": "Handling JavaScript-rendered content with Selenium",
            "code": '''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DynamicContentScraper:
    def __init__(self, headless=True):
        self.driver = self.setup_driver(headless)

    def setup_driver(self, headless):
        """Configure Chrome driver with stealth options"""
        options = Options()

        if headless:
            options.add_argument("--headless")

        # Stealth options
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        driver = webdriver.Chrome(options=options)
        return driver

    def wait_for_element(self, selector, timeout=10):
        """Wait for element to be present"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selector))
            )
            return element
        except:
            return None

    def handle_infinite_scroll(self, scroll_count=5):
        """Handle infinite scroll pages"""
        for i in range(scroll_count):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

    def scrape_spa_content(self, url):
        """Scrape Single Page Application content"""
        self.driver.get(url)
        self.wait_for_element(".content-container")
        self.handle_infinite_scroll()

        items = self.driver.find_elements(By.CSS_SELECTOR, ".item")

        data = []
        for item in items:
            try:
                item_data = {
                    'title': item.find_element(By.CSS_SELECTOR, ".title").text,
                    'content': item.find_element(By.CSS_SELECTOR, ".content").text
                }
                data.append(item_data)
            except:
                continue

        return data
            '''
        }
    }

    # Display code examples in tabs
    tab_names = list(example_categories.keys())
    code_tabs = st.tabs(tab_names)

    for tab, (category, content) in zip(code_tabs, example_categories.items()):
        with tab:
            st.write(f"**{content['description']}**")
            st.code(content['code'], language='python')

elif selected_page == "📊 Data Samples":
    st.title("📊 Data Samples & Results")

    st.write("Examples of the structured data I deliver to clients:")

    # Create sample datasets
    sample_tabs = st.tabs(["Tieba Forum Data", "E-commerce Data", "Business Listings", "Performance Metrics"])

    with sample_tabs[0]:
        st.subheader("Sample Tieba Baidu Forum Data")

        # Create cleaned Tieba data based on your snippet
        tieba_data = pd.DataFrame({
            'post_id': ['140303539072', '140481221322', '144889029969', '140481221322', '138684980132', '146898697939',
                        '119818474756', '35662304517', '40702187613', '52071138320'],
            'timestamp': ['2021-07-15 19:38:00', '2021-07-26 18:54:00', '2022-07-27 16:45:00', '2021-07-28 11:45:36',
                          '2021-04-08 06:56:00', '2023-02-19 05:46:00', '2018-05-20 20:50:00', '2013-07-18 19:19:00',
                          '2013-10-23 22:42:00', '2014-06-12 21:48:00'],
            'text': ['亿维锂能工程、工艺、品质岗位这三个岗主要干啥，工作环境如何。', '你已经入职了吗', '现在去了吗', '没去', '请问湖北亿玮动力法务岗应届生待遇怎么样呢？',
                     '楼主了解到了吗？我也收到了亿纬offer', '还真有点怀恋亿纬了……', '欢迎来到亿纬吧！', '请问这是惠州亿纬贴吧吗？', '..'],
            'thread_title': ['亿维锂能工程岗位咨询', '亿维锂能工程岗位咨询', '亿维锂能工程岗位咨询', '亿维锂能工程岗位咨询', '湖北亿纬动力法务岗', '湖北亿纬动力法务岗', '怀恋亿纬',
                             '欢迎贴', '公司咨询', '日常讨论'],
            'username': ['瀛戠劧濡掔伀鈾', 'deathcharge', 'Anonymous', '瀛戠劧濡掔伀鈾', '抬头望星空璀璨', '橘和枳999', '腐草为萤1103i', '贴吧楼委会',
                         'yanzizuozuo', '孙剑超27'],
            'gender': ['male', 'female', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'male']
        })

        st.dataframe(tieba_data, use_container_width=True)

        # Add visualization
        col1, col2 = st.columns(2)
        with col1:
            gender_counts = tieba_data['gender'].value_counts()
            fig_gender = px.pie(values=gender_counts.values, names=gender_counts.index,
                                title='User Gender Distribution')
            st.plotly_chart(fig_gender, use_container_width=True)

        with col2:
            # Convert timestamp to datetime for analysis
            tieba_data['timestamp'] = pd.to_datetime(tieba_data['timestamp'])
            tieba_data['year'] = tieba_data['timestamp'].dt.year
            yearly_posts = tieba_data['year'].value_counts().sort_index()
            fig_timeline = px.bar(x=yearly_posts.index, y=yearly_posts.values, title='Posts by Year')
            st.plotly_chart(fig_timeline, use_container_width=True)

    with sample_tabs[1]:
        st.subheader("Sample E-commerce Product Data")

        # Create realistic sample data
        ecommerce_data = pd.DataFrame({
            'Product_Name': [
                'Wireless Bluetooth Headphones', 'Smartphone Case', 'USB-C Cable',
                'Portable Charger', 'Screen Protector', 'Car Phone Mount',
                'Bluetooth Speaker', 'Wireless Mouse', 'Laptop Stand', 'Phone Ring Holder'
            ],
            'Price': ['$89.99', '$24.99', '$12.99', '$34.99', '$9.99', '$19.99', '$79.99', '$29.99', '$49.99', '$7.99'],
            'Rating': [4.5, 4.2, 4.8, 4.3, 4.1, 4.6, 4.4, 4.7, 4.2, 4.0],
            'Reviews_Count': [1523, 892, 2341, 567, 1205, 434, 987, 1876, 345, 789],
            'Availability': ['In Stock', 'In Stock', 'Limited', 'In Stock', 'In Stock', 'In Stock', 'Out of Stock',
                             'In Stock', 'In Stock', 'Limited'],
            'Category': ['Electronics', 'Accessories', 'Cables', 'Power', 'Protection', 'Car Accessories', 'Audio',
                         'Computer', 'Office', 'Accessories']
        })

        st.dataframe(ecommerce_data, use_container_width=True)

        # Add visualization
        col1, col2 = st.columns(2)
        with col1:
            fig_rating = px.histogram(ecommerce_data, x='Rating', title='Rating Distribution')
            st.plotly_chart(fig_rating, use_container_width=True)

        with col2:
            fig_category = px.pie(ecommerce_data, names='Category', title='Products by Category')
            st.plotly_chart(fig_category, use_container_width=True)

    with sample_tabs[2]:
        st.subheader("Sample Business Listing Data")

        business_data = pd.DataFrame({
            'Business_Name': [
                'Tech Solutions Inc', 'Digital Marketing Pro', 'Web Design Studio',
                'Data Analytics Corp', 'Software Development LLC', 'Cloud Services Ltd',
                'Mobile App Creators', 'SEO Specialists', 'E-commerce Solutions', 'IT Consulting Group'
            ],
            'Address': [
                '123 Tech St, Silicon Valley, CA', '456 Marketing Ave, Austin, TX',
                '789 Design Blvd, Portland, OR', '321 Data Dr, Seattle, WA',
                '654 Code Ln, San Francisco, CA', '987 Cloud Rd, Denver, CO',
                '147 Mobile Way, Miami, FL', '258 SEO St, Chicago, IL',
                '369 Commerce Dr, Atlanta, GA', '741 Consulting Ct, Boston, MA'
            ],
            'Phone': [f'({random.randint(200, 999)}) {random.randint(200, 999)}-{random.randint(1000, 9999)}' for _ in
                      range(10)],
            'Rating': [round(random.uniform(3.5, 5.0), 1) for _ in range(10)],
            'Category': ['Technology', 'Marketing', 'Design', 'Analytics', 'Development', 'Cloud', 'Mobile', 'SEO',
                         'E-commerce', 'Consulting']
        })

        st.dataframe(business_data, use_container_width=True)

    with sample_tabs[3]:
        st.subheader("Scraping Performance Metrics")

        # Performance data
        performance_data = pd.DataFrame({
            'Date': pd.date_range('2024-01-01', periods=30, freq='D'),
            'Records_Scraped': [random.randint(5000, 15000) for _ in range(30)],
            'Success_Rate': [random.uniform(95, 99.9) for _ in range(30)],
            'Avg_Response_Time': [random.uniform(0.5, 3.0) for _ in range(30)]
        })

        col1, col2 = st.columns(2)

        with col1:
            fig_volume = px.line(performance_data, x='Date', y='Records_Scraped',
                                 title='Daily Scraping Volume')
            st.plotly_chart(fig_volume, use_container_width=True)

        with col2:
            fig_success = px.line(performance_data, x='Date', y='Success_Rate',
                                  title='Success Rate Over Time')
            st.plotly_chart(fig_success, use_container_width=True)

        # Summary metrics
        st.subheader("Summary Statistics")
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Records", f"{performance_data['Records_Scraped'].sum():,}")
        with col2:
            st.metric("Avg Success Rate", f"{performance_data['Success_Rate'].mean():.1f}%")
        with col3:
            st.metric("Avg Response Time", f"{performance_data['Avg_Response_Time'].mean():.2f}s")
        with col4:
            st.metric("Uptime", "99.8%")

elif selected_page == "📞 Contact":
    st.title("📞 Get In Touch")

    # Center the content
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 2rem;">
            <h3>Ready to work together?</h3>
            <p>Let's discuss your project</p>
        </div>
        """, unsafe_allow_html=True)

        # Contact info
        st.markdown("---")
        st.markdown("""
        **📧 Email:** ifeanyi.webapp@gmail.com

        **⏰ Response Time:** Within 24 hours

        """)

        st.markdown("---")

# footer
# social media links
st.markdown("<br><br><br>", unsafe_allow_html=True)


social_media_links = [
    "https://github.com/Anzywiz",
    "https://www.linkedin.com/in/ifeanyi-muotoe-01ab83190",
    "https://x.com/IMuotoe53886"
]

colors = ["Blue", "Blue", "Blue"]

social_media_icons = SocialMediaIcons(social_media_links, colors)
social_media_icons.render()
