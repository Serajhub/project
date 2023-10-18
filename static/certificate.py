from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_certificate(student_name, teacher_name, output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    c.drawString(100, 700, f"Student: {student_name}")
    c.drawString(100, 680, f"Teacher: {teacher_name}")
    # Add other certificate details here
    c.save()
