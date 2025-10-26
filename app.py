from flask import Flask, render_template, jsonify, request, send_file
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib.image as mpimg
import io
import base64

app = Flask(__name__)

# Ensure directories exist
os.makedirs('images', exist_ok=True)
os.makedirs('static', exist_ok=True)

def commentcgpa(cgpa):
    if cgpa >= 9:
        return "Outstanding CGPA. Keep up the excellent work!"
    elif cgpa >= 8:
        return "Very good CGPA. Aim for consistent performance."
    elif cgpa >= 7:
        return "Good CGPA. Can improve with more focus."
    else:
        return "Low CGPA. Needs serious academic improvement."

def commentmarks(avg_marks):
    if avg_marks >= 90:
        return "Excellent academic performance."
    elif avg_marks >= 75:
        return "Good performance. With a bit more effort, you can excel."
    elif avg_marks >= 60:
        return "Average marks. Work on weaker subjects."
    else:
        return "Below average. Needs improvement in most subjects."

def commentattendance(att):
    if att >= 90:
        return "Excellent attendance. Very regular."
    elif att >= 75:
        return "Good attendance. Can improve a little."
    elif att >= 60:
        return "Low attendance. Risk of affecting academics."
    else:
        return "Poor attendance. Needs urgent improvement."

def commentbehavior(grade):
    g = grade.strip().upper()
    if g in ("A", "B"):
        return f"Behavior grade {g}: disciplined and cooperative."
    elif g == "C":
        return f"Behavior grade {g}: average, can improve discipline."
    else:
        return f"Behavior grade {g}: needs serious improvement."

