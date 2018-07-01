# GenomicsSnakemake

This is a repository for the genomics workflows based on Snakemake workflow managment system.
More information can be found in [snakemake readthedocs](https://snakemake.readthedocs.io/en/stable/).

# Requirements

  * snakemake version 5.1.5
  * tools that you want to execute (e.g. bowtie2/hisate2 and so on)
  * fastq-mcf or cutadapt (adapter trimmer)
  * hisat2 (RNAseq) 
  * bwa/bowtie2 (other genomics application)
  * macs2 (peak caller)
  * featureCount (RNAseq)

## Getting Started

An RNAseq workflow is defined in the RNAseq directory.
  * workflow.py: defines the set of rules that are applied
  * config.yml: yaml file that defines the configuration and parameters for the rules


```{shell}
cd RNAseq/
snakemake -s workflow.py

```



# References

Köster, Johannes and Rahmann, Sven. "Snakemake - A scalable bioinformatics workflow engine". Bioinformatics 2012.

