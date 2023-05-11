"""
# st_app.py

Creates a Streamlit app for visualizing the data generated from the Frequency Response simulations.
"""
import re
import zipfile
import numpy as np
import pandas as pd
import streamlit as st
from io import BytesIO
import matplotlib as mpl
import matplotlib.pyplot as plt

from util import *
from st_plotting import *


st.set_page_config(
    layout     = "centered",
    page_icon  = "📊",
    page_title = "Frequency Response Data"
)
st.markdown(body=\
    """ <style>
    section.main > div {max-width:75rem}
    </style> """, unsafe_allow_html=True
)

def descriptions_as_dict(data_type_axis_description: NamedTuple) -> dict:
    """
    """
    return {
        "DIMM1": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM1], axis=1).set_index(""),
        "DIMM2": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM2], axis=1).set_index(""),
        "DIMM3": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM3], axis=1).set_index(""),
        "DIMM4": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM4], axis=1).set_index(""),
        "DIMM5": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM5], axis=1).set_index(""),
        "DIMM6": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM6], axis=1).set_index(""),
        "DIMM7": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM7], axis=1).set_index(""),
        "DIMM8": pd.concat([pd.DataFrame({"": ["mean", "std", "min", "25%", "50%", "75%", "max"]}), data_type_axis_description.DIMM8], axis=1).set_index(""),
    }

if 'chart' not in st.session_state:
    st.session_state.chart = None
if 'data' not in st.session_state:
    st.session_state.data = None

if 'charts' not in st.session_state:
    st.session_state.charts = {
        "sim6": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim7": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim8": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim9": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim10": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim11": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
        "sim12": {
            "all": {
                "line": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
                "bar": {
                    "velocity": {"x": None,"y": None,"z": None,"all": None,},
                    "deformation": {"x": None,"y": None,"z": None,"all": None,},
                    "acceleration": {"x": None,"y": None,"z": None,"all": None,},
                },
            },
        },
    }



st.title("Simulation Results")
# st.markdown("---")
st.markdown("# ")


# Sidebar
st.sidebar.title("Options")

st.sidebar.markdown("---")
st.sidebar.markdown("# Simulation Data")
st.sidebar.write(" ")
sim_folder = st.sidebar.selectbox("Dataset", options=["sim6", "sim7", "sim8", "sim9", "sim10", "sim11", "sim12", "sim13", "sim14", "sim15", "sim16", "sim17"], index=6, key="sim_folder", help="Select the dataset to use for plotting")
st.sidebar.markdown("---")

st.sidebar.markdown("# Plotting")
st.sidebar.write(" ")
plot_type = st.sidebar.selectbox("Plot Type", options=["all", "single"], index=0, key="plot_type", help="Plot data for all DIMMs or just a single DIMM")
if plot_type == "all":
    dimm_number = st.sidebar.selectbox("DIMM Number", options=[1, 2, 3, 4, 5, 6, 7, 8], index=0, disabled=True, key="dimm_number", help="DIMM number to plot")
    chart_type = st.sidebar.selectbox("Chart Type", options=["bar", "line"], index=0, help="Type of chart to use for plotting")
else:
    dimm_number = st.sidebar.selectbox("DIMM Number", options=[1, 2, 3, 4, 5, 6, 7, 8], index=0, key="dimm_number", help="DIMM number to plot")
    chart_type = st.sidebar.selectbox("Chart Type", options=["line"], index=0, help="Type of chart to use for plotting")
if plot_type == "single":
    chart_type = "line"
data_type = st.sidebar.selectbox("Data Type", options=["velocity", "acceleration", "deformation"], index=1, key="data_type", help="Type of data to plot")
if chart_type == "line":
    axis = st.sidebar.selectbox("Axis", options=["x", "y", "z", "all"], index=2, key="axis", help="Axis of the data to plot")
else:
    axis = st.sidebar.selectbox("Axis", options=["x", "y", "z"], index=2, key="axis", help="Axis of the data to plot")
