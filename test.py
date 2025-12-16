import kagglehub

# Download latest version
path = kagglehub.dataset_download("krzysztofjamroz/apartment-prices-in-poland")

print("Path to dataset files:", path)