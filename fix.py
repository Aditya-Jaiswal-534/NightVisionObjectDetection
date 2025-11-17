import json

def remove_widgets(filenames):
    for file in filenames:
        try:
            with open(file, "r", encoding="utf-8") as f:
                nb = json.load(f)

            # Remove top-level widgets
            if "widgets" in nb.get("metadata", {}):
                del nb["metadata"]["widgets"]

            # Remove widgets in each cell
            for cell in nb.get("cells", []):
                if "metadata" in cell and "widgets" in cell["metadata"]:
                    del cell["metadata"]["widgets"]

            # Save back to the same file
            with open(file, "w", encoding="utf-8") as f:
                json.dump(nb, f, indent=1)
            
            print(f"Removed widgets from notebook: {file}")

        except Exception as e:
            print(f"Error processing {file}: {e}")

# Your notebook filenames
notebook_files = ["final_pix2pix.ipynb", "FinalFastRCNN.ipynb", "FinalFastRCNN.ipynb"]
remove_widgets(notebook_files)