st.sidebar.markdown("# Parameters")
st.sidebar.write(" ")
fill = st.sidebar.checkbox("Fill", value=True, key="fill", help="Fill the area under the curve")
markers = st.sidebar.checkbox("Markers", value=True, key="markers", help="Show markers at the data points")
st.sidebar.write(" ")
marker_size = st.sidebar.slider("Marker Size", min_value=1.0, max_value=5.0, value=3.5, step=0.5, key="marker_size", help="Size of the markers, if enabled")
st.sidebar.write(" ")
locate_modal_freq_with = st.sidebar.selectbox("Modal Frequency Locations", options=["Lines", "Markers"], index=0, key="locate_modal_freq_with", help="Mark the modal frequencies with lines or markers")
plot_parameters = dict(fill=fill, markers=markers, locate_modal_freq_with=locate_modal_freq_with, marker_size=marker_size)
st.sidebar.markdown("---")

st.sidebar.header("About")
st.sidebar.info(body=\
    """
    - sim6:  Clip method, acceleration applied in z-direction.
    - sim7:  Clip method, acceleration applied in x-direction.
    - sim8:  Clip method, acceleration applied in y-direction.
    
    - sim9:  Edge-on, acceleration applied in z-direction.
    - sim10: Edge-on, acceleration applied in y-direction.
    - sim11: Edge-on, acceleration applied in x-direction.
    
    - sim12: Screw method, base-excitation applied in z-direction.
    - sim13: Screw method, base-excitation applied in y-direction.
    - sim14: Screw method, base-excitation applied in x-direction.
    
    - sim15: Screw method, forces applied in z-direction.
    - sim16: Screw method, forces applied in y-direction.
    - sim17: Screw method, forces applied in x-direction.
    """
)





# Load the data from the selected simulation folder
velocity_data = get_velocity_data(sim_folder)
acceleration_data = get_acceleration_data(sim_folder)
deformation_data = get_deformation_data(sim_folder)

modal_freq = get_modal_frequencies(sim_folder)
plot_parameters['modal_freq'] = modal_freq
plot_parameters['locate_modal_freq_with'] = plot_parameters['locate_modal_freq_with'].lower()

all_data = {
    "velocity": {
        "x": velocity_data.x,
        "y": velocity_data.y,
        "z": velocity_data.z,
        "1": {
            "x": velocity_data.x.DIMM1,
            "y": velocity_data.y.DIMM1,
            "z": velocity_data.z.DIMM1,
        },
        "2": {
            "x": velocity_data.x.DIMM2,
            "y": velocity_data.y.DIMM2,
            "z": velocity_data.z.DIMM2,
        },
        "3": {
            "x": velocity_data.x.DIMM3,
            "y": velocity_data.y.DIMM3,
            "z": velocity_data.z.DIMM3,
        },
        "4": {
            "x": velocity_data.x.DIMM4,
            "y": velocity_data.y.DIMM4,
            "z": velocity_data.z.DIMM4,
        },
        "5": {
            "x": velocity_data.x.DIMM5,
            "y": velocity_data.y.DIMM5,
            "z": velocity_data.z.DIMM5,
        },
        "6": {
            "x": velocity_data.x.DIMM6,
            "y": velocity_data.y.DIMM6,
            "z": velocity_data.z.DIMM6,
        },
        "7": {
            "x": velocity_data.x.DIMM7,
            "y": velocity_data.y.DIMM7,
            "z": velocity_data.z.DIMM7,
        },
        "8": {
            "x": velocity_data.x.DIMM8,
            "y": velocity_data.y.DIMM8,
            "z": velocity_data.z.DIMM8,
        },
    },
    "deformation": {
        "x": deformation_data.x,
        "y": deformation_data.y,
        "z": deformation_data.z,
        "1": {
            "x": deformation_data.x.DIMM1,
            "y": deformation_data.y.DIMM1,
            "z": deformation_data.z.DIMM1,
        },
        "2": {
            "x": deformation_data.x.DIMM2,
            "y": deformation_data.y.DIMM2,
            "z": deformation_data.z.DIMM2,
        },
        "3": {
            "x": deformation_data.x.DIMM3,
            "y": deformation_data.y.DIMM3,
            "z": deformation_data.z.DIMM3,
        },
        "4": {
            "x": deformation_data.x.DIMM4,
            "y": deformation_data.y.DIMM4,
            "z": deformation_data.z.DIMM4,
        },
        "5": {
            "x": deformation_data.x.DIMM5,
            "y": deformation_data.y.DIMM5,
            "z": deformation_data.z.DIMM5,
        },
        "6": {
            "x": deformation_data.x.DIMM6,
            "y": deformation_data.y.DIMM6,
            "z": deformation_data.z.DIMM6,
        },
        "7": {
            "x": deformation_data.x.DIMM7,
            "y": deformation_data.y.DIMM7,
            "z": deformation_data.z.DIMM7,
        },
        "8": {
            "x": deformation_data.x.DIMM8,
            "y": deformation_data.y.DIMM8,
            "z": deformation_data.z.DIMM8,
        },
    },
    "acceleration": {
        "x": acceleration_data.x,
        "y": acceleration_data.y,
        "z": acceleration_data.z,
        "1": {
            "x": acceleration_data.x.DIMM1,
            "y": acceleration_data.y.DIMM1,
            "z": acceleration_data.z.DIMM1,
        },
        "2": {
            "x": acceleration_data.x.DIMM2,
            "y": acceleration_data.y.DIMM2,
            "z": acceleration_data.z.DIMM2,
        },
        "3": {
            "x": acceleration_data.x.DIMM3,
            "y": acceleration_data.y.DIMM3,
            "z": acceleration_data.z.DIMM3,
        },
        "4": {
            "x": acceleration_data.x.DIMM4,
            "y": acceleration_data.y.DIMM4,
            "z": acceleration_data.z.DIMM4,
        },
        "5": {
            "x": acceleration_data.x.DIMM5,
            "y": acceleration_data.y.DIMM5,
            "z": acceleration_data.z.DIMM5,
        },
        "6": {
            "x": acceleration_data.x.DIMM6,
            "y": acceleration_data.y.DIMM6,
            "z": acceleration_data.z.DIMM6,
        },
        "7": {
            "x": acceleration_data.x.DIMM7,
            "y": acceleration_data.y.DIMM7,
            "z": acceleration_data.z.DIMM7,
        },
        "8": {
            "x": acceleration_data.x.DIMM8,
            "y": acceleration_data.y.DIMM8,
            "z": acceleration_data.z.DIMM8,
        },
    },
}


