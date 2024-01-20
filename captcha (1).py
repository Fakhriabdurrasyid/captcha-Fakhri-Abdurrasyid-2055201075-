import random
import base64
import string

def generate_captcha():
    # Generate random numbers
    random_numbers = [random.randint(0, 9) for _ in range(10)]
    
    # Convert numbers to string
    captcha = ''.join(map(str, random_numbers))
    
    # Encode captcha using Base64
    encoded_captcha = base64.b64encode(captcha.encode()).decode()
    
    # Cut the first 10 characters
    captcha_cut = encoded_captcha[:10]
    
    return captcha_cut

# Main program
print("Selamat datang di program Captcha!")
print("Silakan masukkan Captcha berikut:")
captcha = generate_captcha()
print(captcha)

input_captcha = input("Masukkan Captcha: ")

if input_captcha == captcha:
    print("Captcha benar! Anda berhasil login.")
else:
    print("Captcha salah! Silakan coba lagi.")