def generate_graph_base64(roll, df):
    """Generate graph and return as base64 string"""
    row = df[df["roll"] == roll].iloc[0]
    
    # Extract monthly attendance
    month_columns = ["jun","jul","aug","sep","oct","nov","dec","jan", "feb", "mar"]
    month_attendance = {month: float(row[month]) for month in month_columns}
    
    # Extract main fields
    cgpa = float(row["cgpa"])
    attendance = float(row["attendance"])
    behavior = str(row["behavior_grade"]).upper()
    perf_grade = str(row["performance_grade"]).upper()
    
    # Subjects
    ignore_cols = {"student_id","jun","jul","aug","sep","oct","nov","dec","jan", "feb", "mar",
                   "name","roll","attendance","cgpa","behavior_grade","performance_grade"}
    subject_cols = [c for c in df.columns if c not in ignore_cols]
    
    # Handle missing subject marks safely
    marks = {sub: float(row[sub]) if pd.notna(row[sub]) else 0 for sub in subject_cols}
    avg_marks = np.mean(list(marks.values()))
    
    plt.figure(figsize=(12, 8))
    
    # Subject-wise bar chart
    plt.subplot(3,2,4)
    plt.bar(range(len(marks)), list(marks.values()), color="skyblue")
    plt.xticks(range(len(marks)), list(marks.keys()), rotation=45, ha='right')
    plt.ylim(0, 100)
    plt.title(f"{row['name']} - Subject-wise Marks")
    plt.ylabel("Marks")
    
    # Pie chart for marks
    plt.subplot(3,2,2)
    class_avg_cgpa = df["cgpa"].mean()
    plt.bar(["Student CGPA","Class Avg CGPA"], [cgpa, class_avg_cgpa], color=["blue","gray"])
    plt.ylim(0, 10)
    plt.title(f"{row['name']} - CGPA vs Class Average")
    
    # Month-wise attendance
    plt.subplot(3,2,3)
    plt.bar(month_attendance.keys(), month_attendance.values(), color='lightgreen')
    plt.ylim(0, 100)
    plt.title(f"{row['name']} - Month-wise Attendance")
    plt.ylabel("Attendance (%)")
    plt.xlabel("Months")
    
    # Performance grade distribution (all students)
    grade_counts = df["performance_grade"].value_counts()
    plt.subplot(3,2,5)
    grade_counts.plot(kind="pie", autopct="%1.1f%%", startangle=140, colormap="Set3")
    plt.title("Performance Grade Distribution (All Students)")
    plt.ylabel("")
    
    # Student photo (optional)
    img_path_jpg = f"images/{roll}.jpg"
    img_path_png = f"images/{roll}.png"
    if os.path.exists(img_path_jpg):
        img_path = img_path_jpg
    elif os.path.exists(img_path_png):
        img_path = img_path_png
    else:
        img_path = None
    
    if img_path:
        img = mpimg.imread(img_path)
        plt.subplot(3, 2, 1)
        plt.imshow(img)
        plt.axis('off')
        plt.title(f"{row['name']} Photo")
    else:
        plt.subplot(3, 2, 1)
        plt.text(0.5, 0.5, 'No Image Found', ha='center', va='center', fontsize=12)
        plt.axis('off')
    
    # Feedback section
    plt.subplot(3,2,6)
    plt.axis('off')
    feedback_text = (
        f"CGPA: {cgpa} - {commentcgpa(cgpa)}\n\n"
        f"Avg Marks: {round(avg_marks, 2)} - {commentmarks(avg_marks)}\n\n"
        f"Attendance: {attendance}% - {commentattendance(attendance)}\n\n"
        f"Behavior: {behavior} - {commentbehavior(behavior)}"
    )
    plt.text(0, 1, feedback_text, fontsize=10, va='top', wrap=True)
    plt.title(f"{row['name']}  Student Feedback Report")
    
    plt.tight_layout()
    
    # Convert to base64
    img_buffer = io.BytesIO()
    plt.savefig(img_buffer, format='png', dpi=100, bbox_inches='tight')
    img_buffer.seek(0)
    plt.close()
    
    img_base64 = base64.b64encode(img_buffer.read()).decode()
    return img_base64

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    roll = data.get('roll')
    
    if not roll:
        return jsonify({'error': 'Roll number required'}), 400
    
    try:
        df = pd.read_csv("bunny.csv")
        row = df[df["roll"] == int(roll)]
        
        if row.empty:
            return jsonify({'error': 'Student not found'}), 404
        
        student_data = {
            'name': row['name'].iloc[0],
            'roll': int(row['roll'].iloc[0]),
            'cgpa': float(row['cgpa'].iloc[0]),
            'attendance': float(row['attendance'].iloc[0])
        }
        
        return jsonify(student_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/student/<int:roll>')
def student_details(roll):
    try:
        df = pd.read_csv("bunny.csv")
        row = df[df["roll"] == roll]
        
        if row.empty:
            return "Student not found", 404
        
        # Generate graph
        graph_base64 = generate_graph_base64(roll, df)
        
        student_info = {
            'name': row['name'].iloc[0],
            'roll': int(row['roll'].iloc[0]),
            'cgpa': float(row['cgpa'].iloc[0]),
            'attendance': float(row['attendance'].iloc[0]),
            'behavior': str(row['behavior_grade'].iloc[0]).upper(),
            'performance': str(row['performance_grade'].iloc[0]).upper()
        }
        
        return render_template('student_details.html', student=student_info, graph=graph_base64)
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/api/student/<int:roll>')
def get_student_data(roll):
    try:
        df = pd.read_csv("bunny.csv")
        row = df[df["roll"] == roll]
        
        if row.empty:
            return jsonify({'error': 'Student not found'}), 404
        
        # Extract all subject marks
        ignore_cols = {"student_id","jun","jul","aug","sep","oct","nov","dec","jan", "feb", "mar",
                       "name","roll","attendance","cgpa","behavior_grade","performance_grade"}
        subject_cols = [c for c in df.columns if c not in ignore_cols]
        
        marks = {sub: float(row[sub].iloc[0]) if pd.notna(row[sub].iloc[0]) else 0 for sub in subject_cols}
        
        # Monthly attendance
        month_columns = ["jun","jul","aug","sep","oct","nov","dec","jan", "feb", "mar"]
        month_attendance = {month: float(row[month].iloc[0]) for month in month_columns}
        
        student_data = {
            'name': str(row['name'].iloc[0]),
            'roll': int(row['roll'].iloc[0]),
            'cgpa': float(row['cgpa'].iloc[0]),
            'attendance': float(row['attendance'].iloc[0]),
            'behavior': str(row['behavior_grade'].iloc[0]).upper(),
            'performance': str(row['performance_grade'].iloc[0]).upper(),
            'marks': marks,
            'monthly_attendance': month_attendance
        }
        
        return jsonify(student_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # For local development
    app.run(debug=True)