chart_tab, data_tab, file_upload_tab = st.tabs(["Chart", "Data", "File Upload"])



with chart_tab:
    # Plot the data
    if plot_type == "all":
        if chart_type == "line":
            if axis == "all":
                # if st.session_state.charts[sim_folder]["all"]["line"][data_type][axis] is None:
                #     st.session_state.charts[sim_folder]["all"]["line"][data_type][axis] = subplot_amplitudes_xyz_linear({'velocity': velocity_data, 'deformation': deformation_data, 'acceleration': acceleration_data}[data_type], data_type, **plot_parameters)
                # st.session_state.chart = st.session_state.charts[sim_folder]["all"]["line"][data_type][axis]
                st.session_state.chart = subplot_amplitudes_xyz_linear({'velocity': velocity_data, 'deformation': deformation_data, 'acceleration': acceleration_data}[data_type], data_type, **plot_parameters)
            else:
                st.session_state.chart = subplot_amplitudes_linear(all_data[data_type][axis], data_type, axis, **plot_parameters)
        elif chart_type == "bar":
            st.session_state.chart = plot_peak_amplitudes(all_data[data_type][axis], data_type, axis)

    elif plot_type == "single":
        if chart_type == "line":
            if axis == "all":
                st.session_state.chart = plot_amplitude_xyz_linear({'velocity': velocity_data, 'deformation': deformation_data, 'acceleration': acceleration_data}[data_type], data_type, dimm_number, **plot_parameters)
            else:
                st.session_state.chart = plot_amplitude_linear(all_data[data_type][str(dimm_number)][axis], data_type, axis, dimm_number, locate_peaks=True, **plot_parameters)

    if st.session_state.chart is not None:
        st.pyplot(st.session_state.chart)
        st.markdown("---")






