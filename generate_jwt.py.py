import jwt
import datetime

def generate_jwt(role):
    secret_key = 'your_secret_key_here'  # Your secret key
    payload = {
        'sub': '1234567890',
        'name': 'Sandy Taramonli',
        'email': 's.taramonli@stjohn.ac.uk',
        'role': role,
        'iat': datetime.datetime.utcnow(),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=100000)
    }
    encoded_jwt = jwt.encode(payload, secret_key, algorithm='HS256')
    return encoded_jwt

def decode_jwt(encoded_jwt):
    secret_key = 'your_secret_key_here'  # Use the same secret key used for encoding
    decoded_jwt = jwt.decode(encoded_jwt, secret_key, algorithms=['HS256'])
    return decoded_jwt['role']

# Generate JWT for a patient
patient_token = generate_jwt('patient')
print("Generated JWT for patient:", patient_token)

# Decode JWT to extract the role
role = decode_jwt(patient_token)
print("Role extracted from JWT:", role)
