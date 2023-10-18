from flask import Flask, request, jsonify
import database
import certificate
import jwt_handler

app = Flask(__name)

@app.route('/generate_certificate', methods=['POST'])
def generate_cert():
    data = request.get_json()
    student_name = data['student_name']
    teacher_name = data['teacher_name']
    certificate_filename = f"{student_name}_{teacher_name}_certificate.pdf"
    certificate.generate_certificate(student_name, teacher_name, certificate_filename)
    
    return jsonify({"message": "Certificate generated successfully"})

@app.route('/generate_token', methods=['POST'])
def generate_jwt():
    data = request.get_json()
    certificate_id = data['certificate_id']
    token = jwt_handler.generate_token({"certificate_id": certificate_id})
    
    return jsonify({"token": token})

@app.route('/verify_certificate', methods=['POST'])
def verify_cert():
    data = request.get_json()
    token = data['token']
    result = jwt_handler.verify_token(token)
    
    if isinstance(result, dict):
        return jsonify({"message": "Certificate is valid", "certificate_id": result['certificate_id']})
    else:
        return jsonify({"message": result})

if __name__ == '__main__':
    database.create_tables()
    app.run(debug=True)
