
from dotenv import load_dotenv
import os

load_dotenv()
key = os.environ.get('RAZORPAY_KEY')
print(key)