from backend import gemini

report_value = ""
medic_rep_lis = []
def report_card(answer_prompt, bmi, health_advice, steps, calorie):
    global report_value
    global medic_rep_lis
    report_value += answer_prompt
    medic_rep_lis.append(report_value)
    medic_rep_lis.append(bmi)
    medic_rep_lis.append(health_advice)
    medic_rep_lis.append(steps)
    medic_rep_lis.append(calorie)
print("Report_value from backend : "+report_value)
def send_report():
    return medic_rep_lis