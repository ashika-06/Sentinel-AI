import streamlit as st
import ipaddress
from dotenv import load_dotenv
import tools

# ===============================
# 1. SETUP & CONFIG
# ===============================
load_dotenv()

st.set_page_config(
    page_title="Sentinel-AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Helper Function: Safety Check ---
def is_safe_ip(ip: str) -> bool:
    """Prevents scanning local/private networks (LAN) which breaks the demo."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private or ip_obj.is_loopback or ip_obj.is_multicast:
            return False
        return True
    except ValueError:
        return False

# ===============================
# 2. HEADER & SIDEBAR
# ===============================
st.title("🛡️ Sentinel-AI: Cyber Defense Node")
st.markdown("**System Status:** 🟢 Passive Reconnaissance Mode (Ethical Compliance Active)")
st.caption("Powered by Llama 3.3 (SambaNova) • Shodan • Tavily")

with st.sidebar:
    st.header("⚙️ Operations")
    st.info("Passive Mode enabled. No active packets sent.")
    
    st.markdown("---")
    st.warning("""
    **⚠️ LEGAL DISCLAIMER**
    This tool utilizes **Passive Reconnaissance** (OSINT). 
    It does not initiate direct network connections to the target. 
    Authorized for educational and defensive use only.
    """)

# ===============================
# 3. TARGET SELECTION (Fixed Dropdown + Manual)
# ===============================
st.subheader("🎯 Target Acquisition")

# Toggle between Sandbox and Manual Entry
mode = st.radio("Select Input Mode:", ["Safe Sandbox Targets", "Manual IP Entry"], horizontal=True)

if mode == "Safe Sandbox Targets":
    target = st.selectbox("Select Authorized Node:", [
        "45.33.32.156 (Scanme Sandbox - Authorized)", 
        "1.1.1.1 (Cloudflare DNS)", 
        "8.8.8.8 (Google DNS)"
    ])
    ip = target.split(" ")[0]

else:
    # Manual Input Logic
    col1, col2 = st.columns([3, 1])
    with col1:
        ip_input = st.text_input("Enter Target IP Address:", placeholder="e.g. 142.250.193.206")
    
    if ip_input:
        ip = ip_input.strip()
        if not is_safe_ip(ip):
            st.error("⚠️ Restricted: Scanning Internal/Private networks (LAN) is disabled.")
            st.stop()
    else:
        ip = None # Wait for input

# ===============================
# 4. MAIN EXECUTION
# ===============================
# Only show button if we have a valid IP
if ip:
    if st.button("🔴 INITIATE INTELLIGENCE SCAN", type="primary"):
        
        # Use a container for the status to keep it organized
        with st.status("🚀 Launching Sentinel Agents...", expanded=True) as status:
            
            # --- PHASE 1: SCAN (Shodan) ---
            st.write("📡 Querying Shodan Satellite Feed...")
            scan_data = tools.scan_target(ip)
            # REMOVED time.sleep(0.5) for speed ⚡
            
            if "error" in scan_data:
                status.update(label="❌ Target Unreachable", state="error")
                st.error(scan_data['error'])
                st.stop()
            
            # --- PHASE 2: RESEARCH (Tavily) ---
            st.write(f"🔎 Detected OS: **{scan_data['os']}**. Deploying Research Agent...")
            exploits = tools.find_exploits(scan_data['os'])
            
            # --- PHASE 3: ANALYZE (Llama 3.3) ---
            st.write("🧠 Aggregating Intelligence for Llama 3.3 Analysis...")
            
            final_prompt = f"""
            Act as a Senior Cyber Defense Analyst.
            TARGET: {scan_data}
            THREATS: {exploits}
            TASK:
            1. Risk Level (Low/Med/High)
            2. Key Risks of open ports (Explain technical impact)
            3. One Mitigation Strategy
            Keep it strictly professional and concise.
            """
            
            report = tools.ask_ai(final_prompt)
            
            status.update(label="✅ Intelligence Gathered", state="complete", expanded=False)

        # --- PHASE 4: DASHBOARD UI ---
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.subheader("📊 Network Telemetry")
            st.metric("Target OS", scan_data['os'])
            st.metric("Open Ports", len(scan_data['ports']))
            st.write("**Detected Ports:**")
            st.json(scan_data['ports'])
            
        with col2:
            st.subheader("📍 Target Triangulation")
            if scan_data.get('lat'):
                st.plotly_chart(
                    tools.draw_map(scan_data['lat'], scan_data['lon']), 
                    use_container_width=True
                )
            else:
                st.warning("Geo-location data unavailable for this target.")
                
        st.markdown("---")
        
        # --- PHASE 5: REPORT & LOGGING ---
        st.subheader("📝 Sentinel Strategic Report")
        st.info(report)
        
        # Log to Supabase (Silent background operation)
        tools.log_scan(ip, report)
        st.toast("✅ Incident Encrypted & Archived")

elif mode == "Manual IP Entry":
    st.info("👋 Enter an IP address above to begin.")