with data_tab:
    if axis != "all":
        try:
            # Show the data
            st.session_state.data = all_data[data_type][axis]
            if data_type in ['velocity', 'deformation']:
                description = load_dfs_from_description__velocity_deformation(f"{sim_folder}/data/{data_type}_{axis}_description.txt")
            elif data_type == 'acceleration':
                description = load_dfs_from_description__acceleration(f"{sim_folder}/data/{data_type}_{axis}_description.txt")

            with st.expander("Raw Data"):
                col1, col2 = st.columns(2, gap="large")
                with col1:
                    # create a label for the data (DIMM1, DIMM2, etc.) that is centered in the column
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM1</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM1, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM3</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM3, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM5</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM5, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM7</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM7, use_container_width=True)
                with col2:
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM2</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM2, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM4</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM4, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM6</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM6, use_container_width=True)
                    st.markdown("<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM8</p>", unsafe_allow_html=True)
                    st.dataframe(st.session_state.data.DIMM8, use_container_width=True)
            
            with st.expander("Data Description"):
                col1, col2 = st.columns(2, gap="large")
                descriptions = descriptions_as_dict(description)
                with col1:
                    for i in range(1, 8, 2):
                        st.markdown(f"<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM{i}</p>", unsafe_allow_html=True)
                        st.dataframe(descriptions[f"DIMM{i}"], use_container_width=True)
                with col2:
                    for i in range(2, 9, 2):
                        st.markdown(f"<p style='text-align: center; font-size: 1.7rem; font-weight: bold;'>DIMM{i}</p>", unsafe_allow_html=True)
                        st.dataframe(descriptions[f"DIMM{i}"], use_container_width=True)
        except:
            pass




