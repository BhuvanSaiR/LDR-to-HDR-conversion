import streamlit as st
import subprocess
from pathlib import Path
import time

def main():
    st.title("LDR to HDR Converter")
    st.write("Drag and drop a .jpg file to convert it to .hdr format.")

    # File uploader for drag-and-drop
    uploaded_file = st.file_uploader("Choose a LDR file", type="jpg")

    if uploaded_file is not None:
        # Display the uploaded file
        st.image(uploaded_file, caption="Uploaded LDR image.", use_container_width=True)
        
        # Save the uploaded file to a unique temporary location
        temp_filename = f"temp_{int(time.time())}.jpg"  # Unique filename based on timestamp
        input_path = Path(temp_filename)
        with open(input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Call the conversion script on the uploaded file
        conversion_command = ["python", "conversion.py", str(input_path)]
        
        # Run the conversion command and capture output
        st.write("Converting image...")
        result = subprocess.run(conversion_command, capture_output=True, text=True)

        # Display any output from the conversion script
        if result.stdout:
            st.write("Conversion output:", result.stdout)
        
        # Display errors only if there is an error
        if result.stderr:
            st.error("Conversion errors:")
            st.write(result.stderr)

        # Look for any .hdr file in the directory
        output_files = list(Path.cwd().glob("*.hdr"))
        
        if output_files:
            output_path = output_files[0]  # Use the first .hdr file found
            st.success("Conversion complete! Here is your .hdr file:")
            st.download_button(
                label="Download .hdr file",
                data=output_path.read_bytes(),
                file_name=output_path.name,
                mime="application/octet-stream"
            )
            
            # Clean up temporary files
            input_path.unlink()  # Delete the temp.jpg file
            output_path.unlink()  # Delete the output .hdr file after download
        else:
            st.error("Conversion failed. No .hdr file found.")

if __name__ == "__main__":
    main()
