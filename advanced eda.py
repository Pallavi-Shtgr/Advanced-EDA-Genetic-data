# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


gtf_data = {
    "Chromosome": ["chr1", "chr1", "chr2", "chr2", "chr3"],
    "Source": ["ensembl"] * 5,
    "Feature": ["gene", "exon", "gene", "exon", "intron"],
    "Start": [1000, 1500, 2000, 2500, 3000],
    "End": [2000, 1800, 3000, 2800, 4000],
    "Score": ["."] * 5,
    "Strand": ["+"] * 5,
    "Frame": ["."] * 5,
    "Attributes": ["gene_id 'G1';", "gene_id 'G1';", "gene_id 'G2';", "gene_id 'G2';", "gene_id 'G3';"]
}
annotation_data = pd.DataFrame(gtf_data)

# Mock Dataset 2: 1000 Genomes Project Data
genomes_data = pd.DataFrame({
    "ID": ["rs1", "rs2", "rs3", "rs4", "rs5"],
    "Genotype": ["AA", "AG", "GG", "CT", "TT"],
    "Population": ["EUR", "AFR", "EAS", "EUR", "AFR"],
    "Functional Annotation": ["coding", "regulatory", "intronic", "coding", "intronic"]
})

# Mock Dataset 3: DNA Sequence Base Counts
dna_base_counts = {'A': 120, 'T': 100, 'C': 80, 'G': 90}

# 1. Feature Distribution in GTF Annotation Data
if not annotation_data.empty and 'Feature' in annotation_data.columns:
    plt.figure(figsize=(10, 6))
    feature_counts = annotation_data['Feature'].value_counts()
    feature_counts.plot(kind='bar', color='skyblue')
    plt.title('Feature Distribution in GTF Annotation Data')
    plt.xlabel('Feature Type')
    plt.ylabel('Count')
    plt.grid(axis='y')
    plt.xticks(rotation=45)
    plt.show()
else:
    print("Feature data not available for visualization.")

# 2. Population Distribution in 1000 Genomes Project Data
if not genomes_data.empty and 'Population' in genomes_data.columns:
    plt.figure(figsize=(12, 6))
    sns.countplot(
        data=genomes_data, 
        x='Population', 
        order=genomes_data['Population'].value_counts().index, 
        palette='viridis'
    )
    plt.title('Population Distribution in 1000 Genomes Data')
    plt.xlabel('Population')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.show()
else:
    print("Population data not available for visualization.")

# 3. Genomic Start and End Positions
if not annotation_data.empty:
    plt.figure(figsize=(10, 6))
    sns.histplot(annotation_data['Start'], bins=50, kde=False, color='green', label='Start')
    sns.histplot(annotation_data['End'], bins=50, kde=False, color='red', label='End')
    plt.title('Distribution of Genomic Start and End Positions')
    plt.xlabel('Genomic Position')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid()
    plt.show()
else:
    print("Start and End position data not available.")

# 4. Base Count Visualization (Pie Chart)
# if dna_base_counts:
#     plt.figure(figsize=(8, 8))
#     plt.pie(
#         dna_base_counts.values(), 
#         labels=dna_base_counts.keys(), 
#         autopct='%1.1f%%', 
#         colors=sns.color_palette('pastel')
#     )
#     plt.title('Base Composition in DNA Sequence')
#     plt.show()
# else:
#     print("No base counts available for visualization.")

