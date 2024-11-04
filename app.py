import math
import streamlit as st

# Function to calculate square footage
def calculate_square_ft(pipe_diameter, insulation_thickness, length):
    # Calculate the outer diameter by adding the insulation thickness to both sides
    outer_diameter = pipe_diameter + (2 * insulation_thickness)
    
    # Calculate the circumference in inches
    circumference = math.pi * outer_diameter
    
    # Total surface area (in square inches) covered by insulation, then convert to square feet
    square_inch_area = circumference * (length * 12)  # Length converted to inches
    square_ft = square_inch_area / 144  # Convert square inches to square feet
    
    return square_ft

# Function to calculate running footage
def calculate_running_ft(length):
    return length

# Streamlit App
st.title("Pipe Insulation Calculator")

st.write("This calculator helps to calculate the square footage and running footage required for pipe insulation based on pipe specifications.")

# Input fields
pipe_type = st.selectbox("Select Pipe Type", ["SS", "MS", "Copper"])
pipe_diameter = st.number_input("Enter the Pipe Diameter (in inches):", min_value=0.1)
gauge = st.text_input("Enter the Gauge of the Pipe:")
insulation_thickness = st.number_input("Enter the Insulation Thickness (in inches):", min_value=0.1)
length = st.number_input("Enter the Length of the Pipe (in feet):", min_value=0.1)

# Calculate button
if st.button("Calculate"):
    # Calculate square footage and running footage
    square_ft = calculate_square_ft(pipe_diameter, insulation_thickness, length)
    running_ft = calculate_running_ft(length)
    
    # Calculate unit square footage per foot in both square feet and square inches
    unit_square_ft = square_ft / length
    unit_square_inch = unit_square_ft * 144  # Convert square feet to square inches for per foot

    # Display results
    st.subheader("Insulation Calculation Results")
    st.write(f"**Pipe Type**: {pipe_type}")
    st.write(f"**Pipe Diameter**: {pipe_diameter} inches")
    st.write(f"**Gauge**: {gauge}")
    st.write(f"**Insulation Thickness**: {insulation_thickness} inches")
    st.write(f"**Pipe Length**: {length} feet")
    st.write(f"**Total Square Footage of Insulation Required**: {square_ft:.2f} sq ft")
    st.write(f"**Unit Square Footage of Insulation Required (per foot)**: {unit_square_ft:.2f} sq ft/ft")
    st.write(f"**Unit Square Footage of Insulation Required (per foot in inches)**: {unit_square_inch:.2f} sq in/ft")
    st.write(f"**Running Footage of Insulation Required**: {running_ft} ft")
