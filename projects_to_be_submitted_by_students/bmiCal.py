import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    st.write("Enter your details below to calculate your BMI.")
    
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
    height = st.number_input("Height (m)", min_value=0.5, step=0.01)
    
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = calculate_bmi(weight, height)
            category = get_bmi_category(bmi)
            st.success(f"Your BMI is {bmi}. You are classified as {category}.")
        else:
            st.error("Please enter valid weight and height values.")

if __name__ == "__main__":
    main()