with file_upload_tab:
    # modes_ = []
    velocity_files_x = []
    velocity_files_y = []
    velocity_files_z = []
    deformation_files_x = []
    deformation_files_y = []
    deformation_files_z = []
    acceleration_files_x = []
    acceleration_files_y = []
    acceleration_files_z = []
    file = st.file_uploader("Upload a file", type=["zip"])
    if file is not None:
        with st.spinner("Loading..."):
            with zipfile.ZipFile(file) as zf:
                for file_info in zf.infolist():
                    if 'modes' in file_info.filename and file_info.filename.endswith('.txt'):
                        modes_ = []
                        with zf.open(file_info, 'r') as file:
                            for line in file:
                                if line.startswith(b'#'):
                                    continue
                                else:
                                    modes_.append(line.decode('utf-8').strip())
                            
                    if 'data/acceleration' in file_info.filename and file_info.filename.endswith('.txt'):
                        base_folder = file_info.filename.split('/')[0]
                        if 'x.txt' in file_info.filename:
                            acceleration_files_x.append(file_info.filename)
                        elif 'y.txt' in file_info.filename:
                            acceleration_files_y.append(file_info.filename)
                        elif 'z.txt' in file_info.filename:
                            acceleration_files_z.append(file_info.filename)
                    elif 'data/deformation' in file_info.filename and file_info.filename.endswith('.txt'):
                        if 'x.txt' in file_info.filename:
                            deformation_files_x.append(file_info.filename)
                        elif 'y.txt' in file_info.filename:
                            deformation_files_y.append(file_info.filename)
                        elif 'z.txt' in file_info.filename:
                            deformation_files_z.append(file_info.filename)
                    elif 'data/velocity' in file_info.filename and file_info.filename.endswith('.txt'):
                        if 'x.txt' in file_info.filename:
                            velocity_files_x.append(file_info.filename)
                        elif 'y.txt' in file_info.filename:
                            velocity_files_y.append(file_info.filename)
                        elif 'z.txt' in file_info.filename:
                            velocity_files_z.append(file_info.filename)

                velocity_dataframes_x = []
                velocity_dataframes_y = []
                velocity_dataframes_z = []
                deformation_dataframes_x = []
                deformation_dataframes_y = []
                deformation_dataframes_z = []
                acceleration_dataframes_x = []
                acceleration_dataframes_y = []
                acceleration_dataframes_z = []

                for f in velocity_files_x:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    velocity_dataframes_x.append(df)
                for f in velocity_files_y:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    velocity_dataframes_y.append(df)
                for f in velocity_files_z:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    velocity_dataframes_z.append(df)

                Velocity_Data = namedtuple("Velocity_Data", ["x", "y", "z"])
                Velocity_Data_x = namedtuple("Velocity_Data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Velocity_Data_y = namedtuple("Velocity_Data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Velocity_Data_z = namedtuple("Velocity_Data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                vel_data = Velocity_Data(Velocity_Data_x(*velocity_dataframes_x), Velocity_Data_y(*velocity_dataframes_y), Velocity_Data_z(*velocity_dataframes_z))

                for f in deformation_files_x:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df['Amplitude'] *= 1e3
                    deformation_dataframes_x.append(df)
                for f in deformation_files_y:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df['Amplitude'] *= 1e3
                    deformation_dataframes_y.append(df)
                for f in deformation_files_z:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df['Amplitude'] *= 1e3
                    deformation_dataframes_z.append(df)

                Deformation_Data = namedtuple("Deformation_Data", ["x", "y", "z"])
                Deformation_Data_x = namedtuple("Deformation_Data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Deformation_Data_y = namedtuple("Deformation_Data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Deformation_Data_z = namedtuple("Deformation_Data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                defo_data = Deformation_Data(Deformation_Data_x(*deformation_dataframes_x), Deformation_Data_y(*deformation_dataframes_y), Deformation_Data_z(*deformation_dataframes_z))
                

                for f in acceleration_files_x:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
                    acceleration_dataframes_x.append(df)
                for f in acceleration_files_y:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
                    acceleration_dataframes_y.append(df)
                for f in acceleration_files_z:
                    df = pd.read_csv(f, sep=r'\s+', skiprows=1, names=['Frequency', 'Amplitude', 'Phase Angle'])
                    df.insert(1, 'Amplitude_g', df['Amplitude'] / 9.81)
                    acceleration_dataframes_z.append(df)
                    
                Acceleration_Data = namedtuple("Acceleration_Data", ["x", "y", "z"])
                Acceleration_Data_x = namedtuple("Acceleration_Data_x", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Acceleration_Data_y = namedtuple("Acceleration_Data_y", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                Acceleration_Data_z = namedtuple("Acceleration_Data_z", ["DIMM1", "DIMM2", "DIMM3", "DIMM4", "DIMM5", "DIMM6", "DIMM7", "DIMM8"])
                accel_data = Acceleration_Data(Acceleration_Data_x(*acceleration_dataframes_x), Acceleration_Data_y(*acceleration_dataframes_y), Acceleration_Data_z(*acceleration_dataframes_z))
                

                new_modes = []
                for i in range(len(modes_)):
                    if i > 0:
                        if i < 10:
                            new_modes.append(float(modes_[i][2:]))
                        else:
                            new_modes.append(float(modes_[i][3:]))

                plot_parameters['modal_freq'] = new_modes

                def get_image(fig_):
                    savefig = BytesIO()
                    fig_.savefig(savefig, format='png', dpi=420)
                    savefig.seek(0)
                    return savefig

                # generate plot from the uploaded data
                figs = [
                    plot_peak_amplitudes(velocity_data.x, 'velocity', 'x'),
                    plot_peak_amplitudes(velocity_data.y, 'velocity', 'y'),
                    plot_peak_amplitudes(velocity_data.z, 'velocity', 'z'),
                    plot_peak_amplitudes(deformation_data.x, 'deformation', 'x'),
                    plot_peak_amplitudes(deformation_data.y, 'deformation', 'y'),
                    plot_peak_amplitudes(deformation_data.z, 'deformation', 'z'),
                    plot_peak_amplitudes(acceleration_data.x, 'acceleration', 'x'),
                    plot_peak_amplitudes(acceleration_data.y, 'acceleration', 'y'),
                    plot_peak_amplitudes(acceleration_data.z, 'acceleration', 'z'),
                    subplot_amplitudes_linear(velocity_data.x, 'velocity', 'x', **plot_parameters),
                    subplot_amplitudes_linear(velocity_data.y, 'velocity', 'y', **plot_parameters),
                    subplot_amplitudes_linear(velocity_data.z, 'velocity', 'z', **plot_parameters),
                    subplot_amplitudes_linear(deformation_data.x, 'deformation', 'x', **plot_parameters),
                    subplot_amplitudes_linear(deformation_data.y, 'deformation', 'y', **plot_parameters),
                    subplot_amplitudes_linear(deformation_data.z, 'deformation', 'z', **plot_parameters),
                    subplot_amplitudes_linear(acceleration_data.x, 'acceleration', 'x', **plot_parameters),
                    subplot_amplitudes_linear(acceleration_data.y, 'acceleration', 'y', **plot_parameters),
                    subplot_amplitudes_linear(acceleration_data.z, 'acceleration', 'z', **plot_parameters),
                    subplot_amplitudes_xyz_linear(velocity_data, 'velocity', **plot_parameters),
                    subplot_amplitudes_xyz_linear(deformation_data, 'deformation', **plot_parameters),
                    subplot_amplitudes_xyz_linear(acceleration_data, 'acceleration', **plot_parameters),
                    subplot_amplitudes(velocity_data.x, 'velocity', 'x', **plot_parameters),
                    subplot_amplitudes(velocity_data.y, 'velocity', 'y', **plot_parameters),
                    subplot_amplitudes(velocity_data.z, 'velocity', 'z', **plot_parameters),
                    subplot_amplitudes(deformation_data.x, 'deformation', 'x', **plot_parameters),
                    subplot_amplitudes(deformation_data.y, 'deformation', 'y', **plot_parameters),
                    subplot_amplitudes(deformation_data.z, 'deformation', 'z', **plot_parameters),
                    subplot_amplitudes(acceleration_data.x, 'acceleration', 'x', **plot_parameters),
                    subplot_amplitudes(acceleration_data.y, 'acceleration', 'y', **plot_parameters),
                    subplot_amplitudes(acceleration_data.z, 'acceleration', 'z', **plot_parameters),
                ]
                filenames = [
                    "plots/velocity/bar/velocity_x_peaks.png",
                    "plots/velocity/bar/velocity_y_peaks.png",
                    "plots/velocity/bar/velocity_z_peaks.png",
                    "plots/deformation/bar/deformation_x_peaks.png",
                    "plots/deformation/bar/deformation_y_peaks.png",
                    "plots/deformation/bar/deformation_z_peaks.png",
                    "plots/acceleration/bar/acceleration_x_peaks.png",
                    "plots/acceleration/bar/acceleration_y_peaks.png",
                    "plots/acceleration/bar/acceleration_z_peaks.png",
                    "plots/velocity/subplots/linear/velocity_x.png",
                    "plots/velocity/subplots/linear/velocity_y.png",
                    "plots/velocity/subplots/linear/velocity_z.png",
                    "plots/deformation/subplots/linear/deformation_x.png",
                    "plots/deformation/subplots/linear/deformation_y.png",
                    "plots/deformation/subplots/linear/deformation_z.png",
                    "plots/acceleration/subplots/linear/acceleration_x.png",
                    "plots/acceleration/subplots/linear/acceleration_y.png",
                    "plots/acceleration/subplots/linear/acceleration_z.png",
                    "plots/velocity/subplots/linear/velocityXYZ.png",
                    "plots/deformation/subplots/linear/deformationXYZ.png",
                    "plots/acceleration/subplots/linear/accelerationXYZ.png",
                    "plots/velocity/subplots/log/velocity_x.png",
                    "plots/velocity/subplots/log/velocity_y.png",
                    "plots/velocity/subplots/log/velocity_z.png",
                    "plots/deformation/subplots/log/deformation_x.png",
                    "plots/deformation/subplots/log/deformation_y.png",
                    "plots/deformation/subplots/log/deformation_z.png",
                    "plots/acceleration/subplots/log/acceleration_x.png",
                    "plots/acceleration/subplots/log/acceleration_y.png",
                    "plots/acceleration/subplots/log/acceleration_z.png",
                    "plots/velocity/subplots/log/velocityXYZ.png",
                    "plots/deformation/subplots/log/deformationXYZ.png",
                    "plots/acceleration/subplots/log/accelerationXYZ.png",
                ]

                buffers = []
                for fig, filename in zip(figs, filenames):
                    buffers.append({'filename': filename, 'buffer': get_image(fig)})

                zip_buffer = BytesIO()
                with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
                    for entry in buffers:
                        entry['buffer'].seek(0)
                        zf.writestr(entry['filename'], entry['buffer'].read())
                zip_buffer.seek(0)

        st.download_button(
            label="Download Plots",
            data=zip_buffer,
            file_name=f"plots.zip",
            mime="application/zip",
        )





# st.markdown("---")
st.markdown(body=\
    """ <style>
    footer {visibility:hidden}
    </style> """, unsafe_allow_html=True
)

