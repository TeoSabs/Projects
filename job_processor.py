import pandas as pd
from datetime import datetime

# Sample data from the provided 10 jobs
jobs = [
    {
        "Job Title": "Personal Assistant to CEO",
        "Company Name": "Southsea Investments Pvt Ltd",
        "Description": "An exciting opportunity has arisen for suitably qualified and self-driven individuals in a leading diversified conglomerate for the position of Personal Assistant (PA to CEO). The successful candidate will be responsible for driving business performance through providing administrative and secretarial support to the CEO.",
        "Location": "Harare",
        "Expiration Date": "Expires 24 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 18 hours"
    },
    {
        "Job Title": "Supply Chain Attachee (Mutare Branch)",
        "Company Name": "Nash Paints",
        "Description": "Nash Paints is looking for a Procurement, Purchasing and Supply Chains Management Attachee to join their organization.",
        "Location": "Mutare",
        "Expiration Date": "Expires 14 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 18 hours"
    },
    {
        "Job Title": "Sales Champion - Solar Project",
        "Company Name": "Nash Furnishers",
        "Description": "We are seeking a highly motivated and experienced Sales Champion to lead our solar project. The successful candidate will be responsible for driving sales growth, building relationships with key customers, and identifying new business opportunities in the solar industry.",
        "Location": "Harare",
        "Expiration Date": "Expires 21 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 20 hours"
    },
    {
        "Job Title": "Electrician Class 1",
        "Company Name": "Zimasco (Pvt) Limited",
        "Description": "Zimasco (Pvt) Limited, a major player in Zimbabwe’s Ferrochrome Production sector, has some exciting and challenging career opportunities at its Shurugwi & South Dyke Division.",
        "Location": "Shurugwi",
        "Expiration Date": "Expires 22 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 23 hours"
    },
    {
        "Job Title": "Inventory Controller",
        "Company Name": "Zimasco (Pvt) Limited",
        "Description": "Zimasco (Pvt) Limited, a major player in Zimbabwe’s Ferrochrome Production sector, has some exciting and challenging career opportunities at its Shurugwi & South Dyke Division.",
        "Location": "Harare",
        "Expiration Date": "Expires 22 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 23 hours"
    },
    {
        "Job Title": "Chief Geologist",
        "Company Name": "Zimasco (Pvt) Limited",
        "Description": "Zimasco (Pvt) Limited, a major player in Zimbabwe’s Ferrochrome sector, has an exciting and challenging career opportunity within its Shurugwi & South Dyke Mining Division.",
        "Location": "Shurugwi",
        "Expiration Date": "Expires 21 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 2 days, 23 hours"
    },
    {
        "Job Title": "GIK & Stores Graduate Intern, World Vision Zimbabwe",
        "Company Name": "World Vision",
        "Description": "World Vision Zimbabwe is seeking a highly motivated and detail-oriented Graduate Intern to support our Gifts-in-Kind (GIK) and Stores operations.",
        "Location": "Harare",
        "Expiration Date": "Expires 19 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 3 days, 12 hours"
    },
    {
        "Job Title": "Graduate Intern - People & Culture, World Vision Zimbabwe",
        "Company Name": "World Vision",
        "Description": "World Vision Zimbabwe is seeking a passionate and detail-oriented Graduate Intern - People & Culture to support HR operations across grants and program areas.",
        "Location": "Bulawayo",
        "Expiration Date": "Expires 19 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 3 days, 12 hours"
    },
    {
        "Job Title": "Machine Operator",
        "Company Name": "Isteel and Pump Solutions",
        "Description": "1. Setting up and adjusting machines for production runs. 2. Ensuring machines are functioning accurately and efficiently. 3. Monitoring machines during operations to detect any malfunctions or irregularities. 4. Performing routine maintenance and minor repairs to keep machinery in optimal condition.",
        "Location": "Harare",
        "Expiration Date": "Expires 18 Apr 2025",
        "Job Type": "Full Time",
        "Posted Time": "Posted 3 days, 17 hours"
    }
]

# Save data to CSV and print job details in terminal
def save_to_csv_and_print(jobs, filename="job_listings.csv"):
    try:
        # Save data to a timestamped file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename_with_timestamp = f"{filename.split('.csv')[0]}_{timestamp}.csv"
        df = pd.DataFrame(jobs)

        # Ensure proper cell alignment by cleaning text
        for col in df.columns:
            df[col] = df[col].apply(lambda x: str(x).strip())

        # Save the file
        df.to_csv(filename_with_timestamp, index=False)
        print(f"\nData saved to {filename_with_timestamp}\n")

        # Print job details in terminal
        for i, job in enumerate(jobs, 1):
            print(f"Job {i}:")
            print(f"Job Title: {job['Job Title']}")
            print(f"Company Name: {job['Company Name']}")
            print(f"Description: {job['Description']}")
            print(f"Location: {job['Location']}")
            print(f"Expiration Date: {job['Expiration Date']}")
            print(f"Job Type: {job['Job Type']}")
            print(f"Salary: {job.get('Salary', 'N/A')}")
            print(f"Posted Time: {job['Posted Time']}")
            print("\n" + "-"*50 + "\n")  # Adds a separator between jobs
    except Exception as e:
        print(f"Error saving data or printing jobs: {e}")

# Main script execution
if __name__ == "__main__":
    print("Processing job data...\n")
    save_to_csv_and_print(jobs)