from flask import Flask, render_template, request, send_file
import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/generate', methods=['POST'])
def generate():

    file = request.files['file']

    data = pd.read_csv(file)

    average_marks = data["Marks"].mean()
    highest_marks = data["Marks"].max()
    lowest_marks = data["Marks"].min()

    file_name = "Student_Report.pdf"

    pdf = canvas.Canvas(file_name,pagesize=A4)

    width,height=A4

    pdf.setFont("Helvetica-Bold",18)

    pdf.drawCentredString(
        width/2,
        height-50,
        "Student Performance Report"
    )

    pdf.setFont("Helvetica",12)

    y=height-100

    pdf.drawString(
        50,
        y,
        f"Total Students: {len(data)}"
    )

    y-=25

    pdf.drawString(
        50,
        y,
        f"Average Marks: {average_marks:.2f}"
    )

    y-=25

    pdf.drawString(
        50,
        y,
        f"Highest Marks: {highest_marks}"
    )

    y-=25

    pdf.drawString(
        50,
        y,
        f"Lowest Marks: {lowest_marks}"
    )

    y-=40

    pdf.setFont("Helvetica-Bold",12)
    pdf.drawString(50,y,"Student Details")

    y-=30

    pdf.setFont("Helvetica",12)

    for _,row in data.iterrows():

        pdf.drawString(
            60,
            y,
            f"{row['Name']} - {row['Marks']} Marks"
        )

        y-=20

    pdf.save()

    return send_file(
        file_name,
        as_attachment=True
    )


if __name__=="__main__":
    app.run(debug=True)