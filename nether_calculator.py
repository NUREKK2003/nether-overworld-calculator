import streamlit as st

def calculate_coordinates(x, z, mode):
    if mode == "Overworld to Nether":
        return x / 8, z / 8
    elif mode == "Nether to Overworld":
        return x * 8, z * 8
    return x, z

st.title("Nether & Overworld Coordinates Calculator")

mode = st.radio("Select conversion mode:", ["Overworld to Nether", "Nether to Overworld"])

x = st.number_input(f"Enter {mode.split()[0]} X coordinate", value=0.0, format="%.2f",step=1.0)
z = st.number_input(f"Enter {mode.split()[0]} Z coordinate", value=0.0, format="%.2f",step=1.0)

x_converted, z_converted = calculate_coordinates(x, z, mode)

if abs(x_converted) > 30000000 or abs(z_converted) > 30000000:
    st.error("Coordinates exceed world border (±30,000,000)!")
else:
    st.write(f"Converted {mode.split()[0]} X Coordinate: {x_converted:.6f}")
    st.write(f"Converted {mode.split()[0]} Z Coordinate: {z_converted:.6f}")
