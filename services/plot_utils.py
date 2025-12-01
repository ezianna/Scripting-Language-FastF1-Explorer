import plotly.graph_objects as go

def plot_telemetry(tel):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=tel['Distance'], y=tel['Speed'], mode='lines', name='Speed'))
    fig.update_layout(title="Telemetry Speed", xaxis_title="Distance (m)", yaxis_title="Speed (km/h)")
    return fig.to_html(full_html=False)

def plot_compare(A, B, driver_a, driver_b):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=A['Distance'], y=A['Speed'], name=f"{driver_a} Speed"))
    fig.add_trace(go.Scatter(x=B['Distance'], y=B['Speed'], name=f"{driver_b} Speed"))

    fig.update_layout(title="Driver Telemetry Comparison", xaxis_title="Distance (m)", yaxis_title="Speed (km/h)")
    return fig.to_html(full_html=False)
