import math
import streamlit as st

# Display an image at the top of the app
st.image(https://github.com/Salman07071978/Insulation-Calculator/blob/main/TM%20Logo.jpg, 
         use_column_width=True, 
         caption="Pipe Insulation Diagram")

# Function to calculate square footage
def calculate_square_ft(pipe_diameter, insulation_thickness, length):
    outer_diameter = pipe_diameter + (2 * insulation_thickness)
    circumference = math.pi * outer_diameter
    square_inch_area = circumference * (length * 12)  # Length converted to inches
    square_ft = square_inch_area / 144  # Convert square inches to square feet
    return square_ft

# Function to calculate running footage
def calculate_running_ft(length):
    return length

# Streamlit App
st.title("Pipe Insulation Calculator 🛠️")

# App Introduction
st.write("""
This calculator estimates the amount of insulation required for various types of pipes, 
including **SS (Stainless Steel)**, **MS (Mild Steel)**, and **Copper**. It calculates 
both the total square footage and the per-foot unit square footage required for insulation.
""")

# Sidebar for pipe information
st.sidebar.header("Pipe Information")
pipe_type = st.sidebar.selectbox("Select Pipe Type:", ["SS", "MS", "Copper"], help="Choose the type of pipe that needs insulation.")
pipe_diameter = st.sidebar.number_input("Enter Pipe Diameter (in inches):", min_value=0.1, help="Diameter of the pipe, measured in inches.")
gauge = st.sidebar.text_input("Enter the Gauge of the Pipe:", help="Provide the pipe's gauge for reference.")
insulation_thickness = st.sidebar.number_input("Enter Insulation Thickness (in inches):", min_value=0.1, help="Specify the thickness of the insulation.")
length = st.sidebar.number_input("Enter Pipe Length (in feet):", min_value=0.1, help="Length of the pipe to be insulated, measured in feet.")

# Button to perform calculation
if st.sidebar.button("Calculate Insulation Requirements"):
    # Perform calculations
    square_ft = calculate_square_ft(pipe_diameter, insulation_thickness, length)
    running_ft = calculate_running_ft(length)
    unit_square_ft = square_ft / length
    unit_square_inch = unit_square_ft * 144  # Convert to square inches per foot

    # Display results
    st.subheader("Insulation Calculation Results 📊")
    
    with st.expander("Detailed Calculation Information"):
        st.write("Below are the calculated values based on the inputs provided:")
        st.write(f"- **Pipe Type**: {pipe_type}")
        st.write(f"- **Pipe Diameter**: {pipe_diameter} inches")
        st.write(f"- **Gauge**: {gauge}")
        st.write(f"- **Insulation Thickness**: {insulation_thickness} inches")
        st.write(f"- **Pipe Length**: {length} feet")
    
    # Results summary
    st.success(f"**Total Square Footage of Insulation Required:** {square_ft:.2f} sq ft")
    st.info(f"**Unit Square Footage of Insulation Required (per foot):** {unit_square_ft:.2f} sq ft/ft")
    st.info(f"**Unit Square Footage of Insulation Required (per foot in inches):** {unit_square_inch:.2f} sq in/ft")
    st.warning(f"**Running Footage of Insulation Required:** {running_ft} ft")
    
    # Additional information
    st.write("---")
    st.write("""
    ### Additional Information:
    - The **total square footage** required indicates the total insulation material needed to cover the entire pipe.
    - **Unit square footage** (sq ft/ft) helps estimate insulation requirements per foot of the pipe.
    - **Unit square footage in inches** (sq in/ft) offers a more detailed view for precise measurements.
    """)

    # Option to reset inputs
    if st.button("Reset Inputs"):
        st.sidebar.selectbox("Select Pipe Type:", ["SS", "MS", "Copper"], index=0)
        st.sidebar.number_input("Enter Pipe Diameter (in inches):", min_value=0.1, value=0.1)
        st.sidebar.text_input("Enter the Gauge of the Pipe:", value="")
        st.sidebar.number_input("Enter Insulation Thickness (in inches):", min_value=0.1, value=0.1)
        st.sidebar.number_input("Enter Pipe Length (in feet):", min_value=0.1, value=0.1)
else:
    st.sidebar.write("👈 Adjust the pipe information in the sidebar and click **Calculate Insulation Requirements** to view the results.")
